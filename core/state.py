from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class CodeCommentState:
    """
    状态类：在多智能体之间传递的上下文和结果数据。
    """

    code_snippet: str
    original_comment: str
    old_code_snippet: str = ""

    # 上下文解析智能体提取的信息
    ast_context: Dict = field(default_factory=dict)

    # 意图层、接口层、实现层（多维度思维链上下文）
    intention_context: str = ""
    interface_context: str = ""
    implementation_context: str = ""

    # 检测智能体结果
    is_consistent: Optional[bool] = None
    inconsistency_reason: str = ""
    detection_method: str = ""          # "rule" | "llm"
    detected_comment_type: str = ""     # "param" | "return" | "summary"
    rule_signals: List[str] = field(default_factory=list)
    rule_hard_fails: List[str] = field(default_factory=list)

    # 修正智能体结果
    rectified_comment: str = ""

    # 审查智能体结果
    review_passed: Optional[bool] = None
    review_feedback: str = ""

    # 记录执行历史
    history: List[str] = field(default_factory=list)

    def log(self, message: str):
        self.history.append(message)
