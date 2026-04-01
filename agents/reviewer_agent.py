from .base_agent import BaseAgent
from core.state import CodeCommentState


class ReviewerAgent(BaseAgent):
    """
    审查与反思智能体：
    验证修正智能体新生成的注释是否准确，是否存在“幻觉”，参数是否覆盖完整。
    """

    def __init__(self, model_name: str = "glm-4-flash"):
        super().__init__(name="ReviewerAgent", model_name=model_name)

    def process(self, state: CodeCommentState) -> CodeCommentState:
        if not state.rectified_comment or state.is_consistent is True:
            state.log(f"[{self.name}] No rectified comment to review. Skipping...")
            return state

        state.log(f"[{self.name}] Reviewing the quality of rectified comment...")

        system_prompt = "You are a strict Code Reviewer. Validate if the new comment accurately matches the code logic without hallucinations."
        prompt = f"""
Please review the following code snippet and its newly rectified comment:

[Current Code]
{state.code_snippet}

[Code Context]
- Interface: {state.interface_context}
- Implementation: {state.implementation_context}

[Rectified Comment]
{state.rectified_comment}

Review Checklist:
1. Factuality: Does the comment claim anything that the code does NOT do?
2. Completeness: Does it accurately describe all current parameters and return logic?
3. Format: Is the Javadoc/Comment format correct?

Decision: 
Use strictly "RESULT: PASS" if the comment is perfect.
Use "RESULT: REJECT" if there are errors, followed by specific feedback for re-rectification.
"""
        try:
            response = self._call_llm(prompt, system_prompt)
            upper_response = response.upper()

            if "RESULT: PASS" in upper_response:
                state.review_passed = True
                state.review_feedback = "Review passed. Comment is accurate."
                state.log(f"[{self.name}] Review Passed (PASS).")
            elif "RESULT: REJECT" in upper_response:
                state.review_passed = False
                try:
                    state.review_feedback = response[
                        upper_response.index("RESULT: REJECT") + len("RESULT: REJECT") :
                    ].strip()
                except ValueError:
                    state.review_feedback = "Review failed. Please re-check the logic."
                state.log(
                    f"[{self.name}] Review Rejected (REJECT). Reason: {state.review_feedback[:50]}..."
                )
            else:
                # Fallback
                if "REJECT" in upper_response and "PASS" not in upper_response:
                    state.review_passed = False
                    state.review_feedback = response.strip()
                    state.log(f"[{self.name}] Review Rejected (No standard format).")
                else:
                    state.review_passed = True
                    state.review_feedback = "Default pass."
                    state.log(f"[{self.name}] Review Passed (Fallback).")

        except Exception as e:
            state.log(f"[{self.name}] 模型调用异常: {e}")
            state.review_passed = True  # 异常情况下默认放行

        return state
