import difflib
from .base_agent import BaseAgent
from core.state import CodeCommentState


class RectifierAgent(BaseAgent):
    """
    注释修正智能体：
    在检测到不一致后，根据检测报告和结构化上下文生成修正后的注释。
    支持 RAG 检索相似修正案例作为 few-shot 示范。
    """

    def __init__(self, model_name: str = "glm-4-flash", retriever=None, summary_retriever=None):
        super().__init__(name="RectifierAgent", model_name=model_name)
        self.retriever = retriever
        self.summary_retriever = summary_retriever

    def _build_code_diff(self, state: CodeCommentState) -> str:
        old = getattr(state, "old_code_snippet", "") or ""
        if not old.strip():
            return ""
        old_lines = old.strip().splitlines(keepends=True)
        new_lines = state.code_snippet.strip().splitlines(keepends=True)
        diff = list(difflib.unified_diff(old_lines, new_lines, fromfile="old", tofile="new", lineterm=""))
        if not diff:
            return ""
        return "\n".join(diff[:50])

    def _get_rag_examples(self, state: CodeCommentState) -> str:
        comment_type = getattr(state, "detected_comment_type", "")
        if comment_type == "summary" and self.summary_retriever is not None:
            retriever = self.summary_retriever
        else:
            retriever = self.retriever
        if retriever is None:
            return ""
        try:
            examples = retriever.retrieve_rectification_examples(
                comment=state.original_comment,
                code=state.code_snippet,
                top_k=3,
            )
            if not examples:
                return ""
            return retriever.format_rectification_examples(examples)
        except Exception:
            return ""

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
            "You are a Senior Technical Writer performing MINIMAL comment edits. "
            "Change ONLY the specific words that are factually wrong. "
            "Keep everything else exactly as-is. Output ONLY the corrected comment line."
        )

        diff_block = ""
        diff_text = self._build_code_diff(state)
        if diff_text:
            diff_block = f"""
[Code Change Diff] (what changed from old code to new code)
```diff
{diff_text}
```
"""

        rag_block = self._get_rag_examples(state)

        comment_type = getattr(state, "detected_comment_type", "")

        format_warning = ""
        if comment_type == "return":
            format_warning = (
                "CRITICAL: Output ONLY a single @return line. "
                "Do NOT add @param, @throws, or Javadoc block wrappers (/** ... */)."
            )
        elif comment_type == "param":
            format_warning = (
                "CRITICAL: Output ONLY a single @param line. "
                "Do NOT add @return, @throws, or Javadoc block wrappers (/** ... */)."
            )

        summary_rules = ""
        if comment_type == "summary":
            summary_rules = """
4. SUMMARY-SPECIFIC RULES (CRITICAL for summary comments):
   - First, identify the EXACT words that are factually wrong. Then replace ONLY those words.
   - Do NOT restructure the sentence or change the verb/subject.
   - If the original says "Unsubscribes the resource from this channel" and code uses "repo",
     the fix is "Unsubscribes the resource from this repo" — change ONE word, keep everything else.
   - If the original says "Creates elastic node as single member of a cluster" and only "Create/Creates" is wrong,
     change ONLY that word. Do NOT rewrite the rest of the sentence.
   - Do NOT infer new descriptions from the code. Only fix what the detection report says is wrong.
   - When in doubt, change LESS rather than MORE.
"""

        prompt = f"""The following code comment is INCONSISTENT with the current code.

[Original Comment]
{state.original_comment}

[Current Code]
{state.code_snippet}
{diff_block}
[Context]
- Interface: {state.interface_context}
- Intent: {state.intention_context}

[Why It Is Inconsistent]
{state.inconsistency_reason}

{rag_block}

=== RECTIFICATION RULES (you MUST follow ALL of these) ===

1. MINIMAL EDIT: Change ONLY the words/names that are factually wrong.
   - If a class name changed (e.g., JTextField → ZapTextField), replace ONLY that name.
   - If a return condition changed, update ONLY that condition.
   - Do NOT rephrase, rewrite, or expand the comment.
   - Do NOT add explanations, descriptions, or details that were not in the original.

2. PRESERVE STRUCTURE: Keep the exact same sentence structure and wording.
   - If original says "@return javax.swing.JTextField", the fix is "@return javax.swing.ZapTextField" — NOT a whole new sentence.
   - If original says "@return the value of X", keep "the value of" and only fix X.

3. FORMAT: {format_warning if format_warning else "Maintain the exact same comment format as the original."}
{summary_rules}
Output: ONLY the corrected comment text, nothing else.
"""
        try:
            response = self._call_llm(prompt, system_prompt)
            rectified = response.strip()
            # Strip Javadoc wrappers if LLM added them despite instructions
            if comment_type in ("return", "param") and rectified.startswith("/**"):
                import re
                tag = "@return" if comment_type == "return" else "@param"
                match = re.search(rf"({tag}\s+.*?)(?:\n\s*\*[\s/]|\n\s*\*/|$)", rectified, re.DOTALL)
                if match:
                    rectified = match.group(1).strip()
            state.rectified_comment = rectified
            state.log(f"[{self.name}] Comment rectified successfully.")
        except Exception as e:
            state.log(f"[{self.name}] 模型调用异常: {e}")
            state.rectified_comment = state.original_comment

        return state
