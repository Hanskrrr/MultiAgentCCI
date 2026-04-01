import os
import json
import ast
from .base_agent import BaseAgent
from core.state import CodeCommentState


class ContextParserAgent(BaseAgent):
    """
    上下文解析智能体：
    负责将纯文本代码块解析为结构化的AST信息，
    并为后续智能体提供“意图层”、“接口层”和“实现层”的上下文信息。
    """

    def __init__(self, model_name: str = "glm-4-flash"):
        super().__init__(name="ContextParserAgent", model_name=model_name)

    def process(self, state: CodeCommentState) -> CodeCommentState:
        state.log(f"[{self.name}] Starting code analysis and semantic extraction...")

        # 1. Fallback AST parsing (only works for Python)
        try:
            tree = ast.parse(state.code_snippet)
            functions = [
                node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
            ]
            if functions:
                func = functions[0]
                args = [arg.arg for arg in func.args.args]
                returns_node = getattr(func, "returns", None)
                returns = "None" if returns_node is None else ast.unparse(returns_node)
                state.ast_context = {
                    "type": "function",
                    "name": func.name,
                    "arguments": args,
                    "returns": returns,
                }
                state.log(f"[{self.name}] Python AST extraction successful.")
        except Exception:
            state.log(
                f"[{self.name}] Non-Python code detected or AST failure. Relying on LLM for structure."
            )

        # 2. Use LLM to extract multi-dimensional context
        system_prompt = "You are an expert source code analyzer. Provide analysis results in pure JSON format."
        prompt = f"""
Analyze the following code snippet (Java or Python). 
Extract the function signature and core semantics into the following structure.

Return strictly in JSON format:
{{
    "signature": {{
        "name": "function name",
        "parameters": [
            {{"name": "p1", "type": "type1"}},
            {{"name": "p2", "type": "type2"}}
        ],
        "return_type": "type"
    }},
    "intention": "Briefly describe the primary purpose of this code.",
    "implementation": "Describe the core logic flow or business steps."
}}

[Code Snippet]
{state.code_snippet}
"""
        try:
            response_text = self._call_llm(prompt, system_prompt)
            # Clean markdown
            response_text = (
                response_text.replace("```json", "").replace("```", "").strip()
            )
            result_json = json.loads(response_text)

            sig = result_json.get("signature", {})
            params_list = sig.get("parameters", [])
            params_str = ", ".join(
                [
                    f"{p.get('type', '')} {p.get('name', '')}".strip()
                    for p in params_list
                ]
            )

            state.interface_context = f"Full Signature: {sig.get('name')}({params_str}) -> {sig.get('return_type')}\nParameters Details: {json.dumps(params_list)}"
            state.intention_context = result_json.get("intention", "")
            state.implementation_context = result_json.get("implementation", "")

            state.log(f"[{self.name}] LLM context parsing completed.")

        except Exception as e:
            state.log(f"[{self.name}] LLM parsing exception: {e}")
            state.intention_context = "Failed to parse intention"
            state.interface_context = "Failed to parse interface"
            state.implementation_context = "Failed to parse implementation"

        return state
