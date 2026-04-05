import json
import os
import re
from typing import List, Dict, Optional

from rank_bm25 import BM25Okapi
from core.java_parser import parse_java_method


_CAMEL_SPLIT = re.compile(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")
_NON_ALNUM = re.compile(r"[^a-zA-Z0-9_]")

_JAVA_STOPWORDS = frozenset({
    "public", "private", "protected", "static", "final", "void", "class",
    "interface", "extends", "implements", "import", "package", "new",
    "this", "super", "if", "else", "for", "while", "do", "switch", "case",
    "break", "continue", "try", "catch", "finally",
    "instanceof", "abstract", "synchronized", "volatile",
    "transient", "native", "strictfp", "assert", "enum", "default",
    "int", "long", "short", "byte", "float",
    "double", "char", "object",
    "the", "an", "is", "are", "of", "to", "in", "and", "or", "not",
    "that", "with", "for", "from", "by", "on", "at", "be", "as", "it",
})


def _tokenize(text: str) -> List[str]:
    """Split text into lowercase tokens with CamelCase handling."""
    parts = _NON_ALNUM.sub(" ", text).split()
    tokens = []
    for part in parts:
        sub_parts = _CAMEL_SPLIT.sub(" ", part).split()
        for sp in sub_parts:
            low = sp.lower()
            if len(low) >= 2 and low not in _JAVA_STOPWORDS:
                tokens.append(low)
    return tokens


def _smart_truncate(code: str, max_lines: int = 15) -> str:
    """Extract signature + return statements via tree-sitter; fall back to line truncation."""
    parsed = parse_java_method(code)
    if parsed and parsed.get("method_name"):
        parts = [parsed["full_signature"]]
        for expr in parsed.get("return_expressions", [])[:5]:
            parts.append(f"  return {expr};")
        return "\n".join(parts)

    lines = code.split("\n")
    if len(lines) <= max_lines:
        return code.strip()
    return "\n".join(lines[:max_lines]).strip() + "\n  // ... (truncated)"


class ExampleRetriever:
    """BM25-based retriever that finds similar labeled examples for dynamic few-shot."""

    def __init__(self, data_dir: Optional[str] = None):
        self._examples: List[Dict] = []
        self._bm25: Optional[BM25Okapi] = None
        self._consistent_indices: List[int] = []
        self._inconsistent_indices: List[int] = []
        self._data_dir = data_dir or self._default_data_dir()

    @staticmethod
    def _default_data_dir() -> str:
        here = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(here, "..", "dataset", "just_in_time", "Return")

    def _ensure_loaded(self):
        if self._bm25 is not None:
            return
        self._load_and_index()

    def _load_and_index(self):
        examples = []
        for fname in ("train.json", "valid.json"):
            fpath = os.path.join(self._data_dir, fname)
            if not os.path.exists(fpath):
                continue
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                is_inconsistent = item.get("label", 0) == 1
                examples.append({
                    "comment": item.get("old_comment_raw", ""),
                    "code": item.get("new_code_raw", ""),
                    "is_inconsistent": is_inconsistent,
                    "ground_truth": item.get("new_comment_raw", "") if is_inconsistent else "",
                })

        self._examples = examples

        corpus = []
        for i, ex in enumerate(examples):
            tokens = _tokenize(ex["comment"] + " " + ex["code"])
            corpus.append(tokens)
            if ex["is_inconsistent"]:
                self._inconsistent_indices.append(i)
            else:
                self._consistent_indices.append(i)

        if corpus:
            self._bm25 = BM25Okapi(corpus)

    def retrieve(
        self,
        comment: str,
        code: str,
        top_k: int = 3,
        ensure_mix: bool = True,
    ) -> List[Dict]:
        """Return up to top_k similar labeled examples.

        If ensure_mix is True and top-k results are all the same label,
        swap the last one with the best-scoring example of the opposite label.
        """
        self._ensure_loaded()
        if not self._bm25 or not self._examples:
            return []

        query_tokens = _tokenize(comment + " " + code)
        scores = self._bm25.get_scores(query_tokens)

        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        results_idx = ranked[:top_k]

        if ensure_mix and len(results_idx) >= 2:
            labels = [self._examples[i]["is_inconsistent"] for i in results_idx]
            all_same = len(set(labels)) == 1
            if all_same:
                current_label = labels[0]
                opposite_pool = (
                    self._consistent_indices if current_label else self._inconsistent_indices
                )
                for idx in ranked:
                    if idx in opposite_pool and idx not in results_idx:
                        results_idx[-1] = idx
                        break

        results = []
        for idx in results_idx:
            ex = self._examples[idx]
            results.append({
                "comment": ex["comment"],
                "code_truncated": _smart_truncate(ex["code"]),
                "label": "INCONSISTENT" if ex["is_inconsistent"] else "CONSISTENT",
                "ground_truth": ex["ground_truth"],
            })
        return results

    def format_examples(self, examples: List[Dict]) -> str:
        """Format retrieved examples into a prompt-ready string."""
        if not examples:
            return ""
        parts = ["Retrieved Similar Cases for Reference:"]
        for i, ex in enumerate(examples, 1):
            parts.append(f"--- Case {i} ({ex['label']}) ---")
            parts.append(f"Comment: {ex['comment']}")
            parts.append(f"Code (truncated):\n{ex['code_truncated']}")
            if ex["label"] == "INCONSISTENT" and ex["ground_truth"]:
                parts.append(f"Correct comment should be: {ex['ground_truth']}")
            parts.append("")
        return "\n".join(parts)
