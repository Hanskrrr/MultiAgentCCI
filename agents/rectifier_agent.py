from .base_agent import BaseAgent
from core.state import CodeCommentState


class RectifierAgent(BaseAgent):
    """
    注释修正智能体：
    在检测到不一致后，根据检测报告和结构化上下文生成修正后的注释。
    """

    def __init__(self, model_name: str = "glm-4-flash"):
        super().__init__(name="RectifierAgent", model_name=model_name)

    def process(self, state: CodeCommentState) -> CodeCommentState:
        if state.is_consistent is True:
            state.log(
                f"[{self.name}] State is consistent, no rectification needed. Skipping..."
            )
            return state

        state.log(
            f"[{self.name}] Starting comment rectification based on detection report..."
        )

        system_prompt = (
            "You are a Senior Technical Writer. Your task is to fix outdated or incorrect "
            "code comments to match the actual code logic. Provide the revised comment ONLY."
        )

        prompt = f"""
The following code and its comment are INCONSISTENT.

[Original Comment]
{state.original_comment}

[Current Code]
{state.code_snippet}

[Context Analysis]
- Intent: {state.intention_context}
- Interface: {state.interface_context}
- Implementation: {state.implementation_context}

[Detection Report - Reasons for Inconsistency]
{state.inconsistency_reason}

Task: Rectify the [Original Comment] to align with the [Current Code].
Constraints:
1. Minimal Edit Principle: Retain as much of the original wording as possible. Only fix the factual errors or missing information.
2. Accuracy: Ensure all parameter names and return logic reflect the Current Code.
3. Format: Maintain the original comment style (e.g., Javadoc, single-line).

Output: ONLY the revised comment text.
"""
        try:
            response = self._call_llm(prompt, system_prompt)
            state.rectified_comment = response.strip()
            state.log(f"[{self.name}] Comment rectified successfully.")
        except Exception as e:
            state.log(f"[{self.name}] 模型调用异常: {e}")
            state.rectified_comment = state.original_comment

        return state
