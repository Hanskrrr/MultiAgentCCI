import json
import os
from typing import List, Dict


class DatasetPreprocessor:
    """
    数据集预处理模块：
    负责加载代码与注释的公开数据集（如 CodeSearchNet 的变形版本）或自定义 JSONL 数据，
    清洗并将其转换为框架可接收的标准输入格式。
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> List[Dict]:
        """
        加载 JSONL 格式的数据集
        预期格式包含:
        - id: 数据ID
        - code_snippet: 代码片段
        - original_comment: 待检测的原始注释
        - label_consistent: 真实标签（True表示一致，False表示不一致）
        - ground_truth_comment: 真实的标准注释（当 label_consistent 为 False 时用于评估修正质量）
        """
        dataset = []
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"数据集文件未找到: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    item = json.loads(line.strip())
                    dataset.append(
                        {
                            "id": item.get("id"),
                            "code_snippet": item.get("code_snippet", ""),
                            "old_code_snippet": item.get("old_code_snippet", ""),
                            "original_comment": item.get("original_comment", ""),
                            "label_consistent": item.get("label_consistent", True),
                            "ground_truth_comment": item.get(
                                "ground_truth_comment", ""
                            ),
                        }
                    )
        return dataset

    def filter_long_code(self, dataset: List[Dict], max_lines: int = 100) -> List[Dict]:
        """
        清洗数据：过滤掉过长的代码片段，避免超出 LLM 的上下文窗口
        """
        cleaned_dataset = []
        for data in dataset:
            if len(data["code_snippet"].split("\n")) <= max_lines:
                cleaned_dataset.append(data)
        return cleaned_dataset
