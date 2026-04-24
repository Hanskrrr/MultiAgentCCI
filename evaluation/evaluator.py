import sys
from typing import List, Dict
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
import nltk
import evaluate
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.translate.gleu_score import sentence_gleu
from nltk.translate.meteor_score import meteor_score


class Evaluator:
    """
    结果评估模块（学术级标准指标）：
    用于评估多智能体系统的两项核心能力，常用于与 C4RLLaMA 等基线模型对比：
    1. 检测能力 (Detection): Accuracy, Precision, Recall, F1
    2. 修正能力 (Rectification): BLEU-4, SARI
    """

    @staticmethod
    def evaluate_detection(y_true: List[bool], y_pred: List[bool]) -> Dict[str, float]:
        """
        评估检测准确性
        注意：在“不一致检测”任务中，我们通常将“不一致”(False)视为正例(Positive)。
        为了让 scikit-learn 正确计算，我们需要反转标签或指定 pos_label。
        """
        if len(y_true) != len(y_pred):
            raise ValueError("真实的标签和预测的标签数量不一致！")

        # 转换为：True表示“发现不一致”（Positive），False表示“一致”（Negative）
        # 这是学术界计算Precision/Recall/F1的标准做法：检测任务就是“检测不一致”
        y_true_binary = [not label for label in y_true]
        y_pred_binary = [not label for label in y_pred]

        acc = accuracy_score(y_true_binary, y_pred_binary)
        precision = precision_score(y_true_binary, y_pred_binary, zero_division=0)  # type: ignore
        recall = recall_score(y_true_binary, y_pred_binary, zero_division=0)  # type: ignore
        f1 = f1_score(y_true_binary, y_pred_binary, zero_division=0)  # type: ignore

        return {
            "Accuracy": round(acc, 4),
            "Precision": round(precision, 4),
            "Recall": round(recall, 4),
            "F1_Score": round(f1, 4),
            "Total_Samples": len(y_true),
            "Detected_Inconsistencies": sum(y_pred_binary),
        }

    @staticmethod
    def _calculate_bleu4(reference: str, hypothesis: str) -> float:
        """使用 NLTK 计算标准的 BLEU-4 评分"""
        if not reference or not hypothesis:
            return 0.0
        ref_tokens = nltk.word_tokenize(reference)
        hyp_tokens = nltk.word_tokenize(hypothesis)

        # 使用平滑函数防止因为短句子没有 4-gram 匹配而得 0 分
        smoothie = SmoothingFunction().method1
        return float(
            sentence_bleu([ref_tokens], hyp_tokens, smoothing_function=smoothie)  # type: ignore
        )

    _sari_metric = None

    @classmethod
    def _get_sari_metric(cls):
        if cls._sari_metric is None:
            try:
                cls._sari_metric = evaluate.load("sari")
            except Exception as e:
                print(f"Failed to load SARI metric: {e}")
        return cls._sari_metric

    @staticmethod
    def _calculate_sari(source: str, reference: str, hypothesis: str) -> float:
        """使用 evaluate 库计算 SARI 评分"""
        if not source or not reference or not hypothesis:
            return 0.0
        try:
            sari = Evaluator._get_sari_metric()
            if sari is None:
                return 0.0
            result = sari.compute(
                sources=[source], predictions=[hypothesis], references=[[reference]]
            )
            return float(result["sari"] / 100.0)
        except Exception:
            return 0.0

    @staticmethod
    def _calculate_gleu(reference: str, hypothesis: str) -> float:
        """计算 GLEU 分数"""
        if not reference or not hypothesis:
            return 0.0
        ref_tokens = nltk.word_tokenize(reference)
        hyp_tokens = nltk.word_tokenize(hypothesis)
        return sentence_gleu([ref_tokens], hyp_tokens)

    @staticmethod
    def _calculate_meteor(reference: str, hypothesis: str) -> float:
        """计算 Meteor 分数"""
        if not reference or not hypothesis:
            return 0.0
        ref_tokens = nltk.word_tokenize(reference)
        hyp_tokens = nltk.word_tokenize(hypothesis)
        return meteor_score([ref_tokens], hyp_tokens)

    @staticmethod
    def evaluate_rectification(
        sources: List[str],
        ground_truths: List[str],
        generated_comments: List[str],
        sample_ids: List[str] = None,
        code_snippets: List[str] = None,
        detected_flags: List[bool] = None,
        trace_file: str = None,
    ) -> Dict[str, float]:
        """
        评估生成的修正注释质量。
        当 trace_file 不为 None 时，输出逐样本追踪报告到该路径。
        """
        if len(ground_truths) != len(generated_comments) or len(sources) != len(
            generated_comments
        ):
            raise ValueError("真实注释、原注释与生成的注释数量不一致！")

        bleu_scores = []
        sari_scores = []
        gleu_scores = []
        meteor_scores_list = []
        xmatch_count = 0

        total = len(generated_comments)
        print(f"  [评估] 正在计算修正指标，共 {total} 条样本...")

        Evaluator._get_sari_metric()

        for idx, (src, ref, hyp) in enumerate(zip(sources, ground_truths, generated_comments), 1):
            if ref.strip() == hyp.strip():
                xmatch_count += 1

            bleu_scores.append(Evaluator._calculate_bleu4(ref, hyp))
            sari_scores.append(Evaluator._calculate_sari(src, ref, hyp))
            gleu_scores.append(Evaluator._calculate_gleu(ref, hyp))
            meteor_scores_list.append(Evaluator._calculate_meteor(ref, hyp))

            if idx % 10 == 0 or idx == total:
                print(f"  [评估] 进度: {idx}/{total} ({idx * 100 // total}%)", flush=True)

        print("  [评估] 计算完成。", flush=True)
        total = len(bleu_scores)
        if total == 0:
            return {"Samples_Evaluated": 0}

        avg_bleu = sum(bleu_scores) / total
        avg_sari = sum(sari_scores) / total
        avg_gleu = sum(gleu_scores) / total
        avg_meteor = sum(meteor_scores_list) / total
        xmatch_rate = xmatch_count / total

        # --- Trace report ---
        if trace_file and sample_ids and len(sample_ids) == total:
            Evaluator._write_trace_report(
                trace_file, sample_ids, sources, ground_truths,
                generated_comments, code_snippets, detected_flags,
                bleu_scores, sari_scores, gleu_scores, meteor_scores_list,
                {"xMatch (%)": round(xmatch_rate * 100, 2), "BLEU-4": round(avg_bleu, 4),
                 "GLEU": round(avg_gleu, 4), "Meteor": round(avg_meteor, 4),
                 "SARI": round(avg_sari, 4), "Samples_Evaluated": total},
            )
            print(f"  [评估] 逐样本追踪报告已保存: {trace_file}")

        return {
            "xMatch (%)": round(xmatch_rate * 100, 2),
            "BLEU-4": round(avg_bleu, 4),
            "GLEU": round(avg_gleu, 4),
            "Meteor": round(avg_meteor, 4),
            "SARI": round(avg_sari, 4),
            "Samples_Evaluated": total,
        }

    @staticmethod
    def _write_trace_report(
        path: str, ids: List[str], sources: List[str],
        refs: List[str], hyps: List[str],
        codes: List[str], detected: List[bool],
        bleu: List[float], sari: List[float],
        gleu: List[float], meteor: List[float],
        summary: Dict,
    ):
        with open(path, "w", encoding="utf-8") as f:
            f.write("# Rectifier 逐样本追踪报告\n\n")
            f.write("## 汇总指标\n\n")
            for k, v in summary.items():
                f.write(f"- **{k}**: {v}\n")
            f.write("\n")

            # Summary table sorted by SARI ascending (worst first)
            ranked = sorted(range(len(ids)), key=lambda i: sari[i])
            f.write("## 汇总一览（按 SARI 升序，最差排前）\n\n")
            f.write("| # | ID | 检测到 | xMatch | BLEU-4 | SARI | METEOR | 原注释(前60) | 生成(前60) |\n")
            f.write("|---|---|---|---|---|---|---|---|---|\n")
            for rank, i in enumerate(ranked, 1):
                det_mark = "✓" if (detected and detected[i]) else "✗(漏检)"
                xm = "✓" if refs[i].strip() == hyps[i].strip() else ""
                src_short = sources[i][:60].replace("|", "\\|").replace("\n", " ")
                hyp_short = hyps[i][:60].replace("|", "\\|").replace("\n", " ")
                f.write(
                    f"| {rank} | `{ids[i]}` | {det_mark} | {xm} "
                    f"| {bleu[i]:.3f} | {sari[i]:.3f} | {meteor[i]:.3f} "
                    f"| {src_short} | {hyp_short} |\n"
                )

            f.write("\n---\n\n## 逐样本详情\n\n")
            for i in ranked:
                det_mark = "✓ 已检测" if (detected and detected[i]) else "✗ 漏检(使用原注释)"
                f.write(f"### [{i+1}/{len(ids)}] `{ids[i]}`\n\n")
                f.write(f"| 指标 | 值 |\n|---|---|\n")
                f.write(f"| 检测状态 | {det_mark} |\n")
                f.write(f"| BLEU-4 | {bleu[i]:.4f} |\n")
                f.write(f"| SARI | {sari[i]:.4f} |\n")
                f.write(f"| GLEU | {gleu[i]:.4f} |\n")
                f.write(f"| METEOR | {meteor[i]:.4f} |\n")
                f.write(f"| xMatch | {'✓' if refs[i].strip() == hyps[i].strip() else '✗'} |\n\n")

                f.write(f"**原注释 (source)**\n```\n{sources[i]}\n```\n\n")
                f.write(f"**标准注释 (ground truth)**\n```\n{refs[i]}\n```\n\n")
                f.write(f"**生成注释 (generated)**\n```\n{hyps[i]}\n```\n\n")

                if codes and i < len(codes):
                    code_lines = codes[i].split("\n")
                    code_display = "\n".join(code_lines[:30])
                    if len(code_lines) > 30:
                        code_display += "\n// ... (truncated)"
                    f.write(f"**代码片段**\n```java\n{code_display}\n```\n\n")

                f.write("---\n\n")

    @staticmethod
    def generate_report(detection_metrics: Dict, rectification_metrics: Dict = None):
        """打印最终评估报告"""
        print("\n" + "=" * 60)
        print("= 学术级代码注释一致性系统评估报告 (ICSE Baseline) =")
        print("=" * 60)

        print("\n【检测能力评估 (Detection Metrics)】")
        for k, v in detection_metrics.items():
            print(f"  - {k}: {v}")

        if rectification_metrics is not None:
            print("\n【修正能力评估 (Rectification Metrics)】")
            print("  *(真实标签为不一致样本的生成质量)*")
            for k, v in rectification_metrics.items():
                print(f"  - {k}: {v}")
        else:
            print("\n【修正能力评估】已跳过（仅检测模式）")
        print("=" * 60 + "\n")
