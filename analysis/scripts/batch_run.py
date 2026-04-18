"""
batch_run.py — 通用批次运行器。

从 analysis/data/ 下的 JSON 配置文件读取待分析 ID 列表，
对每个样本运行 run_case_once.py 捕获全链路数据，
生成对应 Markdown 报告到 analysis/reports/。

用法：
    python analysis/scripts/batch_run.py --config analysis/data/error_ids_diff_set.json
    python analysis/scripts/batch_run.py --config analysis/data/error_ids_summary_diff_set.json
"""
import argparse
import json
import subprocess
import sys
import os
from pathlib import Path

TIMEOUT = 90


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
                obj['_stderr_tail'] = stderr[-300:]
                return obj
        return {'id': cid, 'error': 'no_json',
                'stdout_tail': stdout[-800:], '_stderr_tail': stderr[-300:]}
    except subprocess.TimeoutExpired:
        return {'id': cid, 'error': f'timeout_{TIMEOUT}s'}
    except Exception as e:
        return {'id': cid, 'error': str(e)}


def _section(w, title: str):
    w.write(f'### {title}\n\n')


def _code_block(w, lang: str, text: str):
    w.write(f'```{lang}\n{(text or "").strip()}\n```\n\n')


def write_report(results: list, config: dict, out_path: Path):
    model    = config.get('model', 'glm-4-plus')
    use_diff = config.get('use_diff', True)
    parser   = config.get('parser', 'treesitter')
    desc     = config.get('description', '')

    total   = len(results)
    errors  = sum(1 for r in results if r.get('error'))
    correct = sum(1 for r in results
                  if not r.get('error') and r.get('label_consistent') == r.get('is_consistent'))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open('w', encoding='utf-8') as w:
        w.write(f'# {desc or "误判样本"} — 全链路 Agent 判定报告\n\n')
        w.write('| 项目 | 值 |\n|---|---|\n')
        w.write(f'| 模型 | `{model}` |\n')
        w.write(f'| use-diff | `{use_diff}` |\n')
        w.write(f'| parser | `{parser}` |\n')
        w.write(f'| 总样本 | {total} |\n')
        w.write(f'| 运行报错 | {errors} |\n')
        w.write(f'| 本次判对 | {correct} / {total - errors} |\n\n')

        w.write('## 汇总一览\n\n')
        w.write('| # | ID | 真实标签 | 预测 | 判定方式 | 注释类型 | 原始注释 |\n')
        w.write('|---|---|---|---|---|---|---|\n')
        for i, r in enumerate(results, 1):
            cid  = r.get('id', f'?{i}')
            gt   = r.get('label_consistent', '?')
            pred = r.get('is_consistent', '?')
            mark = 'OK' if (gt == pred) else 'FAIL'
            w.write(f'| {mark} {i} | `{cid}` | `{gt}` | `{pred}` '
                    f'| `{r.get("detection_method","?")}` '
                    f'| `{r.get("detected_comment_type","?")}` '
                    f'| {r.get("original_comment","").strip()[:60]} |\n')
        w.write('\n---\n\n')

        for idx, r in enumerate(results, 1):
            cid  = r.get('id', f'?{idx}')
            gt   = r.get('label_consistent')
            pred = r.get('is_consistent')
            mark = 'OK' if (gt == pred) else 'FAIL'

            w.write(f'## {mark} [{idx}/{total}] `{cid}`\n\n')

            if r.get('error'):
                w.write(f'> **运行错误**: `{r["error"]}`\n\n')
                if r.get('stdout_tail'):
                    _code_block(w, 'text', r['stdout_tail'])
                w.write('---\n\n')
                continue

            w.write('| 字段 | 值 |\n|---|---|\n')
            w.write(f'| 真实标签 | `{gt}` |\n')
            w.write(f'| 预测结果 | `{pred}` |\n')
            w.write(f'| 判定方式 | `{r.get("detection_method")}` |\n')
            w.write(f'| 注释类型 | `{r.get("detected_comment_type")}` |\n')
            w.write(f'| original_comment     | `{(r.get("original_comment") or "").strip()}` |\n')
            w.write(f'| ground_truth_comment | `{(r.get("ground_truth_comment") or "").strip()}` |\n\n')

            _section(w, 'Step 0 · 数据集原始数据')
            old_code = (r.get('old_code_snippet') or '').strip()
            new_code = (r.get('code_snippet') or '').strip()
            w.write('**old_code_snippet**（代码变更前）\n\n')
            _code_block(w, 'java', old_code if old_code else '（空）')
            w.write('**code_snippet**（当前代码）\n\n')
            _code_block(w, 'java', new_code)

            _section(w, 'Step 1 · ContextParserAgent 输出')
            _code_block(w, 'text',
                f'interface_context:\n{r.get("interface_context","（未解析）")}\n\n'
                f'intention_context:\n{r.get("intention_context","（未解析）")}\n\n'
                f'implementation_context:\n{r.get("implementation_context","（未解析）")}')

            _section(w, 'Step 2 · 规则检查结果')
            _code_block(w, 'text',
                f'rule_signals    = {r.get("rule_signals", [])}\n'
                f'rule_hard_fails = {r.get("rule_hard_fails", [])}\n'
                f'\n注：rule_hard_fails 非空时规则直接判定，跳过 LLM。')

            _section(w, 'Step 3 · 注入的 Few-Shot 示例')
            fewshot = (r.get('fewshot_injected') or '').strip()
            if fewshot:
                _code_block(w, 'text', fewshot)
            else:
                w.write('> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）\n\n')

            _section(w, 'Step 4 · 发送给 LLM 的完整 Prompt')
            prompt = (r.get('full_prompt') or '').strip()
            if prompt:
                _code_block(w, 'text', prompt)
            else:
                w.write('> *未捕获*（规则已提前判定）\n\n')

            _section(w, 'Step 5 · LLM 原始 Reasoning 输出')
            raw = (r.get('llm_raw_response') or '').strip()
            if raw:
                _code_block(w, 'text', raw)
            else:
                w.write('> *无 LLM 调用*（规则已提前判定）\n\n')

            _section(w, 'Step 6 · Agent 执行历史日志')
            _code_block(w, 'text', '\n'.join(r.get('history', [])))

            w.write('---\n\n')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', required=True,
                    help='JSON 配置文件路径，如 analysis/data/error_ids_summary_diff_set.json')
    ap.add_argument('--out', default=None,
                    help='输出 MD 路径（默认与配置文件同名放 analysis/reports/）')
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
