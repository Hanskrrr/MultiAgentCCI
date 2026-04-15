"""
batch_run_v3.py — traces error cases with full instrumentation.

Captures per-sample:
  - ContextParser output
  - Retrieved & injected few-shot examples (full text)
  - Full prompt sent to LLM
  - LLM raw reasoning output
  - Rule signals / hard-fails
  - Agent history log
  - Old + New code snippets

Output: analysis/reports/return_errors_batch3.md
"""
import json
import subprocess
import sys
import os
from pathlib import Path

MODEL     = 'glm-4-plus'
USE_DIFF  = True
TIMEOUT   = 90
OUT_MD    = Path('analysis/reports/return_errors_batch3.md')

ERROR_IDS = [
    'Return_18', 'Return_23', 'Return_24', 'Return_33', 'Return_35',
    'Return_37', 'Return_47', 'Return_48', 'Return_54', 'Return_56',
    'Return_58', 'Return_61', 'Return_62', 'Return_64', 'Return_65',
    'Return_74', 'Return_78', 'Return_80', 'Return_81', 'Return_83',
    'Return_84', 'Return_86', 'Return_88', 'Return_90', 'Return_97',
    'Return_103', 'Return_104', 'Return_106', 'Return_114', 'Return_115',
    'Return_122', 'Return_124', 'Return_126', 'Return_130', 'Return_133',
    'Return_136', 'Return_143', 'Return_144', 'Return_145', 'Return_150',
    'Return_155', 'Return_160', 'Return_164', 'Return_165', 'Return_177',
    'Return_180', 'Return_190', 'Return_192', 'Return_193', 'Return_198',
    'Return_202',
]


def run_one(cid: str) -> dict:
    cmd = [sys.executable, 'analysis/run_case_once.py', '--id', cid, '--model', MODEL]
    if USE_DIFF:
        cmd.append('--use-diff')
    try:
        cp = subprocess.run(
            cmd, capture_output=True, timeout=TIMEOUT,
            env={**os.environ, 'PYTHONPATH': '.'},
        )
        stdout = (cp.stdout or b'').decode('utf-8', errors='ignore')
        stderr = (cp.stderr or b'').decode('utf-8', errors='ignore')
        for line in reversed(stdout.strip().splitlines()):
            t = line.strip()
            if t.startswith('{') and t.endswith('}'):
                obj = json.loads(t)
                obj['_stderr_tail'] = stderr[-300:]
                return obj
        return {'id': cid, 'error': 'no_json',
                'stdout_tail': stdout[-600:], '_stderr_tail': stderr[-300:]}
    except subprocess.TimeoutExpired:
        return {'id': cid, 'error': f'timeout_{TIMEOUT}s'}
    except Exception as e:
        return {'id': cid, 'error': str(e)}


def _section(w, title: str):
    w.write(f'### {title}\n\n')


def _code_block(w, lang: str, text: str):
    w.write(f'```{lang}\n{text.strip()}\n```\n\n')


