"""Offline pre-computation script for hybrid retrieval.

Generates two cache files under retrieval/cache/:
  - embeddings.npy      : shape [N, 384], sentence-transformers embeddings
  - explanations.json   : {str(index): "one-sentence explanation"}

Usage examples:
  # Step 1: build embedding index only (fast, ~2-3 min for 17740 samples)
  python retrieval/build_index.py --skip-explain

  # Step 2: generate LLM explanations (slow, supports resume)
  python retrieval/build_index.py --model glm-4-flash --explain-only --batch-size 50

  # Both steps in one run
  python retrieval/build_index.py --model glm-4-flash --batch-size 50

  # Test with a small subset first
  python retrieval/build_index.py --model glm-4-flash --limit 200
"""
import argparse
import json
import os
import sys
import time

# Use HuggingFace mirror for users in China; force offline to use local cache
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(HERE, "..")
sys.path.insert(0, PROJECT_ROOT)

CACHE_DIR = os.path.join(HERE, "cache")
DATA_DIR = os.path.join(PROJECT_ROOT, "dataset", "just_in_time", "Return")
EMBED_PATH = os.path.join(CACHE_DIR, "embeddings.npy")
EXPLAIN_PATH = os.path.join(CACHE_DIR, "explanations.json")

EMBED_MODEL_NAME = "all-MiniLM-L6-v2"


def load_corpus(limit: int = 0):
    examples = []
    for fname in ("train.json", "valid.json"):
        fpath = os.path.join(DATA_DIR, fname)
        if not os.path.exists(fpath):
            print(f"[!] Not found: {fpath}")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            examples.append({
                "comment": item.get("old_comment_raw", ""),
                "code": item.get("new_code_raw", ""),
                "is_inconsistent": item.get("label", 0) == 1,
                "ground_truth": item.get("new_comment_raw", "") if item.get("label", 0) == 1 else "",
            })
    if limit > 0:
        examples = examples[:limit]
    return examples


def build_embeddings(examples, batch_size: int = 256):
    from sentence_transformers import SentenceTransformer

    print(f"[*] Loading embedding model: {EMBED_MODEL_NAME}")
    model = SentenceTransformer(EMBED_MODEL_NAME)

    texts = [ex["comment"] + " " + ex["code"][:500] for ex in examples]
    total = len(texts)
    print(f"[*] Encoding {total} samples in batches of {batch_size}...")

    all_embeddings = []
    for start in range(0, total, batch_size):
        batch = texts[start : start + batch_size]
        embs = model.encode(batch, show_progress_bar=False, normalize_embeddings=True)
        all_embeddings.append(embs)
        done = min(start + batch_size, total)
        print(f"    [{done}/{total}] encoded", end="\r", flush=True)

    print()
    embeddings = np.vstack(all_embeddings).astype("float32")
    os.makedirs(CACHE_DIR, exist_ok=True)
    np.save(EMBED_PATH, embeddings)
    print(f"[+] Saved embeddings: {EMBED_PATH}  shape={embeddings.shape}")
    return embeddings


def _call_llm_for_explanation(item: dict, idx: int, model_name: str) -> str:
    """Call LLM once to get a one-sentence explanation for why this example has its label."""
    from agents.base_agent import BaseAgent

    class _TmpAgent(BaseAgent):
        def __init__(self, m):
            super().__init__("ExplainAgent", m)

        def process(self, state):
            pass

    agent = _TmpAgent(model_name)

    label = "INCONSISTENT" if item["is_inconsistent"] else "CONSISTENT"
    gt_line = ""
    if item["is_inconsistent"] and item["ground_truth"]:
        gt_line = f"Correct comment: {item['ground_truth']}\n"

    from core.java_parser import parse_java_method
    parsed = parse_java_method(item["code"])
    sig_line = ""
    if parsed and parsed.get("full_signature"):
        sig_line = f"Code signature: {parsed['full_signature']}\n"

    prompt = (
        f"Given this @return comment and code pair labeled as {label}:\n"
        f"Comment: {item['comment']}\n"
        f"{gt_line}"
        f"{sig_line}"
        f"\nIn one concise sentence (max 25 words), explain why this pair is {label}."
        f" Do not repeat the label word. Start directly with the reason."
    )
    system = "You are a code documentation expert. Reply with exactly one sentence."
    try:
        response = agent._call_llm(prompt, system)
        return response.strip().split("\n")[0][:200]
    except Exception as e:
        return f"[explain failed: {e}]"


def build_explanations(examples, model_name: str, batch_size: int = 50):
    os.makedirs(CACHE_DIR, exist_ok=True)

    existing: dict = {}
    if os.path.exists(EXPLAIN_PATH):
        with open(EXPLAIN_PATH, "r", encoding="utf-8") as f:
            existing = json.load(f)
        print(f"[*] Resuming: {len(existing)} explanations already cached.")

    total = len(examples)
    saved = 0

    for idx, item in enumerate(examples):
        key = str(idx)
        if key in existing:
            continue

        explanation = _call_llm_for_explanation(item, idx, model_name)
        existing[key] = explanation
        saved += 1

        # Small per-call delay to respect API rate limits
        time.sleep(0.3)

        if saved % batch_size == 0:
            with open(EXPLAIN_PATH, "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
            pct = (idx + 1) / total * 100
            print(f"    [{idx+1}/{total}] {pct:.1f}%  saved batch (total cached: {len(existing)})", flush=True)
            time.sleep(1.0)

    with open(EXPLAIN_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    print(f"[+] Saved explanations: {EXPLAIN_PATH}  ({len(existing)} entries)")


def main():
    parser = argparse.ArgumentParser(description="Build hybrid retrieval index")
    parser.add_argument("--model", type=str, default="glm-4-flash",
                        help="LLM model name for explanation generation")
    parser.add_argument("--limit", type=int, default=0,
                        help="Only process first N examples (0 = all)")
    parser.add_argument("--batch-size", type=int, default=50,
                        help="Save checkpoint every N explanations")
    parser.add_argument("--embed-batch-size", type=int, default=256,
                        help="Encoding batch size for sentence-transformers")
    parser.add_argument("--skip-explain", action="store_true",
                        help="Skip LLM explanation generation")
    parser.add_argument("--explain-only", action="store_true",
                        help="Skip embedding generation, only build explanations")
    args = parser.parse_args()

    print("[*] Loading corpus...")
    examples = load_corpus(limit=args.limit)
    print(f"[*] Corpus size: {len(examples)} examples")

    if not args.explain_only:
        if os.path.exists(EMBED_PATH):
            existing = np.load(EMBED_PATH)
            if existing.shape[0] == len(examples):
                print(f"[*] Embedding cache already exists and matches corpus size. Skipping.")
            else:
                print(f"[!] Embedding cache size mismatch ({existing.shape[0]} vs {len(examples)}). Rebuilding.")
                build_embeddings(examples, batch_size=args.embed_batch_size)
        else:
            build_embeddings(examples, batch_size=args.embed_batch_size)

    if not args.skip_explain:
        print(f"\n[*] Generating LLM explanations using model: {args.model}")
        build_explanations(examples, model_name=args.model, batch_size=args.batch_size)
    else:
        print("[*] Skipping LLM explanation generation (--skip-explain).")

    print("\n[+] Done.")


if __name__ == "__main__":
    main()
