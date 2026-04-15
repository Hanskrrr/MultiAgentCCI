import json
from core.state import CodeCommentState
from agents.context_parser_agent import ContextParserAgent
from agents.detector_agent import DetectorAgent
from retrieval.example_retriever import ExampleRetriever

MODEL='glm-4-flash'
ids = ['Return_25','Return_35','Return_47','Return_55','Return_61','Return_65','Return_81','Return_83','Return_101','Return_131','Return_141','Return_143','Return_145','Return_153','Return_155','Return_177','Return_195','Return_207','Return_251','Return_268']

items={}
with open('data/eval_dataset.jsonl','r',encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        o=json.loads(line)
        if o.get('id') in ids:
            items[o['id']]=o

parser=ContextParserAgent(model_name=MODEL, parser_mode='treesitter')
detector=DetectorAgent(model_name=MODEL, retriever=ExampleRetriever())

for _id in ids:
    o=items.get(_id)
    if not o:
        continue
    st=CodeCommentState(code_snippet=o['code_snippet'], original_comment=o['original_comment'])
    st=parser.process(st)
    ctype=detector._detect_comment_type(st.original_comment)
    signals=[]; hard=[]
    if ctype=='return':
        hard, signals = detector._rule_check_return(st)
    if hard:
        print(_id,'RULE_FALSE','|'.join(hard)[:120])
        continue
    prompt=detector._build_prompt(st, ctype, signals)
    sys='You are a strict Software Quality Auditor. Your goal is to detect whether the Original Comment accurately describes the given Current Code after updates.'
    try:
        rsp=detector._call_llm(prompt, sys)
        ok, reason = detector._parse_model_conclusion(rsp)
        print(_id, 'GT', o.get('label_consistent'), 'PRED', ok)
        if o.get('label_consistent') is True and ok is False:
            print('FOUND_FALSE_POSITIVE', _id)
            print('COMMENT', o.get('original_comment'))
            print('RESPONSE_START')
            print(rsp[:2000])
            print('RESPONSE_END')
            break
    except Exception as e:
        print(_id,'ERR',e)