def write_report(results: list):
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    total   = len(results)
    errors  = sum(1 for r in results if r.get('error'))
    correct = sum(1 for r in results
                  if not r.get('error') and r.get('label_consistent') == r.get('is_consistent'))

    with OUT_MD.open('w', encoding='utf-8') as w:
        # ── header ──────────────────────────────────────────────────────
        w.write('# Return 误判样本批次3 — 全链路 Agent 判定报告\n\n')
        w.write(f'| 项目 | 值 |\n|---|---|\n')
        w.write(f'| 模型 | `{MODEL}` |\n')
        w.write(f'| use-diff | `{USE_DIFF}` |\n')
        w.write(f'| parser | `treesitter` |\n')
        w.write(f'| 总样本 | {total} |\n')
        w.write(f'| 运行报错 | {errors} |\n')
        w.write(f'| 本次判对 | {correct} / {total - errors} |\n\n')
        w.write('---\n\n')

        for idx, r in enumerate(results, 1):
            cid  = r.get('id', f'?{idx}')
            gt   = r.get('label_consistent')
            pred = r.get('is_consistent')
            ok   = (gt == pred)
            mark = '✓' if ok else '✗'

            w.write(f'## {mark} [{idx}/{total}] `{cid}`\n\n')

            # ── error shortcut ───────────────────────────────────────────
            if r.get('error'):
                w.write(f'> **运行错误**: `{r["error"]}`\n\n')
                if r.get('stdout_tail'):
                    _code_block(w, 'text', r['stdout_tail'])
                w.write('---\n\n')
                continue

            # ── meta table ───────────────────────────────────────────────
            w.write('| 字段 | 值 |\n|---|---|\n')
            w.write(f'| 真实标签 | `{gt}` |\n')
            w.write(f'| 预测标签 | `{pred}` |\n')
            w.write(f'| 判定方式 | `{r.get("detection_method")}` |\n')
            w.write(f'| 注释类型 | `{r.get("detected_comment_type")}` |\n')
            w.write(f'| original_comment | {r.get("original_comment","").strip()} |\n')
            w.write(f'| ground_truth_comment | {r.get("ground_truth_comment","").strip()} |\n\n')

            # ── Step 1: ContextParser ────────────────────────────────────
            _section(w, 'Step 1 · ContextParser 输出')
            _code_block(w, 'text',
                f'interface_context:\n{r.get("interface_context","")}\n\n'
                f'intention_context:\n{r.get("intention_context","")}\n\n'
                f'implementation_context:\n{r.get("implementation_context","")}')

            # ── Step 2: Rule checks ──────────────────────────────────────
            _section(w, 'Step 2 · Detector 规则检查')
            _code_block(w, 'text',
                f'rule_signals  : {r.get("rule_signals", [])}\n'
                f'rule_hard_fails: {r.get("rule_hard_fails", [])}')

            # ── Step 3: Few-shot injected ────────────────────────────────
            _section(w, 'Step 3 · 注入的 Few-Shot 示例（Retriever 检索结果）')
            fewshot = r.get('fewshot_injected', '').strip()
            if fewshot:
                _code_block(w, 'text', fewshot)
            else:
                w.write('> *无 few-shot（retriever 未加载 / 非 return 类型)*\n\n')

            # ── Step 4: Full prompt ──────────────────────────────────────
            _section(w, 'Step 4 · 发送给 LLM 的完整 Prompt')
            prompt = r.get('full_prompt', '').strip()
            if prompt:
                _code_block(w, 'text', prompt)
            else:
                w.write('> *未捕获（规则已提前判定）*\n\n')

            # ── Step 5: LLM raw reasoning ────────────────────────────────
            _section(w, 'Step 5 · LLM 原始 Reasoning 输出')
            raw = r.get('llm_raw_response', '').strip()
            if raw:
                _code_block(w, 'text', raw)
            else:
                w.write('> *无 LLM 调用（规则已提前判定）*\n\n')

            # ── Step 6: Agent history ────────────────────────────────────
            _section(w, 'Step 6 · Agent 执行日志 (history)')
            _code_block(w, 'text', '\n'.join(r.get('history', [])))

            # ── Old / New code ───────────────────────────────────────────
            old = (r.get('old_code_snippet') or '').strip()
            new = (r.get('code_snippet') or '').strip()
            if old:
                _section(w, 'Old Code Snippet')
                _code_block(w, 'java', old)
            _section(w, 'New Code Snippet (current)')
            _code_block(w, 'java', new)

            w.write('---\n\n')


if __name__ == '__main__':
    total = len(ERROR_IDS)
    results = []
    for i, cid in enumerate(ERROR_IDS, 1):
        print(f'[{i}/{total}] {cid} ...', flush=True)
        r = run_one(cid)
        results.append(r)
        if r.get('error'):
            print(f'  -> ERROR: {r["error"]}', flush=True)
        else:
            status = f'gt={r.get("label_consistent")} pred={r.get("is_consistent")} [{r.get("detection_method")}]'
            print(f'  -> {status}', flush=True)

    write_report(results)
    print(f'\nDone. Report: {OUT_MD}')
