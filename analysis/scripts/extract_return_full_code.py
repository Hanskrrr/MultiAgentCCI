import json
import pathlib

ids = '''Return_2 Return_6 Return_8 Return_11 Return_15 Return_17 Return_18 Return_19 Return_24 Return_25 Return_32 Return_35 Return_41 Return_47 Return_48 Return_55 Return_56 Return_58 Return_61 Return_65 Return_74 Return_78 Return_79 Return_80 Return_81 Return_83 Return_84 Return_85 Return_86 Return_88 Return_90 Return_92 Return_103 Return_104 Return_106 Return_115 Return_124 Return_130 Return_132 Return_133 Return_143 Return_144 Return_145 Return_146 Return_147 Return_150 Return_155 Return_157 Return_159 Return_160 Return_162 Return_166 Return_171 Return_173 Return_177 Return_180 Return_192 Return_193 Return_195 Return_198 Return_202 Return_204 Return_209 Return_211 Return_216 Return_220 Return_223 Return_227 Return_229 Return_235 Return_237 Return_240 Return_241 Return_242 Return_243 Return_244 Return_245 Return_252 Return_255 Return_263 Return_265 Return_273 Return_274 Return_276 Return_282 Return_285 Return_293 Return_294 Return_296 Return_298 Return_303 Return_305 Return_306'''.split()

p = pathlib.Path('data/eval_dataset.jsonl')
records = {}
with p.open('r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        obj = json.loads(line)
        _id = obj.get('id')
        if _id in ids:
            records[_id] = obj

out = pathlib.Path('analysis/return_error_cases_full_code.md')
out.parent.mkdir(exist_ok=True)
with out.open('w', encoding='utf-8') as w:
    w.write('# Return误判样本（完整代码）\n\n')
    w.write(f'总ID: {len(ids)}；命中: {len(records)}；缺失: {len([i for i in ids if i not in records])}\n\n')
    for _id in ids:
        r = records.get(_id)
        if not r:
            w.write(f'## {_id}\n- 未找到\n\n')
            continue
        w.write(f'## {_id}\n')
        w.write(f"- label_consistent: {r.get('label_consistent')}\n")
        w.write(f"- original_comment: {str(r.get('original_comment','')).strip()}\n")
        w.write(f"- ground_truth_comment: {str(r.get('ground_truth_comment','')).strip()}\n\n")
        w.write('```java\n')
        w.write(str(r.get('code_snippet','')).rstrip() + '\n')
        w.write('```\n\n')

print('written', out.as_posix(), 'records', len(records))
