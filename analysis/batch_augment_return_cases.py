import json
import re
import subprocess
import sys
import os
from pathlib import Path

source_md = Path('analysis/return_error_cases_full_code.md')
out_md = Path('analysis/return_error_cases_full_code.md')
model = 'glm-4-flash'
timeout_sec = 35

ids = []
for line in source_md.read_text(encoding='utf-8').splitlines():
    m = re.match(r'^##\s+(Return_\d+)\s*$', line.strip())
    if m:
        ids.append(m.group(1))

results = []
for i, cid in enumerate(ids, 1):
    cmd = [sys.executable, 'analysis/run_case_once.py', '--id', cid, '--model', model]
    try:
        cp = subprocess.run(cmd, capture_output=True, timeout=timeout_sec, env={**os.environ, 'PYTHONPATH': '.'})
        stdout = (cp.stdout or b'').decode('utf-8', errors='ignore')
        stderr = (cp.stderr or b'').decode('utf-8', errors='ignore')
        lines = stdout.strip().splitlines()
        js = None
        for line in reversed(lines):
            t = line.strip()
            if t.startswith('{') and t.endswith('}'):
                js = t
                break
        if js is None:
            results.append({'id': cid, 'error': 'no_json_output', 'stdout': stdout[-500:], 'stderr': stderr[-500:]})
        else:
            obj = json.loads(js)
            obj['runner_stderr_tail'] = stderr[-300:]
            results.append(obj)
    except subprocess.TimeoutExpired:
        results.append({'id': cid, 'error': f'timeout_{timeout_sec}s'})

    print(f'[{i}/{len(ids)}] {cid} done')

with out_md.open('w', encoding='utf-8') as w:
    w.write('# Return误判样本（完整代码 + Multi-Agent中间判定原因）\n\n')
    w.write(f'- 总样本数: {len(ids)}\n')
    w.write(f'- 运行模型: `{model}`\n')
    w.write(f'- 单样本超时: `{timeout_sec}s`\n\n')

    for idx, r in enumerate(results, 1):
        cid = r.get('id', f'UNKNOWN_{idx}')
        w.write(f'## {cid}\n')
        w.write(f'- progress: {idx}/{len(results)}\n')

        if r.get('error'):
            w.write(f"- error: {r['error']}\n")
            if r.get('stdout'):
                w.write(f"- stdout_tail: {r['stdout']}\n")
            if r.get('stderr'):
                w.write(f"- stderr_tail: {r['stderr']}\n")
            w.write('\n')
            continue

        w.write(f"- label_consistent(ground truth): {r.get('label_consistent')}\n")
        w.write(f"- detector_prediction(is_consistent): {r.get('is_consistent')}\n")
        w.write(f"- detection_method: {r.get('detection_method')}\n")
        w.write(f"- detected_comment_type: {r.get('detected_comment_type')}\n")
        w.write(f"- original_comment: {str(r.get('original_comment','')).strip()}\n")
        w.write(f"- ground_truth_comment: {str(r.get('ground_truth_comment','')).strip()}\n")
        if r.get('inconsistency_reason'):
            w.write(f"- detector_reason: {r.get('inconsistency_reason')}\n")

        w.write('\n### ContextParser 输出\n')
        w.write('```text\n')
        w.write(f"interface_context:\n{r.get('interface_context','')}\n\n")
        w.write(f"intention_context:\n{r.get('intention_context','')}\n\n")
        w.write(f"implementation_context:\n{r.get('implementation_context','')}\n")
        w.write('```\n\n')

        w.write('### Detector 中间信号\n')
        w.write('```text\n')
        w.write(f"rule_signals: {r.get('rule_signals', [])}\n")
        w.write(f"rule_hard_fails: {r.get('rule_hard_fails', [])}\n")
        w.write('```\n\n')

        w.write('### Agent History\n')
        w.write('```text\n')
        for h in r.get('history', []):
            w.write(str(h) + '\n')
        w.write('```\n\n')

        w.write('### Full code_snippet\n')
        w.write('```java\n')
        w.write((r.get('code_snippet','') or '').rstrip() + '\n')
        w.write('```\n\n')

print(f'written {out_md}')
