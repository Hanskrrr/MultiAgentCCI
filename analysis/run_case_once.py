"""
run_case_once.py — single-sample tracer with deep instrumentation.

Captures every intermediate artifact:
  - ContextParser output (interface / intention / implementation)
  - Retrieved few-shot examples text (as injected into prompt)
  - Full prompt sent to LLM
  - Raw LLM response (the untruncated reasoning)
  - Parsed conclusion + rule signals / hard-fails
  - Agent history log

Outputs a single JSON object to stdout (last line) so the batch driver
can parse it with json.loads().
"""
import argparse
import json
import os

# ── CLI ────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser()
parser.add_argument('--id', required=True)
parser.add_argument('--model', default='glm-4-flash')
parser.add_argument('--use-diff', action='store_true')
args = parser.parse_args()

# ── load raw item ──────────────────────────────────────────────────────────
item = None
with open('data/eval_dataset.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        obj = json.loads(line)
        if obj.get('id') == args.id:
            item = obj
            break

if item is None:
    print(json.dumps({'id': args.id, 'error': 'not_found'}, ensure_ascii=False))
    raise SystemExit(0)

# ── instrumentation stores ─────────────────────────────────────────────────
_captured = {
    'fewshot_text': '',     # text injected into prompt as few-shot examples
    'full_prompt': '',      # full prompt string sent to LLM
    'llm_raw_response': '', # raw text returned by LLM
}

# ── import project modules ─────────────────────────────────────────────────
from core.state import CodeCommentState
from agents.context_parser_agent import ContextParserAgent
from agents.detector_agent import DetectorAgent
from retrieval.example_retriever import ExampleRetriever
from workflow.orchestrator import WorkflowOrchestrator

# ── monkey-patch DetectorAgent to capture intermediates ───────────────────
_orig_get_return_examples = DetectorAgent._get_return_examples
def _patched_get_return_examples(self, state):
    text = _orig_get_return_examples(self, state)
    _captured['fewshot_text'] = text
    return text
DetectorAgent._get_return_examples = _patched_get_return_examples

_orig_build_prompt = DetectorAgent._build_prompt
def _patched_build_prompt(self, state, comment_type, signals):
    prompt = _orig_build_prompt(self, state, comment_type, signals)
    _captured['full_prompt'] = prompt
    return prompt
DetectorAgent._build_prompt = _patched_build_prompt

_orig_do_api_call = None
from agents.base_agent import BaseAgent
_orig_do_api_call = BaseAgent._do_api_call
def _patched_do_api_call(self, messages):
    result = _orig_do_api_call(self, messages)
    _captured['llm_raw_response'] = result
    return result
BaseAgent._do_api_call = _patched_do_api_call

# ── run orchestrator ───────────────────────────────────────────────────────
orc = WorkflowOrchestrator(
    model_name=args.model,
    max_retries=1,
    detect_only=True,
    verbose=True,
    parser_mode='treesitter',
    use_diff=args.use_diff,
)
state = orc.run(
    code_snippet=item['code_snippet'],
    original_comment=item['original_comment'],
    old_code_snippet=item.get('old_code_snippet', ''),
)

# ── assemble output ────────────────────────────────────────────────────────
out = {
    'id': args.id,
    'label_consistent': item.get('label_consistent'),
    'original_comment': item.get('original_comment', ''),
    'ground_truth_comment': item.get('ground_truth_comment', ''),
    'code_snippet': item.get('code_snippet', ''),
    'old_code_snippet': item.get('old_code_snippet', ''),
    # parser
    'interface_context': state.interface_context,
    'intention_context': state.intention_context,
    'implementation_context': state.implementation_context,
    # detector
    'is_consistent': state.is_consistent,
    'detection_method': state.detection_method,
    'detected_comment_type': state.detected_comment_type,
    'inconsistency_reason': state.inconsistency_reason,
    'rule_signals': state.rule_signals,
    'rule_hard_fails': state.rule_hard_fails,
    # captured instrumentation
    'fewshot_injected': _captured['fewshot_text'],
    'full_prompt': _captured['full_prompt'],
    'llm_raw_response': _captured['llm_raw_response'],
    # history
    'history': state.history,
}
print(json.dumps(out, ensure_ascii=False))
