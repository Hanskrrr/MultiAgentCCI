# MultiAgentCCI

A lightweight research prototype for just-in-time code-comment inconsistency detection and rectification with a multi-agent workflow.

This repository is intentionally kept focused on the core implementation only:
- context parsing
- inconsistency detection
- comment rectification
- BM25/hybrid example retrieval
- workflow orchestration
- evaluation scripts

Large datasets, experiment logs, reports, references, local prompts, and thesis-writing artifacts should stay out of version control.

## Core workflow

The system uses three specialized agents:
- `ContextParserAgent`: extracts structured signature/context information from code, preferring Tree-sitter and falling back to LLM parsing when needed.
- `DetectorAgent`: decides whether the original comment is consistent with the current code using rule signals, diff-aware prompts, and type-specific guidance.
- `RectifierAgent`: rewrites inconsistent comments with a minimal-edit strategy and retrieved correction examples.

The review loop is implemented by reusing `DetectorAgent` to re-check the rectified comment, rather than adding a separate reviewer module.

## Repository layout

```text
agents/
  base_agent.py
  context_parser_agent.py
  detector_agent.py
  rectifier_agent.py
core/
  java_parser.py
  state.py
dataset/
  download_dataset.py
  preprocessor.py
evaluation/
  evaluator.py
retrieval/
  build_index.py
  example_retriever.py
workflow/
  orchestrator.py
main.py
main_baseline.py
main_evaluate.py
requirements.txt
```

## Environment

Recommended: Python 3.10+ in a virtual environment.

Install dependencies:

```bash
pip install -r requirements.txt
```

Download NLTK resources once:

```bash
python3 -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('wordnet')"
```

Set API keys in `.env`:

```bash
ZHIPUAI_API_KEY="your-key"
DEEPSEEK_API_KEY="your-key"
```

## Dataset preparation

The code expects the processed evaluation file at `data/eval_dataset.jsonl` and category splits under `dataset/just_in_time/`.

If needed, prepare the dataset with:

```bash
python3 dataset/download_dataset.py
```

## Running

Single-sample run:

```bash
python3 main.py --model glm-4-plus --parser treesitter --use-diff
```

Baseline run:

```bash
python3 main_baseline.py --model glm-4-plus --category Param
python3 main_baseline.py --model glm-4-plus --category Return
python3 main_baseline.py --model glm-4-plus --category Summary
```

## Final evaluation commands

The thesis results should be reproduced with explicit diff-aware evaluation.

Main system:

```bash
python3 main_evaluate.py --model glm-4-plus --category Param --parser treesitter --use-diff --max-retries 2 --trace-rectify
python3 main_evaluate.py --model glm-4-plus --category Return --parser treesitter --use-diff --max-retries 2 --trace-rectify
python3 main_evaluate.py --model glm-4-plus --category Summary --parser treesitter --use-diff --max-retries 2 --trace-rectify
```

Baseline:

```bash
python3 main_baseline.py --model glm-4-plus --category Param
python3 main_baseline.py --model glm-4-plus --category Return
python3 main_baseline.py --model glm-4-plus --category Summary
```

Notes:
- `--use-diff` is required if you want the detector and rectifier prompts to actually consume old/new code change information.
- `--parser treesitter` matches the main implementation described in the thesis.
- `--max-retries 2` matches the detector re-review loop used in the later experiments.

## Cleaning an already polluted Git index

If files are already tracked, adding them to `.gitignore` is not enough. You must remove them from the Git index once:

```bash
git rm -r --cached .claude analysis refs data retrieval/cache dataset/just_in_time
git rm --cached *.log *.html Data.7z =0.2.2 CLAUDE.md
```

Then commit:

```bash
git add .gitignore README.md
git commit -m "chore: keep repo focused on core implementation"
```

If those files were already pushed before, this commit will stop tracking them going forward, but it will not erase them from old commits. To fully purge them from repository history, use a history-rewrite tool such as `git filter-repo` or BFG on the branch you plan to publish.
