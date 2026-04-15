import json
from dataset.preprocessor import DatasetPreprocessor
from core.state import CodeCommentState
from agents.context_parser_agent import ContextParserAgent
from agents.detector_agent import DetectorAgent
from retrieval.example_retriever import ExampleRetriever

TARGET_ID = 'Return_11'  # 真实一致，但你记录里预测不一致(llm)
MODEL = 'glm-4-flash'

# 1) 读取数据集原始项
raw_item = None
with open('data/eval_dataset.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        obj = json.loads(line)
        if obj.get('id') == TARGET_ID:
            raw_item = obj
            break

if raw_item is None:
    raise SystemExit(f'ID not found: {TARGET_ID}')

print('=== [A] Dataset RAW ===')
for k in ['id', 'label_consistent', 'original_comment', 'ground_truth_comment']:
    print(f'{k}: {raw_item.get(k)}')
print('code_snippet(first 300 chars):')
print((raw_item.get('code_snippet','')[:300]).replace('\n','\\n'))
print()

# 2) 经过 preprocessor 后的样本结构
pre = DatasetPreprocessor('data/eval_dataset.jsonl')
dataset = pre.load_data()
item = [d for d in dataset if d['id'] == TARGET_ID][0]
print('=== [B] After Preprocessor.load_data ===')
print({k:item[k] for k in ['id','label_consistent','original_comment','ground_truth_comment']})
print('code lines:', len(item['code_snippet'].split('\n')))
print()

# 3) 进入 state
state = CodeCommentState(code_snippet=item['code_snippet'], original_comment=item['original_comment'])
print('=== [C] Initial State ===')
print('state.original_comment:', state.original_comment)
print('state.code_snippet(first line):', state.code_snippet.split('\n')[0])
print()

# 4) Context Parser
parser = ContextParserAgent(model_name=MODEL, parser_mode='treesitter')
state = parser.process(state)
print('=== [D] After ContextParserAgent ===')
print('interface_context:', state.interface_context)
print('intention_context:', state.intention_context)
print('implementation_context:', state.implementation_context)
print('ast_context keys:', list((state.ast_context or {}).keys()))
print()

# 5) Detector 的中间过程（手动展开，保留LLM原始输出）
retriever = ExampleRetriever()
detector = DetectorAgent(model_name=MODEL, retriever=retriever)

comment_type = detector._detect_comment_type(state.original_comment)
state.detected_comment_type = comment_type
signals = []
hard_fail_reasons = []
if comment_type == 'return':
    hard_fail_reasons, signals = detector._rule_check_return(state)

print('=== [E] Detector pre-LLM ===')
print('comment_type:', comment_type)
print('rule_signals:', signals)
print('rule_hard_fails:', hard_fail_reasons)
print()

prompt = detector._build_prompt(state, comment_type, signals)
system_prompt = (
    'You are a strict Software Quality Auditor. Your goal is to detect whether the '
    'Original Comment accurately describes the given Current Code after updates.'
)
print('=== [F] Prompt Snapshot ===')
print('prompt(first 1200 chars):')
print(prompt[:1200])
print('... [truncated] ...')
print()

print('=== [G] LLM Raw Response ===')
try:
    response = detector._call_llm(prompt, system_prompt)
    print(response)
    is_consistent, reason = detector._parse_model_conclusion(response)
    print('\n=== [H] Parsed Conclusion ===')
    print('parsed_is_consistent:', is_consistent)
    print('parsed_reason:', reason)
except Exception as e:
    print('LLM call failed:', e)

print('\n=== [I] Ground Truth ===')
print('label_consistent:', item['label_consistent'])
print('ground_truth_comment:', item['ground_truth_comment'])
