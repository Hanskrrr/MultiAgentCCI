import re
from .base_agent import BaseAgent
from core.state import CodeCommentState


class DetectorAgent(BaseAgent):
    """
    一致性检测智能体：
    基于代码片段、原始注释以及被解析出的多维度上下文，
    判断代码与注释是否具有一致性。
    """

    def __init__(self, model_name: str = "glm-4-flash"):
        super().__init__(name="DetectorAgent", model_name=model_name)

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
        code = state.code_snippet
        return_type = self._extract_return_type_from_context(state.interface_context)
        norm_return = self._normalize_type_name(return_type) if return_type else ""
        mentions = self._extract_explicit_return_type_mentions(comment)

        if return_type:
            signals.append(f"Parsed return type from signature: {return_type}")
        if mentions:
            signals.append(f"Explicit return type mentions in comment: {mentions}")

        # Hard rule 1: explicit class/type mention must match parsed return type.
        if norm_return and mentions:
            compatible = False
            for m in mentions:
                nm = self._normalize_type_name(m)
                if nm == norm_return:
                    compatible = True
                    break
                if nm.endswith(norm_return) or norm_return.endswith(nm):
                    compatible = True
                    break
            if not compatible:
                hard_fail_reasons.append(
                    f"Return type/class mismatch: comment mentions {mentions}, but code signature returns {return_type}."
                )

        # Hard rule 2: code has an explicit null return path but comment omits null.
        has_return_null = re.search(r"\breturn\s+null\b", code, flags=re.IGNORECASE) is not None
        if has_return_null and "null" not in comment.lower():
            hard_fail_reasons.append(
                "Code contains 'return null' branch but @return comment does not mention null."
            )
        elif has_return_null:
            signals.append("Code has an explicit null return branch.")

        # Soft signal: method declares throws but comment omits exception signal.
        has_throws = re.search(r"\bthrows\b", code, flags=re.IGNORECASE) is not None
        if has_throws and ("throw" not in comment.lower() and "exception" not in comment.lower()):
            signals.append(
                "Method signature/logic indicates exceptions (throws), but @return comment does not mention exceptions."
            )

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
Classification Guidelines (@param focused):
1. Exact Name Matching: @param identifier must match code parameter name exactly.
2. Type Precision: @param type mentions must match signature types (e.g., float vs double is INCONSISTENT).
3. Logic/Intent Drift: If behavior described by the comment no longer matches code, mark INCONSISTENT.
4. Be strict on identifier drift; do not forgive renames.

Output Requirement:
Reasoning: <Direct comparison of identifiers and types in comment vs signature>
CONCLUSION: [CONSISTENT or INCONSISTENT]
"""
            )

        if comment_type == "return":
            return (
                common_head
                + signal_block
                + """
Classification Guidelines (@return focused):
1. Return Class/Type Matching: if comment explicitly names a class/type, it must match actual return type.
2. Return Conditions: if code can return null/fallback or throw exceptions relevant to return semantics, omissions in @return imply INCONSISTENT.
3. Unit/Qualifier Precision: unit words (seconds/milliseconds) and object identity qualifiers ("same object" vs "new object") must be accurate.
4. Tolerate variable-to-natural-language paraphrases ONLY when meaning is unchanged.
5. Do NOT treat class-name substitutions as paraphrases.

Output Requirement:
Reasoning: <Compare @return semantics, return type/class names, and return-path conditions>
CONCLUSION: [CONSISTENT or INCONSISTENT]
"""
            )

        return (
            common_head
            + signal_block
            + """
Classification Guidelines (summary focused):
1. Functional Accuracy: summary must align with current behavior.
2. Critical Drift: operation/object/target changes imply INCONSISTENT.
3. Minor wording changes without semantic drift are CONSISTENT.

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
            state.is_consistent = True

        return state
