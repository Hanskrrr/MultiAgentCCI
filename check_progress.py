"""Quick progress check for explanations generation."""
import json, os

EXPLAIN_PATH = os.path.join(os.path.dirname(__file__), "retrieval", "cache", "explanations.json")

if not os.path.exists(EXPLAIN_PATH):
    print("No explanations.json found yet.")
else:
    with open(EXPLAIN_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    total_corpus = 17740
    done = len(data)
    pct = done / total_corpus * 100
    print(f"Progress: {done}/{total_corpus} ({pct:.1f}%)")
    if done > 0:
        sample_keys = sorted(data.keys(), key=int)[:3]
        print("\nSample explanations:")
        for k in sample_keys:
            print(f"  [{k}] {data[k]}")
