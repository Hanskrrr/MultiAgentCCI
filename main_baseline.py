"""
Baseline 实验：使用单一大模型（无提示词工程、无多智能体）进行注释一致性检测与修正。
用于与多智能体框架进行对比。

用法:
  python main_baseline.py --model glm-4-plus --category Return
  python main_baseline.py --model glm-4-plus --category Param --limit 200
"""
import os
from agents.base_agent import BaseAgent
from core.state import CodeCommentState
from dataset.preprocessor import DatasetPreprocessor
from evaluation.evaluator import Evaluator


class NaiveLLMBaseline(BaseAgent):
    """单一 LLM baseline：不加任何 prompt 工程，用最朴素的指令检测和修正。"""

    def __init__(self, model_name: str = "glm-4-flash"):
        super().__init__(name="NaiveBaseline", model_name=model_name)

    def process(self, state: CodeCommentState) -> CodeCommentState:
        raise NotImplementedError

    def detect(self, code: str, comment: str) -> bool:
        system_prompt = "You are a software engineering assistant."
        prompt = (
            f"Given the following code and its comment, determine whether the comment "
            f"is consistent with the code. Answer with ONLY one word: CONSISTENT or INCONSISTENT.\n\n"
            f"Code:\n{code}\n\n"
            f"Comment:\n{comment}"
        )
        try:
            response = self._call_llm(prompt, system_prompt)
            return "INCONSISTENT" not in response.upper()
        except Exception as e:
            print(f"    [Error] {e}")
            return True

    def rectify(self, code: str, comment: str) -> str:
        system_prompt = "You are a software engineering assistant."
        prompt = (
            f"The following code comment is inconsistent with the code. "
            f"Fix the comment to match the code. Output ONLY the corrected comment.\n\n"
            f"Code:\n{code}\n\n"
            f"Comment:\n{comment}"
        )
        try:
            return self._call_llm(prompt, system_prompt).strip()
        except Exception as e:
            print(f"    [Error] rectify: {e}")
            return comment


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Baseline: 单一 LLM 检测+修正（无 prompt 工程）")
    parser.add_argument("--model", type=str, default="glm-4-flash",
                        choices=["glm-4-flash", "glm-4-plus", "glm-4.7", "glm-4.7-flash", "glm-5",
                                 "deepseek-chat", "deepseek-reasoner",
                                 "gpt-4o", "gpt-4o-mini", "gpt-4.1", "gpt-4.1-mini", "o3-mini",
                                 "gemini-2.0-flash", "gemini-2.5-flash", "gemini-2.5-pro"])
    parser.add_argument("--category", type=str, default=None, choices=["Param", "Return", "Summary"])
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    print("===================================================")
    print(f"= Baseline 单模型检测+修正（无 prompt 工程） ({args.model}) =")
    print("===================================================\n")

    data_path = os.path.join("data", "eval_dataset.jsonl")
    if not os.path.exists(data_path):
        print("[!] 数据集未找到，请先运行: python dataset/download_dataset.py")
        return

    preprocessor = DatasetPreprocessor(data_path)
    dataset = preprocessor.load_data()
    dataset = preprocessor.filter_long_code(dataset, max_lines=100)

    if args.category:
        dataset = [d for d in dataset if d["id"].startswith(args.category + "_")]
        print(f"[*] 已按类型筛选: {args.category}，剩余 {len(dataset)} 条数据。")
    if args.offset:
        dataset = dataset[args.offset:]
    if args.limit:
        dataset = dataset[:args.limit]

    print(f"[*] 数据集加载完成，共计 {len(dataset)} 条。\n")

    baseline = NaiveLLMBaseline(model_name=args.model)

    y_true = []
    y_pred = []

    sources_rectification = []
    ground_truths_rectification = []
    generated_rectifications = []

    for i, data in enumerate(dataset):
        print(f"--- 正在处理第 {i + 1}/{len(dataset)} 条 (ID: {data['id']}) ---")

        pred_consistent = baseline.detect(data["code_snippet"], data["original_comment"])

        y_true.append(data["label_consistent"])
        y_pred.append(pred_consistent)

        if data["label_consistent"] is False:
            sources_rectification.append(data["original_comment"])
            ground_truths_rectification.append(data["ground_truth_comment"])
            detected = not pred_consistent
            if detected:
                rectified = baseline.rectify(data["code_snippet"], data["original_comment"])
                generated_rectifications.append(rectified)
            else:
                generated_rectifications.append(data["original_comment"])

        is_correct = data["label_consistent"] == pred_consistent
        mark = "✓" if is_correct else "✗"
        print(
            f"    {mark} 真实: {'一致' if data['label_consistent'] else '不一致'} | "
            f"预测: {'一致' if pred_consistent else '不一致'}"
        )

    print("\n[*] 正在计算评估指标...")
    evaluator = Evaluator()

    detection_metrics = evaluator.evaluate_detection(y_true=y_true, y_pred=y_pred)

    rectification_metrics = None
    if sources_rectification:
        rectification_metrics = evaluator.evaluate_rectification(
            sources=sources_rectification,
            ground_truths=ground_truths_rectification,
            generated_comments=generated_rectifications,
        )

    evaluator.generate_report(detection_metrics, rectification_metrics)


if __name__ == "__main__":
    main()
