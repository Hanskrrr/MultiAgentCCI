"""
Batch runner for error-case set #2 (glm-4-plus, use-diff, treesitter).
Spawns run_case_once.py per ID, captures JSON result, writes a detailed
Markdown report to analysis/reports/return_errors_batch2_glm4plus_diff.md
"""
import json
import re
import subprocess
import sys
import os
from pathlib import Path

MODEL = 'glm-4-plus'
USE_DIFF = True
TIMEOUT_SEC = 60
OUT_MD = Path('analysis/reports/return_errors_batch2_glm4plus_diff.md')

# --- error IDs from the user's run log ---
ERROR_IDS = [
    # offset=0 batch (Return_0-99)
    'Return_9',
    'Return_18', 'Return_24', 'Return_25', 'Return_27',
    'Return_35', 'Return_47', 'Return_48', 'Return_54', 'Return_56',
    'Return_61', 'Return_62', 'Return_64', 'Return_74', 'Return_78',
    'Return_80', 'Return_81', 'Return_83', 'Return_84', 'Return_85',
    'Return_86', 'Return_88', 'Return_90', 'Return_102',
    # offset=100 batch (Return_103-202)
    'Return_103', 'Return_104', 'Return_106', 'Return_111', 'Return_114',
    'Return_115', 'Return_122', 'Return_124', 'Return_130', 'Return_132',
    'Return_133', 'Return_143', 'Return_144', 'Return_145', 'Return_146',
    'Return_147', 'Return_150', 'Return_155', 'Return_157', 'Return_159',
    'Return_160', 'Return_162', 'Return_164', 'Return_166', 'Return_168',
    'Return_177', 'Return_180', 'Return_192', 'Return_193', 'Return_194',
    'Return_195', 'Return_198', 'Return_202',
]


def run_one(cid: str) -> dict:
    cmd = [sys.executable, 'analysis/run_case_once.py', '--id', cid, '--model', MODEL]
    if USE_DIFF:
        cmd.append('--use-diff')
    try:
        cp = subprocess.run(
            cmd,
            capture_output=True,
            timeout=TIMEOUT_SEC,
            env={**os.environ, 'PYTHONPATH': '.'},
        )
        stdout = (cp.stdout or b'').decode('utf-8', errors='ignore')
        stderr = (cp.stderr or b'').decode('utf-8', errors='ignore')
        for line in reversed(stdout.strip().splitlines()):
            t = line.strip()
            if t.startswith('{') and t.endswith('}'):
                obj = json.loads(t)
                obj['_stderr_tail'] = stderr[-400:]
                return obj
        return {'id': cid, 'error': 'no_json', 'stdout_tail': stdout[-500:], '_stderr_tail': stderr[-400:]}
    except subprocess.TimeoutExpired:
        return {'id': cid, 'error': f'timeout_{TIMEOUT_SEC}s'}
    except Exception as e:
        return {'id': cid, 'error': str(e)}


def write_report(results: list):
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    with OUT_MD.open('w', encoding='utf-8') as w:
        w.write('# Return 误判样本批次2 — Agent 判定链路报告\n\n')
        w.write(f'- 模型: `{MODEL}`\n')
        w.write(f'- use-diff: `{USE_DIFF}`\n')
        w.write(f'- parser: `treesitter`\n')
        w.write(f'- 总样本: {len(results)}\n\n')

        for idx, r in enumerate(results, 1):
            cid = r.get('id', f'UNKNOWN_{idx}')
            gt = r.get('label_consistent')
            pred = r.get('is_consistent')
            correct = (gt == pred)
            mark = '✓' if correct else '✗'

            w.write(f'## {mark} [{idx}/{len(results)}] {cid}\n\n')

            if r.get('error'):
                w.write(f'- **error**: `{r["error"]}`\n')
                if r.get('stdout_tail'):
                    w.write(f'- stdout_tail:\n```\n{r["stdout_tail"]}\n```\n')
                if r.get('_stderr_tail'):
                    w.write(f'- stderr_tail:\n```\n{r["_stderr_tail"]}\n```\n')
                w.write('\n')
                continue

            w.write(f'- **真实标签 (label_consistent)**: `{gt}`\n')
            w.write(f'- **预测标签 (is_consistent)**: `{pred}`\n')
            w.write(f'- **判定方式 (detection_method)**: `{r.get("detection_method")}`\n')
            w.write(f'- **注释类型**: `{r.get("detected_comment_type")}`\n')
            w.write(f'- **original_comment**: {r.get("original_comment","").strip()}\n')
            w.write(f'- **ground_truth_comment**: {r.get("ground_truth_comment","").strip()}\n')
            if r.get('inconsistency_reason'):
                w.write(f'- **detector_reason**:\n\n```text\n{r["inconsistency_reason"].strip()}\n```\n')
            w.write('\n')

            # --- ContextParser 输出 ---
            w.write('### ContextParser 输出\n\n')
            w.write('```text\n')
            w.write(f'interface_context:\n{r.get("interface_context","")}\n\n')
            w.write(f'intention_context:\n{r.get("intention_context","")}\n\n')
            w.write(f'implementation_context:\n{r.get("implementation_context","")}\n')
            w.write('```\n\n')

            # --- Detector 规则信号 ---
            w.write('### Detector 规则信号\n\n')
            w.write('```text\n')
            w.write(f'rule_signals  : {r.get("rule_signals", [])}\n')
            w.write(f'rule_hard_fails: {r.get("rule_hard_fails", [])}\n')
            w.write('```\n\n')

            # --- Agent 执行日志 ---
            w.write('### Agent 执行日志 (history)\n\n')
            w.write('```text\n')
            for h in r.get('history', []):
                w.write(str(h) + '\n')
            w.write('```\n\n')

            # --- old / new code ---
            old = (r.get('old_code_snippet') or '').strip()
            new = (r.get('code_snippet') or '').strip()
            if old:
                w.write('### Old Code Snippet\n\n')
                w.write('```java\n')
                w.write(old + '\n')
                w.write('```\n\n')

            w.write('### New Code Snippet (current)\n\n')
            w.write('```java\n')
            w.write(new + '\n')
            w.write('```\n\n')

            w.write('---\n\n')


if __name__ == '__main__':
    total = len(ERROR_IDS)
    results = []
    for i, cid in enumerate(ERROR_IDS, 1):
        print(f'[{i}/{total}] running {cid} ...', flush=True)
        r = run_one(cid)
        results.append(r)
        status = r.get('error') or f"gt={r.get('label_consistent')} pred={r.get('is_consistent')} {r.get('detection_method')}"
        print(f'  -> {status}', flush=True)

    write_report(results)
    print(f'\nDone. Report written to: {OUT_MD}')
