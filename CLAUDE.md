# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Multi-agent framework for detecting and rectifying code-comment inconsistencies, aligned with the ICSE 2025 C4RLLaMA benchmark. Uses a Generator-Reviewer paradigm: four specialized agents run in a pipeline orchestrated by `WorkflowOrchestrator`.

The task is to determine whether an `@param`, `@return`, or summary comment on a Java method is still consistent with the code after the code has been modified (Just-In-Time setting).

## Setup & Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Download NLTK data (required for evaluation metrics)
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('wordnet')"

# Create `.env` file with API keys before running:
#   ZHIPUAI_API_KEY, DEEPSEEK_API_KEY, OPENAI_API_KEY, GEMINI_API_KEY
```

```bash
# Single-sample test (uses hardcoded Python example in main.py)
python main.py --model glm-4-flash
python main.py --model deepseek-chat --use-diff --verbose

# Batch evaluation on the JIT dataset (subset)
python main_evaluate.py --model deepseek-chat --limit 100 --category Return
python main_evaluate.py --model glm-4-flash --limit 100 --detect-only

# Baseline: single LLM without prompt engineering (for ablation comparison)
python main_baseline.py --model glm-4-flash --category Return --limit 100
```

Build RAG retrieval indexes (pre-compute embeddings + LLM explanations for few-shot examples):
```bash
python retrieval/build_index.py --category Return --model glm-4-flash --batch-size 50
python retrieval/build_index.py --category Summary --model deepseek-chat --skip-explain
python retrieval/build_index.py --category Param --model glm-4-flash
```

Check explanation generation progress: `python check_progress.py`

## Architecture

### Agent Pipeline

```
Code + Comment → ContextParser → Detector → [if inconsistent] Rectifier ⇄ Reviewer (retry loop)
```

1. **ContextParser** (`agents/context_parser_agent.py`): Extracts method signature, parameters, return type via tree-sitter (Java), then falls back to Python `ast` or LLM JSON extraction. Produces `intention_context`, `interface_context`, `implementation_context` stored in `CodeCommentState`.

2. **Detector** (`agents/detector_agent.py`): Classifies comment as `param`/`return`/`summary` by keywords. Runs type-specific **rule checks** first (e.g., void method with @return content → INCONSISTENT; return type mismatch). If no hard rule triggers, sends to LLM with few-shot calibration examples (via RAG retrievers). The detector prompt uses claim-by-claim verification — the LLM must break the comment into individual claims and verify each against the code.

3. **Rectifier** (`agents/rectifier_agent.py`): Given the inconsistency reason, produces a corrected comment following a **minimal-edit principle** (change only wrong words, preserve structure). This directly optimizes for SARI metric. Supported by RAG retrieval of similar rectification examples.

4. **Reviewer** (`agents/reviewer_agent.py`): Checks rectified comment for factuality, completeness, format. Returns PASS or REJECT. Orchestrator retries up to `max_retries` times (default 2) on REJECT, feeding reviewer feedback back into the Rectifier.

### Key Modules

- **`core/state.py`**: `CodeCommentState` dataclass — the single state object passed through all agents. Fields for code, comment, parsed context, detection result, rectified comment, review result, and execution history.
- **`core/java_parser.py`**: Deterministic Java parsing via `tree-sitter-java`. Extracts method name, return type, parameters (with types), throws, return expressions, null return detection, empty collection return detection. Returns `full_signature` string.
- **`workflow/orchestrator.py`**: Creates all agents with their RAG retrievers, manages the pipeline and retry loop. `detect_only` mode skips rectification+review (only outputs detection metrics).
- **`evaluation/evaluator.py`**: Detection metrics (Accuracy, Precision, Recall, F1) treating INCONSISTENT as the positive class. Rectification metrics (xMatch, BLEU-4, GLEU, Meteor, SARI). Can write per-sample trace reports to markdown.
- **`retrieval/example_retriever.py`**: Hybrid BM25 + sentence-transformers (`all-MiniLM-L6-v2`) retrieval over labeled training examples. Category-specific retrievers (`summary_retriever`, `param_retriever`) for different comment types. `retrieve()` ensures mix of CONSISTENT/INCONSISTENT examples; `retrieve_rectification_examples()` returns only INCONSISTENT cases with ground-truth corrections.

### Data Format

Dataset (`data/eval_dataset.jsonl` after download): JSONL with fields `id`, `code_snippet`, `original_comment`, `old_code_snippet`, `label_consistent` (bool), `ground_truth_comment`. IDs are prefixed by category: `Param_*`, `Return_*`, `Summary_*`.

RAG training data lives in `dataset/just_in_time/{Return,Summary,Param}/` as `train.json` and `valid.json` with fields `old_comment_raw`, `new_code_raw`, `label` (0=consistent, 1=inconsistent), `new_comment_raw`.

### Models & API

`BaseAgent._do_api_call()` routes by model name prefix (`glm-` → ZhipuAI, `deepseek-` → OpenAI-compatible at api.deepseek.com, `gpt-`/`o1`/`o3` → OpenAI, `gemini-` → Google GenAI). All calls use `temperature=0.1`. Retry with exponential backoff on rate-limit/timeout errors.
