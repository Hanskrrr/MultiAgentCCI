import argparse
import json
import os
from workflow.orchestrator import WorkflowOrchestrator

parser = argparse.ArgumentParser()
parser.add_argument('--id', required=True)
parser.add_argument('--model', default='glm-4-flash')
args = parser.parse_args()

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

orc = WorkflowOrchestrator(model_name=args.model, max_retries=1, detect_only=True, verbose=True, parser_mode='treesitter')
state = orc.run(code_snippet=item['code_snippet'], original_comment=item['original_comment'])

out = {
    'id': args.id,
    'label_consistent': item.get('label_consistent'),
    'original_comment': item.get('original_comment',''),
    'ground_truth_comment': item.get('ground_truth_comment',''),
    'code_snippet': item.get('code_snippet',''),
    'is_consistent': state.is_consistent,
    'detection_method': state.detection_method,
    'detected_comment_type': state.detected_comment_type,
    'inconsistency_reason': state.inconsistency_reason,
    'interface_context': state.interface_context,
    'intention_context': state.intention_context,
    'implementation_context': state.implementation_context,
    'rule_signals': state.rule_signals,
    'rule_hard_fails': state.rule_hard_fails,
    'history': state.history,
}
print(json.dumps(out, ensure_ascii=False))
