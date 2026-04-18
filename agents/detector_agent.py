import difflib
import re
from typing import Dict, List
from .base_agent import BaseAgent
from core.state import CodeCommentState
from core.java_parser import parse_java_method


class DetectorAgent(BaseAgent):
    """
    一致性检测智能体：
    基于代码片段、原始注释以及被解析出的多维度上下文，
    判断代码与注释是否具有一致性。
    """

    def __init__(self, model_name: str = "glm-4-flash", retriever=None, use_treesitter: bool = True):
        super().__init__(name="DetectorAgent", model_name=model_name)
        self.retriever = retriever
        self.use_treesitter = use_treesitter

    def _detect_comment_type(self, comment: str) -> str:
        c = comment.lower()
        if "@param" in c:
            return "param"
        if "@return" in c:
            return "return"
        return "summary"

    def _normalize_type_name(self, type_name: str) -> str:
        t = re.sub(r"<.*?>", "", type_name).strip()
        t = t.split(".")[-1]
        t = t.replace("[]", "")
        return t.lower()

    def _extract_return_type_from_context(self, interface_context: str) -> str:
        # Context parser formats as: "Full Signature: name(args) -> return_type"
        marker = "->"
        if marker not in interface_context:
            return ""
        return interface_context.split(marker, 1)[1].strip().split("\n")[0].strip()

    def _extract_explicit_return_type_mentions(self, comment: str) -> list:
        mentions = []
        # e.g., {@link HttpServletRequest}
        mentions += re.findall(r"\{@link\s+([A-Za-z0-9_$.]+)\}", comment)
        # e.g., javax.swing.JMenuItem
        mentions += re.findall(r"\b([A-Z][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+)+)\b", comment)
        # e.g., ActiveMQConnectionFactory, ObjectName, Optional
        mentions += re.findall(
            r"\b([A-Z][A-Za-z0-9_]*(?:Factory|Request|Response|Builder|Manager|Item|ObjectName|Optional|Map|List|Set|View|Sentence|Parser))\b",
            comment,
        )
        # Keep order while deduplicating
        seen = set()
        uniq = []
        for m in mentions:
            if m not in seen:
                seen.add(m)
                uniq.append(m)
        return uniq

    def _rule_check_return(self, state: CodeCommentState) -> tuple:
        hard_fail_reasons = []
        signals = []

        comment = state.original_comment
        comment_lower = comment.lower()
        code = state.code_snippet
        ast_ctx = (getattr(state, "ast_context", {}) or {}) if self.use_treesitter else {}

        # --- Return type: prefer tree-sitter, fall back to LLM-parsed context ---
        if ast_ctx.get("return_type"):
            return_type = ast_ctx["return_type"]
        else:
            return_type = self._extract_return_type_from_context(state.interface_context)

        # --- Hard rule 0: void method but @return has content → INCONSISTENT ---
        if return_type and return_type.strip().lower() == "void":
            return_content = re.sub(r"@return\s*", "", comment, flags=re.IGNORECASE).strip()
            if return_content and len(return_content) > 2:
                hard_fail_reasons.append(
                    f"Method returns void but @return comment describes a value: '{return_content[:80]}'."
                )

        norm_return = self._normalize_type_name(return_type) if return_type else ""
        mentions = self._extract_explicit_return_type_mentions(comment)

        if return_type:
            signals.append(f"Parsed return type from signature: {return_type}")
        if mentions:
            signals.append(f"Explicit return type mentions in comment: {mentions}")

        # Hard rule 1: explicit class/type mention must match parsed return type
        if norm_return and mentions:
            compatible = False
            for m in mentions:
                nm = self._normalize_type_name(m)
                if nm == norm_return or nm.endswith(norm_return) or norm_return.endswith(nm):
                    compatible = True
                    break
            if not compatible:
                hard_fail_reasons.append(
                    f"Return type/class mismatch: comment mentions {mentions}, "
                    f"but code signature returns {return_type}."
                )

        # --- Null return: prefer tree-sitter, fall back to regex ---
        # Only flag when a top-level "return null;" statement exists,
        # not null literals inside ternaries, constructor args, or inner classes.
        if "has_null_return" in ast_ctx:
            has_null = ast_ctx["has_null_return"]
        else:
            # Stricter regex: "return null;" on its own line, not inside ternary or expression
            has_null = re.search(r"^\s*return\s+null\s*;", code, flags=re.MULTILINE) is not None

        if has_null and "null" not in comment_lower:
            signals.append(
                "Code contains 'return null' branch but @return comment does not mention null."
            )
        elif has_null:
            signals.append("Code has an explicit null return branch.")

        # --- Empty collection return (tree-sitter only) ---
        if ast_ctx.get("has_empty_return") and "empty" not in comment_lower:
            signals.append(
                "Code returns empty collection/Optional but comment does not mention empty case."
            )

        # --- Throws: demoted to signal (FP-prone as @return doesn't require mentioning exceptions) ---
        if ast_ctx.get("throws"):
            throws_list = ast_ctx["throws"]
            if not any(w in comment_lower for w in ("throw", "exception", "error", "illegal")):
                signals.append(
                    f"Method declares throws {throws_list} but @return comment "
                    f"does not mention exceptions."
                )
        else:
            has_throws = re.search(r"\bthrows\b", code, flags=re.IGNORECASE) is not None
            if has_throws and not any(w in comment_lower for w in ("throw", "exception")):
                signals.append(
                    "Method signature indicates exceptions (throws), "
                    "but @return comment does not mention exceptions."
                )

        # --- Structural diff signals (old_code vs new_code comparison) ---
        structural_signals = self._structural_diff_signals(state)
        signals.extend(structural_signals)

        return hard_fail_reasons, signals

    def _parse_model_conclusion(self, response: str) -> tuple:
        upper_response = response.upper()
        reasoning = response.split("CONCLUSION:")[0].strip() if "CONCLUSION:" in response else response.strip()
        if "CONCLUSION: INCONSISTENT" in upper_response:
            return False, reasoning
        if "CONCLUSION: CONSISTENT" in upper_response:
            return True, reasoning

        # Fallback
        if "INCONSISTENT" in upper_response and "CONSISTENT" not in upper_response:
            return False, reasoning
        return True, reasoning

    _STATIC_RETURN_EXAMPLES = """
Benchmark Examples for Calibration:
- Ex A (INCONSISTENT, class rename): Comment: "@return the HornetQConnectionFactory", Code returns ActiveMQConnectionFactory -> Class name changed.
- Ex B (INCONSISTENT, class rename): Comment: "@return javax.swing.JMenuItem", Code returns ZapMenuItem -> Class name changed.
- Ex C (INCONSISTENT, missing null): Comment: "@return an instance of Foo", Code can return null on failure but comment omits this.
- Ex D (INCONSISTENT, missing condition): Comment: "@return read-only view of headers", Code: `return headers == null ? null : unmodifiableMap(headers)` -> Missing "or null if none are set".
- Ex E (INCONSISTENT, unit error): Comment: "@return max time in milliseconds", Code variable is actually in seconds -> Unit mismatch.
- Ex F (INCONSISTENT, identity): Comment: "@return this same sentence", Code: `return new Sentence(...)` -> Returns new object, not "this same".
- Ex G (CONSISTENT): Comment: "@return the parent type information", Code: `return parentInfo;` -> Variable name described in natural language, meaning aligns.
- Ex H (CONSISTENT): Code changed internal logic but return type, behavior, and conditions still match -> CONSISTENT.
"""

    def _get_return_examples(self, state: CodeCommentState) -> str:
        if self.retriever is None:
            return self._STATIC_RETURN_EXAMPLES
        try:
            examples = self.retriever.retrieve(
                comment=state.original_comment,
                code=state.code_snippet,
                top_k=3,
                ensure_mix=True,
            )
            if not examples:
                return self._STATIC_RETURN_EXAMPLES
            return self.retriever.format_examples(examples)
        except Exception:
            return self._STATIC_RETURN_EXAMPLES

    def _build_code_diff(self, state: CodeCommentState) -> str:
        """Generate a unified diff between old and new code if old_code is available."""
        old = getattr(state, "old_code_snippet", "") or ""
        if not old.strip():
            return ""
        old_lines = old.strip().splitlines(keepends=True)
        new_lines = state.code_snippet.strip().splitlines(keepends=True)
        diff = list(difflib.unified_diff(old_lines, new_lines, fromfile="old_code", tofile="new_code", lineterm=""))
        if not diff:
            return ""
        diff_text = "\n".join(diff[:60])
        return diff_text

    # ------------------------------------------------------------------
    # Structural diff: compare old and new code structure
    # ------------------------------------------------------------------

    @staticmethod
    def _extract_identifiers(code: str) -> set:
        """Extract all camelCase / PascalCase identifiers from code."""
        return set(re.findall(r"\b[a-zA-Z_]\w*\b", code))

    def _structural_diff_signals(self, state: CodeCommentState) -> List[str]:
        """Compare old_code vs new_code structurally. Return hard signals for the detector."""
        old_code = getattr(state, "old_code_snippet", "") or ""
        if not old_code.strip():
            return []

        signals: List[str] = []
        new_code = state.code_snippet

        # --- tree-sitter structural comparison ---
        old_parsed = parse_java_method(old_code)
        new_parsed = parse_java_method(new_code)

        if old_parsed and new_parsed:
            # Return type change
            old_rt = old_parsed.get("return_type", "")
            new_rt = new_parsed.get("return_type", "")
            if old_rt and new_rt and old_rt != new_rt:
                signals.append(
                    f"RETURN TYPE CHANGED: '{old_rt}' -> '{new_rt}'. "
                    f"If the comment references the old return type, it is INCONSISTENT."
                )

            # Parameter changes
            old_params = {p["name"]: p["type"] for p in old_parsed.get("parameters", [])}
            new_params = {p["name"]: p["type"] for p in new_parsed.get("parameters", [])}
            removed = set(old_params) - set(new_params)
            added = set(new_params) - set(old_params)
            if removed or added:
                parts = []
                if removed:
                    parts.append(f"removed params: {removed}")
                if added:
                    parts.append(f"added params: {added}")
                signals.append(f"PARAMETERS CHANGED: {'; '.join(parts)}.")

            # Throws changes
            old_throws = set(old_parsed.get("throws", []))
            new_throws = set(new_parsed.get("throws", []))
            if old_throws != new_throws:
                signals.append(
                    f"THROWS CHANGED: {old_throws or 'none'} -> {new_throws or 'none'}."
                )

            # Method name change (rare but possible with overloads in dataset)
            old_name = old_parsed.get("method_name", "")
            new_name = new_parsed.get("method_name", "")
            if old_name and new_name and old_name != new_name:
                signals.append(f"METHOD NAME CHANGED: '{old_name}' -> '{new_name}'.")
        elif not old_parsed or not new_parsed:
            # Fallback: regex-based return type extraction for non-Java or parse failures
            old_rt_match = re.search(r"\b(public|private|protected|static|\s)+([\w<>\[\]]+)\s+\w+\s*\(", old_code)
            new_rt_match = re.search(r"\b(public|private|protected|static|\s)+([\w<>\[\]]+)\s+\w+\s*\(", new_code)
            if old_rt_match and new_rt_match:
                old_rt = old_rt_match.group(2).strip()
                new_rt = new_rt_match.group(2).strip()
                if old_rt != new_rt:
                    signals.append(
                        f"RETURN TYPE CHANGED: '{old_rt}' -> '{new_rt}'. "
                        f"If the comment references the old return type, it is INCONSISTENT."
                    )

        # --- Identifier drift: find renamed identifiers between old and new code ---
        old_ids = self._extract_identifiers(old_code)
        new_ids = self._extract_identifiers(new_code)
        comment_lower = state.original_comment.lower()

        disappeared = old_ids - new_ids
        appeared = new_ids - old_ids
        # Check if any disappeared identifier is mentioned in the comment
        for old_id in disappeared:
            if len(old_id) < 4:
                continue
            if old_id.lower() in comment_lower:
                # See if there's a plausible rename in new code
                candidates = [n for n in appeared if len(n) >= 4 and n[0].lower() == old_id[0].lower()]
                if candidates:
                    signals.append(
                        f"IDENTIFIER DRIFT: comment mentions '{old_id}' which no longer exists in new code. "
                        f"Possible renames: {candidates[:3]}."
                    )
                else:
                    signals.append(
                        f"IDENTIFIER DRIFT: comment mentions '{old_id}' which no longer exists in new code."
                    )

        return signals

    def _build_prompt(self, state: CodeCommentState, comment_type: str, signals: list) -> str:
        diff_text = self._build_code_diff(state)
        diff_block = ""
        if diff_text:
            diff_block = f"""
[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
{diff_text}
```
"""

        common_head = f"""
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
{comment_type}

[Original Comment]
{state.original_comment}

[Current Code]
{state.code_snippet}
{diff_block}
[Code Context]
- Signature: {state.interface_context}
- Intent: {state.intention_context}
"""

        signal_block = ""
        if signals:
            signal_text = "\n".join([f"- {s}" for s in signals])
            signal_block = f"""
[Rule-based Signals — HIGH PRIORITY]
{signal_text}
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
"""

        if comment_type == "param":
            return (
                common_head
                + signal_block
                + """
Classification Guidelines (IMPORTANT):

=== @param Rules (Primary Focus) ===
1. Exact Name Matching: If a comment documents a parameter (e.g., "@param file") but the code signature uses a different name (e.g., "requiredFile"), it is INCONSISTENT (Rename Drift).
2. Type Precision: If a comment specifies a type (e.g., "@param float x") but the code uses a different type (e.g., "double x"), it is INCONSISTENT (Type Drift).
3. Logic Drift: If the core functional behavior described in the comment has changed, it is INCONSISTENT.
4. Be strict on identifier drift; do not forgive renames or synonym substitutions for parameter names.

=== General Rules ===
5. Tolerate Natural Language Paraphrasing ONLY for variable-to-description (e.g., `userId` described as "user ID" is fine).
6. CONSISTENT if: All parameter identifiers match the code signature EXACTLY, types are correct, and the functional description remains accurate.

Benchmark Examples for Calibration:
- Ex A (INCONSISTENT): Comment: "@param file to upload", Code: "upload(File requiredFile)" -> Name mismatch (file vs requiredFile).
- Ex B (INCONSISTENT): Comment: "@param float x", Code: "distance(double x)" -> Type mismatch (float vs double).
- Ex C (CONSISTENT): Code changed internal logic but parameter name and types match the description -> CONSISTENT.

Output Requirement:
Reasoning: <Direct comparison of identifiers and types mentioned in the comment vs the code signature>
CONCLUSION: [CONSISTENT or INCONSISTENT]
"""
            )

        if comment_type == "return":
            guidelines = """
Classification Guidelines (IMPORTANT):

=== Claim-by-Claim Verification (you MUST follow this) ===
Break the comment into individual claims, then verify EACH against the current code:

1. CLASS/TYPE NAME: Does the comment mention a specific class name (e.g., "SqlParser", "AsyncAppenderBase", "HornetQConnectionFactory")? If so, does the code ACTUALLY return that exact class? A renamed class is INCONSISTENT.
2. QUALIFIER/OWNER: Does the comment mention a specific owner, source, or context (e.g., "used by this SVGGraphics2D instance", "on the test VirtualHost", "the supplied foreground color")? Verify each qualifier still matches the current code. Extra or outdated qualifiers make it INCONSISTENT.
3. UNIT/PRECISION: Does the comment mention a unit (e.g., "milliseconds", "seconds") or precision? If the code uses a different unit, it is INCONSISTENT.
4. RETURN CONDITIONS: Does the comment describe return conditions (e.g., "or null if...", "false otherwise")? Are ALL conditions still present in the code? Missing conditions = INCONSISTENT.
5. DESCRIPTIVE ACCURACY: Does the comment describe what is returned (e.g., "the union of the char[]s" vs "the char[]")? Does the description PRECISELY match what the code does? If the method is named "union()" but the comment just says "the char[]" without mentioning union, it is INCONSISTENT.

=== If Code Change Diff is provided ===
6. Check EVERY changed line in the diff. If any change invalidates ANY word or claim in the comment, it is INCONSISTENT.
7. Pay special attention to: renamed variables/methods, changed return types, removed/added parameters, changed logic flow.

=== Paraphrasing Rules ===
8. Tolerate ONLY variable-name-to-natural-language (e.g., `parentInfo` described as "parent type information" is fine).
9. Substituting one CLASS NAME for another is NEVER paraphrasing — it is INCONSISTENT.
"""
            examples_block = self._get_return_examples(state)

            return (
                common_head
                + signal_block
                + guidelines
                + examples_block
                + """
Output Requirement:
Reasoning: Break the comment into claims and verify each one:
- Claim 1: "<extract first claim from comment>" → matches code? YES/NO
- Claim 2: "<extract second claim>" → matches code? YES/NO
- ...
If ANY claim is NO → INCONSISTENT. If ALL claims are YES → CONSISTENT.
CONCLUSION: [CONSISTENT or INCONSISTENT]
"""
            )

        return (
            common_head
            + signal_block
            + """
Classification Guidelines (IMPORTANT):

=== Summary Rules (Primary Focus) ===
1. Functional Accuracy: The summary must align with the current code behavior.
2. Critical Drift: If the operation, object, or target described in the summary has changed, it is INCONSISTENT.
3. Identifier/Class Changes: If the summary references specific class names or method targets that have been renamed, it is INCONSISTENT.

=== General Rules ===
4. Tolerate minor wording changes without semantic drift.
5. CONSISTENT if: The summary accurately reflects the current code's purpose, objects, and behavior.

Benchmark Examples for Calibration:
- Ex A (INCONSISTENT): Summary says "Creates elastic node as single member of a cluster", but code now creates an instance with existing settings -> Purpose changed.
- Ex B (CONSISTENT): Summary says "Sends an email to the given address", code still does `smtp.send(to_addr, content)` -> Meaning unchanged.

Output Requirement:
Reasoning: <Compare summary semantics with current code behavior>
CONCLUSION: [CONSISTENT or INCONSISTENT]
"""
        )

    def process(self, state: CodeCommentState) -> CodeCommentState:
        state.log(f"[{self.name}] Starting consistency detection analysis...")

        system_prompt = (
            "You are a strict Software Quality Auditor. Your goal is to detect whether the "
            "Original Comment accurately describes the given Current Code after updates."
        )
        comment_type = self._detect_comment_type(state.original_comment)
        state.detected_comment_type = comment_type
        signals = []
        hard_fail_reasons = []
        if comment_type == "return":
            hard_fail_reasons, signals = self._rule_check_return(state)
            state.rule_signals = signals
            state.rule_hard_fails = hard_fail_reasons
            if hard_fail_reasons:
                state.is_consistent = False
                state.inconsistency_reason = " | ".join(hard_fail_reasons)
                state.detection_method = "rule"
                state.log(
                    f"[{self.name}] Rule-based return check flagged inconsistency: {state.inconsistency_reason[:120]}..."
                )
                return state

        prompt = self._build_prompt(state, comment_type, signals)

        try:
            response = self._call_llm(prompt, system_prompt)
            state.is_consistent, state.inconsistency_reason = self._parse_model_conclusion(
                response
            )
            state.detection_method = "llm"

            if state.is_consistent:
                state.log(f"[{self.name}] Detection Passed: Comment is consistent.")
            else:
                state.log(
                    f"[{self.name}] Inconsistency found (Reason: {state.inconsistency_reason[:100]}...)"
                )

        except Exception as e:
            state.log(f"[{self.name}] Model calling exception: {e}")
            state.detection_method = "llm_error"
            state.is_consistent = True
            state.inconsistency_reason = f"LLM call failed: {e}"

        return state
