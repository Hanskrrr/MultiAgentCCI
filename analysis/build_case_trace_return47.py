import json
import pathlib
from core.state import CodeCommentState
from agents.context_parser_agent import ContextParserAgent
from agents.detector_agent import DetectorAgent
from retrieval.example_retriever import ExampleRetriever

TARGET_ID = 'Return_47'
MODEL = 'glm-4-flash'

# load raw item
raw = None
with open('data/eval_dataset.jsonl','r',encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        o = json.loads(line)
        if o.get('id') == TARGET_ID:
            raw = o
            break
if raw is None:
    raise SystemExit(f'ID not found: {TARGET_ID}')

# run parser + detector and capture intermediate artifacts
state = CodeCommentState(code_snippet=raw['code_snippet'], original_comment=raw['original_comment'])
parser = ContextParserAgent(model_name=MODEL, parser_mode='treesitter')
state = parser.process(state)

detector = DetectorAgent(model_name=MODEL, retriever=ExampleRetriever())
comment_type = detector._detect_comment_type(state.original_comment)
signals = []
hard_fail_reasons = []
if comment_type == 'return':
    hard_fail_reasons, signals = detector._rule_check_return(state)

prompt = detector._build_prompt(state, comment_type, signals)
system_prompt = (
    'You are a strict Software Quality Auditor. Your goal is to detect whether the '
    'Original Comment accurately describes the given Current Code after updates.'
)

llm_response = ''
llm_error = ''
parsed_is_consistent = None
parsed_reason = ''
if hard_fail_reasons:
    parsed_is_consistent = False
    parsed_reason = ' | '.join(hard_fail_reasons)
else:
    try:
        llm_response = detector._call_llm(prompt, system_prompt)
        parsed_is_consistent, parsed_reason = detector._parse_model_conclusion(llm_response)
    except Exception as e:
        llm_error = str(e)

# write report
out = pathlib.Path('analysis/case_trace_Return_47.md')
out.parent.mkdir(exist_ok=True)
with out.open('w', encoding='utf-8') as w:
    w.write('# Case Trace: Return_47\n\n')
    w.write('## 1) Dataset Raw Item\n')
    w.write(f"- id: {raw.get('id')}\n")
    w.write(f"- label_consistent (ground truth): {raw.get('label_consistent')}\n")
    w.write(f"- original_comment: {raw.get('original_comment')}\n")
    w.write(f"- ground_truth_comment: {raw.get('ground_truth_comment')}\n\n")

    w.write('### Full code_snippet\n')
    w.write('```java\n')
    w.write((raw.get('code_snippet') or '').rstrip() + '\n')
    w.write('```\n\n')

    w.write('## 2) State After ContextParserAgent\n')
    w.write(f"- detected comment type (pre): {comment_type}\n")
    w.write(f"- interface_context:\n\n```text\n{state.interface_context}\n```\n\n")
    w.write(f"- intention_context: `{state.intention_context}`\n")
    w.write(f"- implementation_context: `{state.implementation_context}`\n")
    w.write(f"- ast_context keys: {list((state.ast_context or {}).keys())}\n\n")

    w.write('## 3) Detector Pre-LLM Checks\n')
    w.write(f"- rule_signals: {signals}\n")
    w.write(f"- rule_hard_fails: {hard_fail_reasons}\n\n")

    w.write('## 4) Prompt (truncated to 2000 chars)\n')
    w.write('```text\n')
    w.write(prompt[:2000])
    w.write('\n```\n\n')

    w.write('## 5) LLM Raw Response\n')
    if llm_error:
        w.write(f"- llm_error: {llm_error}\n\n")
    else:
        w.write('```text\n')
        w.write(llm_response.strip() + '\n')
        w.write('```\n\n')

    w.write('## 6) Parsed Detector Output\n')
    w.write(f"- parsed_is_consistent: {parsed_is_consistent}\n")
    w.write(f"- parsed_reason: {parsed_reason}\n\n")

    w.write('## 7) Why This Can Be Misclassified\n')
    w.write('- The comment is a return-style sentence: `@return false ... true otherwise`, implying boolean semantics.\n')
    w.write('- The method signature in this sample is `void offer(...)`, so strict auditors may conclude return semantics mismatch.\n')
    w.write('- In JIT datasets, comments may lag code updates; however this particular sample is labeled consistent, so model strictness can over-trigger false positives.\n')
    w.write('- Prompt wording emphasizes strict symbol/behavior alignment, which can amplify this type of mismatch judgment.\n')

print('written', out.as_posix())
