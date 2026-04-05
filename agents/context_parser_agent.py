import re
import json
import ast
from .base_agent import BaseAgent
from core.state import CodeCommentState
from core.java_parser import parse_java_method, TREE_SITTER_AVAILABLE


class ContextParserAgent(BaseAgent):
    """
    上下文解析智能体：
    负责将纯文本代码块解析为结构化的AST信息，
    并为后续智能体提供"意图层"、"接口层"和"实现层"的上下文信息。
    """

    def __init__(self, model_name: str = "glm-4-flash", parser_mode: str = "treesitter"):
        super().__init__(name="ContextParserAgent", model_name=model_name)
        self.parser_mode = parser_mode

    @staticmethod
    def _method_name_to_intent(name: str) -> str:
        """Convert camelCase method name to human-readable intent."""
        words = re.sub(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", " ", name)
        return words.strip()

    def _try_treesitter(self, state: CodeCommentState) -> bool:
        """Attempt tree-sitter Java parse. Returns True on success."""
        if not TREE_SITTER_AVAILABLE:
            return False

        parsed = parse_java_method(state.code_snippet)
        if not parsed or not parsed.get("method_name"):
            return False

        state.ast_context = parsed

        params_json = json.dumps(parsed["parameters"])
        state.interface_context = (
            f"Full Signature: {parsed['full_signature']}\n"
            f"Parameters Details: {params_json}"
        )

        intent = self._method_name_to_intent(parsed["method_name"])
        ret_count = len(parsed.get("return_expressions", []))
        state.intention_context = f"Method '{parsed['method_name']}' ({intent})"
        state.implementation_context = (
            f"Return paths: {ret_count}"
            + (f", throws: {', '.join(parsed['throws'])}" if parsed.get("throws") else "")
        )

        state.log(
            f"[{self.name}] Tree-sitter Java parsing successful: "
            f"{parsed['full_signature'][:80]}"
        )
        return True

    def _try_python_ast(self, state: CodeCommentState) -> bool:
        """Attempt Python AST parse. Returns True on success."""
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
                params_list = [{"name": a, "type": ""} for a in args]
                params_str = ", ".join(args)
                state.interface_context = (
                    f"Full Signature: {func.name}({params_str}) -> {returns}\n"
                    f"Parameters Details: {json.dumps(params_list)}"
                )
                intent = self._method_name_to_intent(func.name)
                state.intention_context = f"Function '{func.name}' ({intent})"
                state.implementation_context = ""
                state.log(f"[{self.name}] Python AST extraction successful.")
                return True
        except Exception:
            pass
        return False

    def _fallback_llm(self, state: CodeCommentState):
        """Fall back to LLM for structure extraction."""
        system_prompt = (
            "You are an expert source code analyzer. "
            "Provide analysis results in pure JSON format."
        )
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
            response_text = (
                response_text.replace("```json", "").replace("```", "").strip()
            )
            result_json = json.loads(response_text)

            sig = result_json.get("signature", {})
            params_list = sig.get("parameters", [])
            params_str = ", ".join(
                f"{p.get('type', '')} {p.get('name', '')}".strip()
                for p in params_list
            )

            state.interface_context = (
                f"Full Signature: {sig.get('name')}({params_str}) -> {sig.get('return_type')}\n"
                f"Parameters Details: {json.dumps(params_list)}"
            )
            state.intention_context = result_json.get("intention", "")
            state.implementation_context = result_json.get("implementation", "")
            state.log(f"[{self.name}] LLM context parsing completed.")

        except Exception as e:
            state.log(f"[{self.name}] LLM parsing exception: {e}")
            state.intention_context = "Failed to parse intention"
            state.interface_context = "Failed to parse interface"
            state.implementation_context = "Failed to parse implementation"

    def process(self, state: CodeCommentState) -> CodeCommentState:
        state.log(f"[{self.name}] Starting code analysis (mode={self.parser_mode})...")

        if self.parser_mode == "treesitter":
            if self._try_treesitter(state):
                return state
            if self._try_python_ast(state):
                return state
            state.log(f"[{self.name}] Deterministic parsing failed. Falling back to LLM.")

        self._fallback_llm(state)
        return state
