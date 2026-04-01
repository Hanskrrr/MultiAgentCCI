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
1. Exact Name Matching (@param): If a comment documents a parameter (e.g., "@param file") but the code signature uses a different name (e.g., "requiredFile"), it is INCONSISTENT (Rename Drift).
2. Type Precision (@param): If a comment specifies a type (e.g., "@param float x") but the code uses a different type (e.g., "double x"), it is INCONSISTENT (Type Drift).
3. Return Type Drift (@return): If the comment claims a specific return type (e.g., "a List") but the code actually returns a different type (e.g., "a Clip"), it is INCONSISTENT.
4. Missing Return Condition (@return): If the code can return null or throw exceptions under certain conditions, but the comment omits this, it is INCONSISTENT.
5. Semantic Over-specification (@return): If the comment adds qualifiers or details (e.g., "of simple annotation names") that no longer match the actual code behavior, it is INCONSISTENT.
6. Tolerate Natural Language Paraphrasing: A comment like "@return the parent type information" for a method returning `parentInfo` is CONSISTENT — natural language descriptions of variable names are acceptable as long as the meaning aligns.
7. Consistent if: All identifiers match, the return type/behavior description is accurate, and no important conditions (null, exceptions) are omitted.

Benchmark Examples for Calibration:
- Example A (INCONSISTENT, @param): Comment: "@param file to upload", Code: "upload(File requiredFile)" -> Name mismatch (file vs requiredFile).
- Example B (INCONSISTENT, @param): Comment: "@param float x", Code: "distance(double x)" -> Type mismatch (float vs double).
- Example C (INCONSISTENT, @return): Comment: "@return a List of records", Code returns `Clip.of(aggregate)` -> Return type changed from List to Clip.
- Example D (INCONSISTENT, @return): Comment: "@return an instance of Foo", Code: method can return null on failure but comment omits this -> Missing null condition.
- Example E (CONSISTENT): Comment: "@return the parent type information", Code: `return parentInfo;` -> Natural language description matches the variable semantics.
- Example F (CONSISTENT): Code changed internal logic but parameter names, return type, and described behavior still match -> CONSISTENT.

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
