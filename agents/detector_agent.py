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
1. Exact Name Matching: If a comment documents a parameter (e.g., "@param file") but the code signature uses a different name (e.g., "requiredFile"), it is INCONSISTENT (Rename Drift).
2. Type Precision: If a comment specifies a type (e.g., "@param float x") but the code uses a different type (e.g., "double x"), it is INCONSISTENT (Type Drift).
3. Logic Drift: If the core functional behavior described in the comment has changed, it is INCONSISTENT.
4. Consistent if: All mentioned identifiers match the code signature EXACTLY, and the functional description remains accurate.

Benchmark Examples for Calibration:
- Example A (INCONSISTENT): Comment: "@param file to upload", Code: "upload(File requiredFile)" -> Name mismatch (file vs requiredFile).
- Example B (INCONSISTENT): Comment: "@param float x", Code: "distance(double x)" -> Type mismatch (float vs double).
- Example C (CONSISTENT): Code changed internal logic but parameter name and return type match the description -> CONSISTENT.

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
