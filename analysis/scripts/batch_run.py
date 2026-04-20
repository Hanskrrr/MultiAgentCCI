"""
batch_run.py — 通用批次运行器（支持 compact 紧凑模式）。

从 analysis/data/ 下的 JSON 配置文件读取待分析 ID 列表，
对每个样本运行 run_case_once.py 捕获全链路数据，
生成对应 Markdown 报告到 analysis/reports/。

JSON 配置选项：
  compact: true  — 分类规则/Prompt 模板只在报告开头输出一次，
                   每个样本只展示「各自独有」的部分（代码/注释/diff/LLM推理）

用法：
    python analysis/scripts/batch_run.py --config analysis/data/error_ids_summary_batch3.json
"""
import argparse
import json
import subprocess
import sys
import os
from pathlib import Path

TIMEOUT = 90

# ── 分隔关键字：Prompt 中「共用模板」的起始标志 ────────────────────────────────
_SHARED_PROMPT_MARKERS = [
    "Classification Guidelines",
    "Benchmark Examples",
    "Output Requirement",
]


def _split_prompt(prompt: str):
    """把 prompt 拆分成 (unique_part, shared_part)。
    在第一个共用段标志处切断。"""
    if not prompt:
        return '', ''
    lines = prompt.splitlines()
    for i, line in enumerate(lines):
        if any(m in line for m in _SHARED_PROMPT_MARKERS):
            unique = '\n'.join(lines[:i]).strip()
            shared = '\n'.join(lines[i:]).strip()
            return unique, shared
    return prompt.strip(), ''


def run_one(cid: str, model: str, use_diff: bool) -> dict:
    cmd = [sys.executable, 'analysis/run_case_once.py', '--id', cid, '--model', model]
    if use_diff:
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
                obj['_stderr_tail'] = stderr[-200:]
                return obj
        return {'id': cid, 'error': 'no_json',
                'stdout_tail': stdout[-600:], '_stderr_tail': stderr[-200:]}
    except subprocess.TimeoutExpired:
        return {'id': cid, 'error': f'timeout_{TIMEOUT}s'}
    except Exception as e:
        return {'id': cid, 'error': str(e)}


def _cb(w, lang: str, text: str):
    """Write a fenced code block."""
    w.write(f'```{lang}\n{(text or "").strip()}\n```\n\n')


def _h3(w, title: str):
    w.write(f'### {title}\n\n')


