import json
import re
from pathlib import Path

from workflow.orchestrator import WorkflowOrchestrator

MODEL = 'glm-4-flash'

root = Path('.')
source_md = root / 'analysis' / 'return_error_cases_full_code.md'
dataset_path = root / 'data' / 'eval_dataset.jsonl'

ids = []
for line in source_md.read_text(encoding='utf-8').splitlines():
    m = re.match(r'^##\s+(Return_\d+)$', line.strip())
    if m:
        ids.append(m.group(1))

items = {}
with dataset_path.open('r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        obj = json.loads(line)
        if obj.get('id') in ids:
            items[obj['id']] = obj

orch = WorkflowOrchestrator(model_name=MODEL, detect_only=True, parser_mode='treesitter', verbose=True)

out_lines = []
out_lines.append('# Return误判样本（完整代码 + 多Agent判定链路）')
out_lines.append('')
out_lines.append(f'模型: `{MODEL}`；运行模式: `detect_only=True`；样本数: {len(ids)}')
out_lines.append('')

for idx, _id in enumerate(ids, start=1):
    item = items.get(_id)
    out_lines.append(f'## {_id}')
    if not item:
        out_lines.append('- 数据集中未找到该ID')
        out_lines.append('')
        continue

    state = orch.run(code_snippet=item['code_snippet'], original_comment=item['original_comment'])

    pred = state.is_consistent
    gt = item.get('label_consistent')
    is_correct = pred == gt

    out_lines.append(f'- 序号: {idx}/{len(ids)}')
    out_lines.append(f'- 真实标签(label_consistent): {gt}')
    out_lines.append(f'- 预测标签(is_consistent): {pred}')
    out_lines.append(f'- 是否判对: {is_correct}')
    out_lines.append(f'- 判定方式(detection_method): {state.detection_method}')
    out_lines.append(f'- 注释类型(detected_comment_type): {state.detected_comment_type}')
    out_lines.append(f'- original_comment: {item.get("original_comment", "")}')
    out_lines.append(f'- ground_truth_comment: {item.get("ground_truth_comment", "")}')
    out_lines.append('')

    out_lines.append('### Code Snippet (full)')
    out_lines.append('```java')
    out_lines.append((item.get('code_snippet') or '').rstrip())
    out_lines.append('```')
    out_lines.append('')

    out_lines.append('### ContextParser 输出')
    out_lines.append(f'- interface_context: `{state.interface_context}`')
    out_lines.append(f'- intention_context: `{state.intention_context}`')
    out_lines.append(f'- implementation_context: `{state.implementation_context}`')
    out_lines.append('')

    out_lines.append('### Detector 中间信号')
    out_lines.append(f'- rule_signals: {state.rule_signals}')
    out_lines.append(f'- rule_hard_fails: {state.rule_hard_fails}')
    out_lines.append(f'- inconsistency_reason: {state.inconsistency_reason}')
    out_lines.append('')

    out_lines.append('### Agent 执行日志(history)')
    out_lines.append('```text')
    for h in state.history:
        out_lines.append(h)
    out_lines.append('```')
    out_lines.append('')

(source_md).write_text('\n'.join(out_lines), encoding='utf-8')
print(f'updated {source_md} with {len(ids)} traced cases')
