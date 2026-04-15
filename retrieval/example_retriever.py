"""Hybrid retriever: BM25 + sentence-transformers embeddings.

Retrieval pipeline:
  1. BM25 lexical score (always available)
  2. Cosine similarity from pre-built embeddings.npy (optional)
  3. Weighted fusion: alpha * bm25_norm + (1 - alpha) * cos_score
  4. Optional: inject pre-computed LLM explanations from explanations.json

If embeddings.npy does not exist, falls back to pure BM25 automatically.
If explanations.json does not exist, the "explanation" field is an empty string.
"""
import json
import os
import re
import warnings
from typing import List, Dict, Optional

# Force offline mode before any HuggingFace library is imported
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import numpy as np
from rank_bm25 import BM25Okapi

from core.java_parser import parse_java_method


# ---------------------------------------------------------------------------
# Tokenisation helpers (BM25)
# ---------------------------------------------------------------------------

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
    parts = _NON_ALNUM.sub(" ", text).split()
    tokens = []
    for part in parts:
        for sp in _CAMEL_SPLIT.sub(" ", part).split():
            low = sp.lower()
            if len(low) >= 2 and low not in _JAVA_STOPWORDS:
                tokens.append(low)
    return tokens


# ---------------------------------------------------------------------------
# Code display helper
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# ExampleRetriever
# ---------------------------------------------------------------------------

_HERE = os.path.dirname(os.path.abspath(__file__))
_CACHE_DIR = os.path.join(_HERE, "cache")
_EMBED_PATH = os.path.join(_CACHE_DIR, "embeddings.npy")
_EXPLAIN_PATH = os.path.join(_CACHE_DIR, "explanations.json")
_EMBED_MODEL_NAME = "all-MiniLM-L6-v2"


class ExampleRetriever:
    """BM25 + optional embedding hybrid retriever with LLM explanation injection."""

    def __init__(
        self,
        data_dir: Optional[str] = None,
        alpha: float = 0.5,
    ):
        self._examples: List[Dict] = []
        self._bm25: Optional[BM25Okapi] = None
        self._consistent_indices: List[int] = []
        self._inconsistent_indices: List[int] = []
        self._data_dir = data_dir or self._default_data_dir()
        self.alpha = alpha

        # Loaded lazily
        self._embeddings: Optional[np.ndarray] = None
        self._embed_model = None
        self._explanations: Dict[str, str] = {}

    @staticmethod
    def _default_data_dir() -> str:
        here = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(here, "..", "dataset", "just_in_time", "Return")

    # ------------------------------------------------------------------
    # Lazy initialisation
    # ------------------------------------------------------------------

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

        # Try to load pre-built embedding cache
        if os.path.exists(_EMBED_PATH):
            try:
                embs = np.load(_EMBED_PATH)
                if embs.shape[0] == len(examples):
                    self._embeddings = embs
                    self._load_embed_model()
                else:
                    print(
                        f"[ExampleRetriever] Warning: embeddings.npy size mismatch "
                        f"({embs.shape[0]} vs {len(examples)}). Using BM25 only."
                    )
            except Exception as e:
                print(f"[ExampleRetriever] Warning: failed to load embeddings: {e}")

        # Try to load pre-built explanations
        if os.path.exists(_EXPLAIN_PATH):
            try:
                with open(_EXPLAIN_PATH, "r", encoding="utf-8") as f:
                    self._explanations = json.load(f)
            except Exception as e:
                print(f"[ExampleRetriever] Warning: failed to load explanations: {e}")

    def _load_embed_model(self):
        try:
            # Suppress the noisy CUDA driver version warning from PyTorch
            warnings.filterwarnings("ignore", message="CUDA initialization", category=UserWarning)
            from sentence_transformers import SentenceTransformer
            # local_files_only=True prevents any network requests even if env vars are ignored
            self._embed_model = SentenceTransformer(_EMBED_MODEL_NAME, local_files_only=True)
        except Exception as e:
            print(f"[ExampleRetriever] Warning: could not load embedding model: {e}")
            self._embed_model = None
            self._embeddings = None

    # ------------------------------------------------------------------
    # Hybrid scoring
    # ------------------------------------------------------------------

    def _hybrid_scores(self, comment: str, code: str) -> np.ndarray:
        """Return hybrid score array of length len(self._examples)."""
        query_tokens = _tokenize(comment + " " + code)
        bm25_raw = np.array(self._bm25.get_scores(query_tokens), dtype="float32")

        # Normalise BM25 to [0, 1]
        b_min, b_max = bm25_raw.min(), bm25_raw.max()
        bm25_norm = (bm25_raw - b_min) / (b_max - b_min + 1e-9)

        if self._embeddings is not None and self._embed_model is not None:
            query_emb = self._embed_model.encode(
                [comment + " " + code[:500]], normalize_embeddings=True
            )  # shape [1, D]
            cos_scores = (self._embeddings @ query_emb.T).squeeze(axis=1)  # shape [N]
            cos_scores = np.clip(cos_scores, 0, 1)
            return self.alpha * bm25_norm + (1.0 - self.alpha) * cos_scores

        return bm25_norm

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def retrieve(
        self,
        comment: str,
        code: str,
        top_k: int = 3,
        ensure_mix: bool = True,
    ) -> List[Dict]:
        """Return up to top_k similar labeled examples with optional explanations."""
        self._ensure_loaded()
        if not self._bm25 or not self._examples:
            return []

        scores = self._hybrid_scores(comment, code)
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        results_idx = list(ranked[:top_k])

        if ensure_mix and len(results_idx) >= 2:
            labels = [self._examples[i]["is_inconsistent"] for i in results_idx]
            if len(set(labels)) == 1:
                current_label = labels[0]
                opposite_pool = set(
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
                "explanation": self._explanations.get(str(idx), ""),
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
            parts.append(f"Code:\n{ex['code_truncated']}")
            if ex["label"] == "INCONSISTENT" and ex["ground_truth"]:
                parts.append(f"Correct comment: {ex['ground_truth']}")
            if ex.get("explanation"):
                parts.append(f"Why: {ex['explanation']}")
            parts.append("")
        return "\n".join(parts)

    @property
    def using_hybrid(self) -> bool:
        return self._embeddings is not None and self._embed_model is not None
