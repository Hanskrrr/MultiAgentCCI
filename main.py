from workflow.orchestrator import WorkflowOrchestrator


def main():
    import argparse

    parser = argparse.ArgumentParser(description="单样本多智能体测试")
    parser.add_argument(
        "--model",
        type=str,
        default="glm-4-flash",
        choices=["glm-4-flash", "glm-4-plus", "glm-4.7", "glm-5", "deepseek-chat", "deepseek-reasoner"],
        help="指定使用的模型名",
    )
    parser.add_argument(
        "--detect-only",
        action="store_true",
        help="仅运行上下文解析+一致性检测，跳过修正和审查",
    )
    args = parser.parse_args()

    print("========================================")
    print(f"= 多智能体代码注释一致性检测与修正系统 ({args.model}) =")
    print("========================================\n")

    # 模拟一个实际场景：代码被重构了，但是注释没有更新
    # 原始功能是计算 a + b，但是曾经代码可能是 a * b
    original_comment = "/** \n * 这是一个用于计算并返回两个整数乘积的函数。\n * @param a 第一个乘数\n * @param b 第二个乘数\n * @return a与b的乘积\n */"

    code_snippet = """
def calculate(a: int, b: int) -> int:
    print(f"Calculating sum of {a} and {b}")
    return a + b
"""

    print("【输入】原始代码和注释：")
    print("--- 原始注释 ---")
    print(original_comment)
    print("--- 代码实现 ---")
    print(code_snippet.strip())
    print("-" * 40 + "\n")

    # 初始化工作流引擎
    orchestrator = WorkflowOrchestrator(model_name=args.model, detect_only=args.detect_only)

    # 运行多智能体系统
    result_state = orchestrator.run(code_snippet, original_comment)

    # 打印运行日志
    print("【多智能体执行日志】：")
    for log in result_state.history:
        print(f"  {log}")

    # 输出结果
    print("\n" + "=" * 40)
    print("【最终结果】：")
    if result_state.is_consistent:
        print(">> 代码与注释一致。无需修改。")
    else:
        print(">> 发现不一致！")
        print(f"   原因: {result_state.inconsistency_reason}")
        print("\n>> 修正后的注释：")
        print(result_state.rectified_comment)
        if result_state.review_passed:
            print("\n>> [Reviewer] 审核结果：PASS")
        else:
            print("\n>> [Reviewer] 审核结果：REJECT (需人工介入)")


if __name__ == "__main__":
    main()
