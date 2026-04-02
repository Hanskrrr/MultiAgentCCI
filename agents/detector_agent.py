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

    def process(self, state: CodeCommentState) -> CodeCommentState:
        state.log(f"[{self.name}] Starting consistency detection analysis...")

        system_prompt = (
            "You are a strict Software Quality Auditor. Your goal is to detect whether the "
            "Original Comment accurately describes the given Current Code after updates."
        )
        prompt = f"""
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Original Comment]
{state.original_comment}

[Current Code]
{state.code_snippet}

[Code Context]
- Signature: {state.interface_context}
- Intent: {state.intention_context}

Classification Guidelines (IMPORTANT):

=== @param Rules ===
1. Exact Name Matching: If a comment documents a parameter (e.g., "@param file") but the code signature uses a different name (e.g., "requiredFile"), it is INCONSISTENT (Rename Drift).
2. Type Precision: If a comment specifies a type (e.g., "@param float x") but the code uses a different type (e.g., "double x"), it is INCONSISTENT (Type Drift).

=== @return Rules ===
3. Return Class/Type Name Matching: If the comment mentions a SPECIFIC class name (e.g., "HornetQConnectionFactory", "JMenuItem", "HttpServletRequest") but the code returns a DIFFERENT class (e.g., "ActiveMQConnectionFactory", "ZapMenuItem", "AtmosphereRequest"), it is INCONSISTENT. Class names must match exactly — renaming a class is NOT paraphrasing.
4. Unit / Precision Mismatch: If the comment specifies a unit (e.g., "in milliseconds") but the code uses a different unit (e.g., seconds), or a qualifier like "this same object" when the code returns a new object, it is INCONSISTENT.
5. Missing Return Condition: If the code has conditional branches that return null, throw exceptions, or return a fallback value, but the comment omits these conditions, it is INCONSISTENT. Look carefully at all return paths and null checks.
6. Semantic Over-specification: If the comment adds qualifiers, details, or attributions (e.g., "used by this SVGGraphics2D instance", "on the test VirtualHost") that no longer match the actual code, it is INCONSISTENT.

=== General Rules ===
7. Tolerate ONLY Variable-to-NaturalLanguage Paraphrasing: A comment like "@return the parent type information" for code `return parentInfo` is CONSISTENT — describing a variable name in natural language is acceptable. However, substituting one CLASS NAME for another (e.g., "HornetQ" for "ActiveMQ") is NOT paraphrasing — it is INCONSISTENT.
8. CONSISTENT if and only if: All parameter names match, all class/type names mentioned in the comment match the code, the return behavior is accurately described, no important conditions (null, exceptions, edge cases) are omitted, and units/qualifiers are correct.

Benchmark Examples for Calibration:
- Ex A (INCONSISTENT, @param): Comment: "@param file to upload", Code: "upload(File requiredFile)" -> Name mismatch.
- Ex B (INCONSISTENT, @param): Comment: "@param float x", Code: "distance(double x)" -> Type mismatch.
- Ex C (INCONSISTENT, @return, class rename): Comment: "@return the HornetQConnectionFactory", Code returns ActiveMQConnectionFactory -> Class name changed.
- Ex D (INCONSISTENT, @return, class rename): Comment: "@return javax.swing.JMenuItem", Code returns ZapMenuItem -> Class name changed.
- Ex E (INCONSISTENT, @return, missing null): Comment: "@return an instance of Foo", Code can return null on failure but comment omits this.
- Ex F (INCONSISTENT, @return, missing condition): Comment: "@return read-only view of headers", Code: `return headers == null ? null : unmodifiableMap(headers)` -> Missing "or null if none are set".
- Ex G (INCONSISTENT, @return, unit error): Comment: "@return max time in milliseconds", Code variable is actually in seconds -> Unit mismatch.
- Ex H (INCONSISTENT, @return, identity): Comment: "@return this same sentence", Code: `return new Sentence(...)` -> Returns new object, not "this same".
- Ex I (CONSISTENT): Comment: "@return the parent type information", Code: `return parentInfo;` -> Variable name described in natural language, meaning aligns.
- Ex J (CONSISTENT): Code changed internal logic but all names, types, return behavior, and conditions still match the comment -> CONSISTENT.

Output Requirement:
Reasoning: <Direct comparison of identifiers and types mentioned in the comment vs the code signature>
CONCLUSION: [CONSISTENT or INCONSISTENT]
"""

        try:
            response = self._call_llm(prompt, system_prompt)
            # Parse verdict
            upper_response = response.upper()
            if "CONCLUSION: INCONSISTENT" in upper_response:
                state.is_consistent = False
                state.inconsistency_reason = response.split("CONCLUSION:")[0].strip()
            elif "CONCLUSION: CONSISTENT" in upper_response:
                state.is_consistent = True
                state.inconsistency_reason = ""
            else:
                # Fallback
                if (
                    "INCONSISTENT" in upper_response
                    and "CONSISTENT" not in upper_response
                ):
                    state.is_consistent = False
                    state.inconsistency_reason = response.strip()
                else:
                    state.is_consistent = True
                    state.inconsistency_reason = ""

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
