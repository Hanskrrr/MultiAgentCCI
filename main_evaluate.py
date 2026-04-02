import os
from dataset.preprocessor import DatasetPreprocessor
from evaluation.evaluator import Evaluator
from workflow.orchestrator import WorkflowOrchestrator


def main():
    import argparse

    parser = argparse.ArgumentParser(description="数据集批量评估测试")
    parser.add_argument(
        "--model",
        type=str,
        default="glm-4-flash",
        choices=["glm-4-flash", "glm-4-plus", "glm-4.7", "glm-4.7-flash", "glm-5", "deepseek-chat", "deepseek-reasoner"],
        help="指定使用的模型名",
    )
    parser.add_argument(
        "--detect-only",
        action="store_true",
        help="仅运行上下文解析+一致性检测，跳过修正和审查（只输出检测指标）",
    )
    parser.add_argument(
        "--offset",
        type=int,
        default=0,
        help="跳过前 N 条数据，从第 N+1 条开始评估",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="限制跑评估的数据条数，便于小批量验证",
    )
    parser.add_argument(
        "--category",
        type=str,
        default=None,
        choices=["Param", "Return", "Summary"],
        help="只测试指定类型的数据（按 ID 前缀筛选），不指定则测试全部",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="输出每条数据的详细调试信息（判定来源、注释类型、规则信号等）",
    )
    args = parser.parse_args()

    print("===================================================")
    print(f"= 多智能体代码注释一致性系统 - 数据集批量评估模式 ({args.model}) =")
    print("===================================================\n")

    # 1. 加载和预处理数据集
    data_path = os.path.join("data", "eval_dataset.jsonl")
    if not os.path.exists(data_path):
        print(f"[!] 数据集未找到，请先运行: python dataset/download_dataset.py")
        return

    print(f"[*] 正在加载数据集: {data_path}")
    preprocessor = DatasetPreprocessor(data_path)

    try:
        dataset = preprocessor.load_data()
    except FileNotFoundError as e:
        print(e)
        return

    # 过滤掉过长的代码 (此处设为100行)
    dataset = preprocessor.filter_long_code(dataset, max_lines=100)

    if args.category:
        dataset = [d for d in dataset if d["id"].startswith(args.category + "_")]
        print(f"[*] 已按类型筛选: {args.category}，剩余 {len(dataset)} 条数据。")

    if args.offset:
        dataset = dataset[args.offset:]

    if args.limit:
        dataset = dataset[: args.limit]

    print(f"[*] 数据集加载完成，共计 {len(dataset)} 条有效数据。\n")

    # 初始化工作流引擎
    orchestrator = WorkflowOrchestrator(model_name=args.model, max_retries=2, detect_only=args.detect_only, verbose=args.verbose)

    # 用于收集评估结果的容器
    y_true_detection = []
    y_pred_detection = []

    sources_rectification = []
    ground_truths_rectification = []
    generated_rectifications = []

    # 2. 遍历数据集进行批量测试
    for i, data in enumerate(dataset):
        print(f"--- 正在处理第 {i + 1}/{len(dataset)} 条数据 (ID: {data['id']}) ---")

        # 运行智能体框架
        result_state = orchestrator.run(
            code_snippet=data["code_snippet"], original_comment=data["original_comment"]
        )

        # 收集检测评估数据
        y_true_detection.append(data["label_consistent"])
        y_pred_detection.append(result_state.is_consistent)

        # 收集修正评估数据 (仅对真实情况为"不一致"的样本进行修正质量评估)
        if data["label_consistent"] is False:
            sources_rectification.append(data["original_comment"])
            ground_truths_rectification.append(data["ground_truth_comment"])
            # 若智能体也认为不一致并生成了修正注释，则使用新生成的；若漏报，则算作未修改
            if result_state.is_consistent is False and result_state.rectified_comment:
                generated_rectifications.append(result_state.rectified_comment)
            else:
                generated_rectifications.append(data["original_comment"])

        is_correct = data["label_consistent"] == result_state.is_consistent
        mark = "✓" if is_correct else "✗"
        print(
            f"    {mark} 真实标签: {'一致' if data['label_consistent'] else '不一致'} | "
            f"预测标签: {'一致' if result_state.is_consistent else '不一致'} | "
            f"判定方式: {result_state.detection_method} | "
            f"注释类型: {result_state.detected_comment_type}"
        )

        if args.verbose:
            print(f"    [DEBUG] 注释内容: {data['original_comment'][:120]}")
            print(f"    [DEBUG] 接口签名: {result_state.interface_context[:120]}")
            if result_state.rule_signals:
                for sig in result_state.rule_signals:
                    print(f"    [DEBUG] 规则信号: {sig}")
            if result_state.rule_hard_fails:
                for hf in result_state.rule_hard_fails:
                    print(f"    [DEBUG] 规则硬判: {hf}")
            if result_state.inconsistency_reason:
                print(f"    [DEBUG] 不一致原因: {result_state.inconsistency_reason[:200]}")
            if not is_correct:
                if not data["label_consistent"]:
                    print(f"    [DEBUG] 标准注释: {data['ground_truth_comment'][:120]}")
                print(f"    [DEBUG] >>> 此条判定错误 <<<")
            print()

    # 3. 结果评估
    print("\n[*] 正在计算评估指标...")
    evaluator = Evaluator()

    detection_metrics = evaluator.evaluate_detection(
        y_true=y_true_detection, y_pred=y_pred_detection
    )

    if args.detect_only:
        rectification_metrics = None
    else:
        rectification_metrics = evaluator.evaluate_rectification(
            sources=sources_rectification,
            ground_truths=ground_truths_rectification,
            generated_comments=generated_rectifications,
        )

    # 4. 打印报告
    evaluator.generate_report(detection_metrics, rectification_metrics)


if __name__ == "__main__":
    main()