def write_report(results: list, config: dict, out_path: Path):
    model    = config.get('model', 'glm-4-plus')
    use_diff = config.get('use_diff', True)
    parser   = config.get('parser', 'treesitter')
    desc     = config.get('description', '')
    compact  = config.get('compact', False)

    total   = len(results)
    errors  = sum(1 for r in results if r.get('error'))
    correct = sum(1 for r in results
                  if not r.get('error') and r.get('label_consistent') == r.get('is_consistent'))

    # 提取共用 Prompt 模板（仅 compact 模式，从第一个成功样本里取）
    shared_prompt_text = ''
    if compact:
        for r in results:
            if not r.get('error') and r.get('full_prompt'):
                _, shared_prompt_text = _split_prompt(r['full_prompt'])
                break

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open('w', encoding='utf-8') as w:
        # ── 报告头 ────────────────────────────────────────────────────────
        w.write(f'# {desc or "误判样本"} — 全链路 Agent 判定报告\n\n')
        w.write('| 项目 | 值 |\n|---|---|\n')
        w.write(f'| 模型 | `{model}` |\n')
        w.write(f'| use-diff | `{use_diff}` |\n')
        w.write(f'| parser | `{parser}` |\n')
        w.write(f'| compact 模式 | `{compact}` |\n')
        w.write(f'| 总样本 | {total} |\n')
        w.write(f'| 运行报错 | {errors} |\n')
        w.write(f'| 本次判对 | {correct} / {total - errors} |\n\n')

        # ── compact 模式：共用 Prompt 模板只输出一次 ─────────────────────
        if compact and shared_prompt_text:
            w.write('## 共用 Prompt 分类规则（所有样本通用，以下每个样本不再重复）\n\n')
            _cb(w, 'text', shared_prompt_text)
            w.write('---\n\n')

        # ── 汇总表 ────────────────────────────────────────────────────────
        w.write('## 汇总一览\n\n')
        w.write('| # | ID | 真实 | 预测 | 判定方式 | 原始注释 |\n')
        w.write('|---|---|---|---|---|---|\n')
        for i, r in enumerate(results, 1):
            cid  = r.get('id', f'?{i}')
            gt   = r.get('label_consistent', '?')
            pred = r.get('is_consistent', '?')
            mark = 'OK' if (gt == pred) else 'FAIL'
            orig = r.get('original_comment', '').strip()[:55]
            w.write(f'| {mark} {i} | `{cid}` | `{gt}` | `{pred}` '
                    f'| `{r.get("detection_method","?")}` | {orig} |\n')
        w.write('\n---\n\n')

        # ── 逐样本详情 ────────────────────────────────────────────────────
        for idx, r in enumerate(results, 1):
            cid  = r.get('id', f'?{idx}')
            gt   = r.get('label_consistent')
            pred = r.get('is_consistent')
            mark = 'OK' if (gt == pred) else 'FAIL'

            w.write(f'## {mark} [{idx}/{total}] `{cid}`\n\n')

            if r.get('error'):
                w.write(f'> **运行错误**: `{r["error"]}`\n\n')
                if r.get('stdout_tail'):
                    _cb(w, 'text', r['stdout_tail'])
                w.write('---\n\n')
                continue

            # 元信息
            orig = (r.get('original_comment') or '').strip()
            gt_c = (r.get('ground_truth_comment') or '').strip()
            w.write('| 字段 | 值 |\n|---|---|\n')
            w.write(f'| 真实标签 | `{gt}` |\n')
            w.write(f'| 预测结果 | `{pred}` |\n')
            w.write(f'| 判定方式 | `{r.get("detection_method")}` |\n')
            w.write(f'| 注释类型 | `{r.get("detected_comment_type")}` |\n')
            w.write(f'| original_comment     | `{orig}` |\n')
            w.write(f'| ground_truth_comment | `{gt_c}` |\n\n')

            # Step 0: 原始数据
            _h3(w, 'Step 0 · 原始数据')
            old_code = (r.get('old_code_snippet') or '').strip()
            new_code = (r.get('code_snippet') or '').strip()
            w.write('**old_code_snippet**\n\n')
            _cb(w, 'java', old_code if old_code else '（空）')
            w.write('**code_snippet**\n\n')
            _cb(w, 'java', new_code)

            # Step 1: ContextParser
            _h3(w, 'Step 1 · ContextParser 输出')
            _cb(w, 'text',
                f'interface:      {r.get("interface_context","")}\n'
                f'intention:      {r.get("intention_context","")}\n'
                f'implementation: {r.get("implementation_context","")}')

            # Step 2: 规则信号
            _h3(w, 'Step 2 · 规则信号')
            _cb(w, 'text',
                f'rule_signals    = {r.get("rule_signals", [])}\n'
                f'rule_hard_fails = {r.get("rule_hard_fails", [])}')

            # Step 3: Prompt 的唯一部分（compact 模式下不重复共用模板）
            prompt = (r.get('full_prompt') or '').strip()
            if prompt:
                if compact:
                    unique_part, _ = _split_prompt(prompt)
                    _h3(w, 'Step 3 · Prompt 样本专属部分（分类规则见报告开头）')
                    _cb(w, 'text', unique_part)
                else:
                    _h3(w, 'Step 3 · 完整 Prompt')
                    _cb(w, 'text', prompt)
            else:
                _h3(w, 'Step 3 · Prompt')
                w.write('> *规则已提前判定，未进入 LLM*\n\n')

            # Step 4: LLM 原始推理
            _h3(w, 'Step 4 · LLM 原始 Reasoning 输出')
            raw = (r.get('llm_raw_response') or '').strip()
            if raw:
                _cb(w, 'text', raw)
            else:
                w.write('> *无 LLM 调用（规则已提前判定）*\n\n')

            # Step 5: Agent 日志（精简）
            history = r.get('history', [])
            if history:
                _h3(w, 'Step 5 · Agent 执行日志')
                _cb(w, 'text', '\n'.join(history))

            w.write('---\n\n')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', required=True)
    ap.add_argument('--out', default=None)
    args = ap.parse_args()

    cfg_path = Path(args.config)
    with cfg_path.open(encoding='utf-8') as f:
        config = json.load(f)

    ids      = config['ids']
    model    = config.get('model', 'glm-4-plus')
    use_diff = config.get('use_diff', True)
    out_path = Path(args.out) if args.out else \
               Path('analysis/reports') / (cfg_path.stem + '_report.md')

    total   = len(ids)
    results = []
    for i, cid in enumerate(ids, 1):
        print(f'[{i}/{total}] {cid} ...', flush=True)
        r = run_one(cid, model, use_diff)
        results.append(r)
        if r.get('error'):
            print(f'  -> ERROR: {r["error"]}', flush=True)
        else:
            gt   = r.get('label_consistent')
            pred = r.get('is_consistent')
            mark = 'OK' if gt == pred else 'FAIL'
            print(f'  -> {mark} gt={gt} pred={pred} [{r.get("detection_method")}]', flush=True)

    write_report(results, config, out_path)
    print(f'\nDone. Report -> {out_path}', flush=True)
