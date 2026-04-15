import json
import re
from pathlib import Path
from workflow.orchestrator import WorkflowOrchestrator

ROOT = Path('.')
source_md = ROOT / 'analysis' / 'return_error_cases_full_code.md'
data_path = ROOT / 'data' / 'eval_dataset.jsonl'
out_md = ROOT / 'analysis' / 'return_error_cases_full_code_with_agent_reasons.md'

ids = []
for line in source_md.read_text(encoding='utf-8').splitlines():
    m = re.match(r'^##\s+(Return_\d+)\s*$', line.strip())
    if m:
        ids.append(m.group(1))

records = {}
with data_path.open('r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        obj = json.loads(line)
        oid = obj.get('id')
        if oid in ids:
            records[oid] = obj

model = 'glm-4-flash'
orchestrator = WorkflowOrchestrator(model_name=model, max_retries=2, detect_only=True, verbose=True, parser_mode='treesitter')

missing = [i for i in ids if i not in records]

with out_md.open('w', encoding='utf-8') as w:
    w.write('# Return误判样本（完整代码 + Agent中间原因）\n\n')
    w.write(f'- 样本数: {len(ids)}\n')
    w.write(f'- 命中数据: {len(records)}\n')
    w.write(f'- 模型: `{model}`\n')
    w.write(f'- 运行模式: `detect-only`\n\n')
    if missing:
        w.write('## 缺失ID\n')
        w.write(', '.join(missing) + '\n\n')

    for idx, _id in enumerate(ids, 1):
        item = records.get(_id)
        if item is None:
            continue
        state = orchestrator.run(code_snippet=item['code_snippet'], original_comment=item['original_comment'])

        w.write(f'## {_id}\n')
        w.write(f'- progress: {idx}/{len(ids)}\n')
        w.write(f"- label_consistent(ground truth): {item.get('label_consistent')}\n")
        w.write(f"- detector_prediction(is_consistent): {state.is_consistent}\n")
        w.write(f"- detection_method: {state.detection_method}\n")
        w.write(f"- detected_comment_type: {state.detected_comment_type}\n")
        w.write(f"- original_comment: {str(item.get('original_comment','')).strip()}\n")
        w.write(f"- ground_truth_comment: {str(item.get('ground_truth_comment','')).strip()}\n")
        if state.inconsistency_reason:
            w.write(f"- detector_reason: {state.inconsistency_reason}\n")

        w.write('\n### ContextParser 输出\n')
        w.write('```text\n')
        w.write(f"interface_context:\n{state.interface_context}\n\n")
        w.write(f"intention_context:\n{state.intention_context}\n\n")
        w.write(f"implementation_context:\n{state.implementation_context}\n")
        w.write('```\n\n')

        w.write('### Detector 中间信号\n')
        w.write('```text\n')
        w.write(f"rule_signals: {state.rule_signals}\n")
        w.write(f"rule_hard_fails: {state.rule_hard_fails}\n")
        w.write('```\n\n')

        w.write('### Agent History\n')
        w.write('```text\n')
        for h in state.history:
            w.write(h + '\n')
        w.write('```\n\n')

        w.write('### Full code_snippet\n')
        w.write('```java\n')
        w.write((item.get('code_snippet') or '').rstrip() + '\n')
        w.write('```\n\n')

print(f'written: {out_md}')
