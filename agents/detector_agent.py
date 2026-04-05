import re
from .base_agent import BaseAgent
from core.state import CodeCommentState


class DetectorAgent(BaseAgent):
    """
    一致性检测智能体：
    基于代码片段、原始注释以及被解析出的多维度上下文，
    判断代码与注释是否具有一致性。
    """

    def __init__(self, model_name: str = "glm-4-flash", retriever=None):
        super().__init__(name="DetectorAgent", model_name=model_name)
        self.retriever = retriever

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
        ast_ctx = getattr(state, "ast_context", {}) or {}

        # --- Return type: prefer tree-sitter, fall back to LLM-parsed context ---
        if ast_ctx.get("return_type"):
            return_type = ast_ctx["return_type"]
        else:
            return_type = self._extract_return_type_from_context(state.interface_context)

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
        if "has_null_return" in ast_ctx:
            has_null = ast_ctx["has_null_return"]
        else:
            has_null = re.search(r"\breturn\s+null\b", code, flags=re.IGNORECASE) is not None

        if has_null and "null" not in comment_lower:
            hard_fail_reasons.append(
                "Code contains 'return null' branch but @return comment does not mention null."
            )
        elif has_null:
            signals.append("Code has an explicit null return branch.")

        # --- Empty collection return (tree-sitter only) ---
        if ast_ctx.get("has_empty_return") and "empty" not in comment_lower:
            signals.append(
                "Code returns empty collection/Optional but comment does not mention empty case."
            )

        # --- Throws: prefer tree-sitter, fall back to regex ---
        if ast_ctx.get("throws"):
            throws_list = ast_ctx["throws"]
            if not any(w in comment_lower for w in ("throw", "exception", "error")):
                signals.append(
                    f"Method throws {throws_list} but comment does not mention exceptions."
                )
        else:
            has_throws = re.search(r"\bthrows\b", code, flags=re.IGNORECASE) is not None
            if has_throws and not any(w in comment_lower for w in ("throw", "exception")):
                signals.append(
                    "Method signature indicates exceptions (throws), "
                    "but @return comment does not mention exceptions."
                )

        # --- Multiple return paths (tree-sitter only) ---
        ret_exprs = ast_ctx.get("return_expressions", [])
        if len(ret_exprs) > 1:
            signals.append(f"Method has {len(ret_exprs)} distinct return paths.")

        return hard_fail_reasons, signals

    def _parse_model_conclusion(self, response: str) -> tuple:
        upper_response = response.upper()
        if "CONCLUSION: INCONSISTENT" in upper_response:
            return False, response.split("CONCLUSION:")[0].strip()
        if "CONCLUSION: CONSISTENT" in upper_response:
            return True, ""

        # Fallback
        if "INCONSISTENT" in upper_response and "CONSISTENT" not in upper_response:
            return False, response.strip()
        return True, ""

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

    def _build_prompt(self, state: CodeCommentState, comment_type: str, signals: list) -> str:
        common_head = f"""
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
{comment_type}

[Original Comment]
{state.original_comment}

[Current Code]
{state.code_snippet}

[Code Context]
- Signature: {state.interface_context}
- Intent: {state.intention_context}
"""

        signal_block = ""
        if signals:
            signal_text = "\n".join([f"- {s}" for s in signals])
            signal_block = f"""
[Rule-based Signals]
{signal_text}
These are deterministic signals extracted from code/comment. Treat them as high-priority evidence.
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

=== @return Rules (Primary Focus) ===
1. Return Class/Type Name Matching: If the comment mentions a SPECIFIC class name (e.g., "HornetQConnectionFactory", "JMenuItem", "HttpServletRequest") but the code returns a DIFFERENT class (e.g., "ActiveMQConnectionFactory", "ZapMenuItem", "AtmosphereRequest"), it is INCONSISTENT. Class names must match exactly — renaming a class is NOT paraphrasing.
2. Unit / Precision Mismatch: If the comment specifies a unit (e.g., "in milliseconds") but the code uses a different unit (e.g., seconds), or a qualifier like "this same object" when the code returns a new object, it is INCONSISTENT.
3. Missing Return Condition: If the code has conditional branches that return null, throw exceptions, or return a fallback value, but the comment omits these conditions, it is INCONSISTENT. Look carefully at ALL return paths and null checks.
4. Semantic Over-specification: If the comment adds qualifiers, details, or attributions (e.g., "used by this SVGGraphics2D instance", "on the test VirtualHost") that no longer match the actual code, it is INCONSISTENT.

=== General Rules ===
5. Tolerate ONLY Variable-to-NaturalLanguage Paraphrasing: A comment like "@return the parent type information" for code `return parentInfo` is CONSISTENT. However, substituting one CLASS NAME for another (e.g., "HornetQ" for "ActiveMQ") is NOT paraphrasing — it is INCONSISTENT.
6. CONSISTENT if and only if: All class/type names mentioned in the comment match the code, the return behavior is accurately described, no important conditions (null, exceptions, edge cases) are omitted, and units/qualifiers are correct.
"""
            examples_block = self._get_return_examples(state)

            return (
                common_head
                + signal_block
                + guidelines
                + examples_block
                + """
Output Requirement:
Reasoning: <Compare @return semantics, return type/class names, and return-path conditions step by step>
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
