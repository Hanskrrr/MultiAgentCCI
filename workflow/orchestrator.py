from core.state import CodeCommentState
from agents.context_parser_agent import ContextParserAgent
from agents.detector_agent import DetectorAgent
from agents.rectifier_agent import RectifierAgent
from agents.reviewer_agent import ReviewerAgent
from retrieval.example_retriever import ExampleRetriever


class WorkflowOrchestrator:
    """
    工作流编排引擎：
    管理和协调多个智能体的交互流，确保按照既定的执行顺序处理代码和注释。
    """

    def __init__(self, model_name: str = "glm-4-flash", max_retries: int = 3, detect_only: bool = False, verbose: bool = False, parser_mode: str = "treesitter", use_diff: bool = False):
        self.model_name = model_name
        self.detect_only = detect_only
        self.verbose = verbose
        self.use_diff = use_diff
        self.parser = ContextParserAgent(model_name=model_name, parser_mode=parser_mode)
        self.retriever = ExampleRetriever()
        self.summary_retriever = ExampleRetriever(
            data_dir=self._summary_data_dir(),
            cache_dir=self._summary_cache_dir(),
        )
        self.param_retriever = ExampleRetriever(
            data_dir=self._param_data_dir(),
            cache_dir=self._param_cache_dir(),
        )
        self.detector = DetectorAgent(
            model_name=model_name,
            retriever=self.retriever,
            use_treesitter=(parser_mode == "treesitter"),
            summary_retriever=self.summary_retriever,
        )
        self.rectifier = RectifierAgent(
            model_name=model_name,
            retriever=self.retriever,
            summary_retriever=self.summary_retriever,
            param_retriever=self.param_retriever,
        )
        self.reviewer = ReviewerAgent(model_name=model_name)

        self.max_retries = max_retries

    @staticmethod
    def _summary_data_dir() -> str:
        import os
        here = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(here, "..", "dataset", "just_in_time", "Summary")

    @staticmethod
    def _summary_cache_dir() -> str:
        import os
        here = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(here, "..", "retrieval", "cache", "summary")

    @staticmethod
    def _param_data_dir() -> str:
        import os
        here = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(here, "..", "dataset", "just_in_time", "Param")

    @staticmethod
    def _param_cache_dir() -> str:
        import os
        here = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(here, "..", "retrieval", "cache", "param")

    def run(self, code_snippet: str, original_comment: str, old_code_snippet: str = "") -> CodeCommentState:
        """
        开始运行整个代码注释检测与修正管线
        """
        # 1. 初始化状态
        state = CodeCommentState(
            code_snippet=code_snippet,
            original_comment=original_comment,
            old_code_snippet=old_code_snippet if self.use_diff else "",
        )
        state.log("[Orchestrator] 初始化任务，工作流开始。")

        # 2. 上下文解析（Parser）
        state = self.parser.process(state)

        # 3. 一致性检测（Detector）
        state = self.detector.process(state)

        # 4. 仅检测模式：跳过修正和审查
        if self.detect_only:
            if state.is_consistent:
                state.log("[Orchestrator] (仅检测模式) 代码与注释一致。")
            else:
                state.log("[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。")
            return state

        # 5. 如果发现不一致，进入修正与反思循环
        if not state.is_consistent:
            retries = 0
            while retries < self.max_retries:
                state.log(
                    f"[Orchestrator] 开始修正循环，尝试次数 {retries + 1}/{self.max_retries}..."
                )

                # 修正常试
                state = self.rectifier.process(state)

                # 审查智能体进行审查
                state = self.reviewer.process(state)

                # 判断是否通过审查
                if state.review_passed:
                    state.log("[Orchestrator] 修正后的注释通过审查。工作流成功完成。")
                    break
                else:
                    state.log(
                        f"[Orchestrator] 审查未通过，准备重试。反馈信息: {state.review_feedback}"
                    )
                    # 将反馈信息补充到检测报告中，使得下一次修正能包含这些建议
                    state.inconsistency_reason += (
                        f"\n审查官反馈补充: {state.review_feedback}"
                    )
                    retries += 1

            if retries == self.max_retries:
                state.log(
                    "[Orchestrator] 达到最大重试次数，终止工作流。请人工介入审查。"
                )
        else:
            state.log("[Orchestrator] 原代码与注释一致，无需后续流程。")

        return state
