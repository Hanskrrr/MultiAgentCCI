"""Deterministic Java code structure extraction using tree-sitter."""
import re
from typing import Dict, List, Optional

try:
    import tree_sitter_java as tsjava
    from tree_sitter import Language, Parser

    _JAVA_LANGUAGE = Language(tsjava.language())
    TREE_SITTER_AVAILABLE = True
except (ImportError, Exception):
    _JAVA_LANGUAGE = None
    TREE_SITTER_AVAILABLE = False


def _make_parser() -> "Parser":
    return Parser(_JAVA_LANGUAGE)


def _text(node, source: bytes) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8", errors="replace")


def _find_all(node, type_name: str) -> List:
    """Recursively find all nodes of a given type."""
    hits: list = []
    if node.type == type_name:
        hits.append(node)
    for child in node.children:
        hits.extend(_find_all(child, type_name))
    return hits


def _collect_returns_in_scope(node, source: bytes) -> List[str]:
    """Collect return expressions without descending into nested methods / lambdas / classes."""
    results: List[str] = []
    for child in node.children:
        if child.type == "return_statement":
            if child.named_child_count > 0:
                results.append(_text(child.named_children[0], source))
            else:
                results.append("")
        elif child.type in (
            "method_declaration",
            "constructor_declaration",
            "lambda_expression",
            "class_declaration",
            "enum_declaration",
            "interface_declaration",
            "record_declaration",
        ):
            continue
        else:
            results.extend(_collect_returns_in_scope(child, source))
    return results


def _parse_parameters(params_node, source: bytes) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []
    for child in params_node.children:
        if child.type == "formal_parameter":
            p_type = child.child_by_field_name("type")
            p_name = child.child_by_field_name("name")
            dims = child.child_by_field_name("dimensions")
            if p_type and p_name:
                type_str = _text(p_type, source)
                if dims:
                    type_str += _text(dims, source)
                result.append({"name": _text(p_name, source), "type": type_str})
        elif child.type == "spread_parameter":
            p_type = child.child_by_field_name("type")
            p_name = child.child_by_field_name("name")
            if p_type and p_name:
                result.append(
                    {"name": _text(p_name, source), "type": _text(p_type, source) + "..."}
                )
    return result


def _parse_throws(method_node, source: bytes) -> List[str]:
    for child in method_node.children:
        if child.type == "throws":
            return [_text(nc, source) for nc in child.named_children]
    return []


_EMPTY_PATTERNS = re.compile(
    r"Collections\.empty|Optional\.empty|List\.of\(\)|Set\.of\(\)|Map\.of\(\)",
    re.IGNORECASE,
)


def parse_java_method(code: str) -> Optional[Dict]:
    """Parse Java code and extract the first method's structural information.

    Returns dict with keys:
        method_name, return_type, parameters, throws,
        return_expressions, has_null_return, has_empty_return,
        full_signature
    Or None if tree-sitter is unavailable or no method found.
    """
    if not TREE_SITTER_AVAILABLE:
        return None

    parser = _make_parser()
    source = code.encode("utf-8")
    tree = parser.parse(source)

    methods = _find_all(tree.root_node, "method_declaration")

    if not methods:
        wrapped = f"class _W {{\n{code}\n}}"
        source = wrapped.encode("utf-8")
        tree = parser.parse(source)
        methods = _find_all(tree.root_node, "method_declaration")

    if not methods:
        return None

    method = methods[0]

    type_node = method.child_by_field_name("type")
    name_node = method.child_by_field_name("name")
    params_node = method.child_by_field_name("parameters")
    body_node = method.child_by_field_name("body")

    return_type = _text(type_node, source) if type_node else "void"
    method_name = _text(name_node, source) if name_node else ""
    parameters = _parse_parameters(params_node, source) if params_node else []
    throws = _parse_throws(method, source)

    return_expressions: List[str] = []
    has_null_return = False
    has_empty_return = False

    if body_node:
        return_expressions = _collect_returns_in_scope(body_node, source)
        for expr in return_expressions:
            stripped = expr.strip()
            # Only flag "return null;" — not "return x != null;" or "return x == null ? a : b"
            if stripped == "null":
                has_null_return = True
            if _EMPTY_PATTERNS.search(stripped):
                has_empty_return = True
        if not has_null_return:
            for ret_node in _find_all(body_node, "return_statement"):
                # Only flag if the DIRECT child of return_statement is null_literal
                # (not null_literal buried inside a binary_expression or ternary)
                for child in ret_node.named_children:
                    if child.type == "null_literal":
                        has_null_return = True
                        break
                if has_null_return:
                    break

    params_str = ", ".join(f"{p['type']} {p['name']}" for p in parameters)
    throws_str = f" throws {', '.join(throws)}" if throws else ""
    full_signature = f"{method_name}({params_str}) -> {return_type}{throws_str}"

    return {
        "method_name": method_name,
        "return_type": return_type,
        "parameters": parameters,
        "throws": throws,
        "return_expressions": return_expressions,
        "has_null_return": has_null_return,
        "has_empty_return": has_empty_return,
        "full_signature": full_signature,
    }
