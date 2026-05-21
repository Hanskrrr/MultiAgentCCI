import os
import json
import random

try:
    import gdown
except ImportError:
    import subprocess
    import sys

    print("Installing 'gdown' library...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown"])
    import gdown


def download_and_preprocess(output_file: str, sample_size: int = None):
    """
    下载 AAAI-2021 (Panthaplackel et al.) 论文中的 Just-In-Time Code Comment Inconsistency 数据集。
    该数据集被 C4RLLaMA 等顶会论文用作评估其模型检测与修正能力的基准。
    包含 @param, @return, Summary 三种类型的代码注释一致性数据。
    """
    print("[*] 开始下载 Just-In-Time 数据集...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    jit_dataset_dir = os.path.join(base_dir, "just_in_time")

    # Check if dataset already downloaded
    if not os.path.exists(jit_dataset_dir) or not os.path.exists(
        os.path.join(jit_dataset_dir, "Param", "test.json")
    ):
        # Google Drive folder ID for the dataset
        folder_url = (
            "https://drive.google.com/drive/folders/1heqEQGZHgO6gZzCjuQD1EyYertN4SAYZ"
        )
        try:
            gdown.download_folder(
                url=folder_url, output=jit_dataset_dir, use_cookies=False
            )

            # If folder download didn't work properly for all files, try individual test files
            for cat, file_id in [
                ("Summary", "1_kFHhYRz4U-t8tskbOt-AWMgXBJAe9KQ"),
                ("Return", "1b03YWJMNBmcWkFTHq4qBWcUKkPf5Q2Vl"),
                ("Param", "1Jng5et1MDOwGxriOwhY6GgM9JM9-rv6E"),
            ]:
                cat_dir = os.path.join(jit_dataset_dir, cat)
                os.makedirs(cat_dir, exist_ok=True)
                test_file = os.path.join(cat_dir, "test.json")
                if not os.path.exists(test_file):
                    print(f"[*] 下载单独的 {cat} test.json")
                    gdown.download(id=file_id, output=test_file, quiet=False)

        except Exception as e:
            print(f"[!] 数据集下载失败: {e}")
            print("[!] 请确保安装了 gdown 库并能够访问 Google Drive。")
            return

    print("[*] 数据集下载/检查完毕，开始处理格式...")
    all_data = []

    input_dirs = ["Param", "Return", "Summary"]
    for comment_type in input_dirs:
        test_file = os.path.join(jit_dataset_dir, comment_type, "test.json")
        if not os.path.exists(test_file):
            print(f"[!] 找不到文件: {test_file}")
            continue

        with open(test_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for idx, item in enumerate(data):
            # label 1 means inconsistent (C1 != C2), label 0 means consistent (C1 == C2)
            # label_consistent: True -> label 0 (consistent), False -> label 1 (inconsistent)
            is_consistent = item["label"] == 0

            processed_item = {
                "id": f"{comment_type}_{idx}",
                "code_snippet": item["new_code_raw"],
                "old_code_snippet": item.get("old_code_raw", ""),
                "original_comment": item["old_comment_raw"],
                "label_consistent": is_consistent,
                "ground_truth_comment": item["new_comment_raw"]
                if not is_consistent
                else item["old_comment_raw"],
            }
            all_data.append(processed_item)

    print(f"[*] 共处理了 {len(all_data)} 条测试数据。")

    if sample_size and sample_size < len(all_data):
        random.seed(42)
        # Ensure balanced sampling
        consistent_items = [d for d in all_data if d["label_consistent"]]
        inconsistent_items = [d for d in all_data if not d["label_consistent"]]

        half_size = sample_size // 2
        sampled_consistent = random.sample(
            consistent_items, min(half_size, len(consistent_items))
        )
        sampled_inconsistent = random.sample(
            inconsistent_items,
            min(sample_size - len(sampled_consistent), len(inconsistent_items)),
        )

        all_data = sampled_consistent + sampled_inconsistent
        random.shuffle(all_data)
        print(f"[*] 按要求采样了 {len(all_data)} 条数据。")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        for data in all_data:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

    print(f"[*] 数据集构造完成！已成功保存至: {output_file}")


if __name__ == "__main__":
    output_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "eval_dataset.jsonl",
    )
    # 默认使用完整的测试集进行评估，如果要快速验证可传入 sample_size
    download_and_preprocess(output_path, sample_size=None)
