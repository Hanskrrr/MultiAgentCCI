# 多智能体代码注释一致性检测与修正框架
(Multi-Agent Based Code Comment Consistency Detection and Rectification)

这是一个为了支持本科毕业论文《一种基于多智能体的代码注释一致性检测与修正技术研究》而设计的概念验证与评估框架。该系统旨在通过多个专业化智能体（Agent）的协作，检测代码与其注释之间的不一致性，并在发现不一致时自动修正陈旧或错误的注释。

本框架完全对齐了 ICSE 2025 顶会论文《Code Comment Inconsistency Detection and Rectification Using a Large Language Model》(C4RLLaMA) 中定义的实验基准与评估指标。

## 框架设计思路

本框架采用了“生成-审查 (Generator-Reviewer)”范式和结构化思维链 (Structured CoT)，将复杂的端到端任务拆解为四个主要智能体的协同工作流：

1. **上下文解析智能体 (Context Parser Agent)**：专职负责把复杂的代码逻辑转化为结构化信息。系统采用 LLM 驱动的语义提取技术，能够跨语言（如 Java, Python）精确提取函数签名（Full Signature）、意图层、接口层和实现层信息，弥补了传统 AST 解析库在跨语言和部分代码片段上的局限性。
2. **一致性检测智能体 (Detector Agent)**：基于原始注释、代码片段以及解析出的结构化上下文，执行**标签校验 (Tag Verification)** 和 **实体映射 (Entity Mapping)**，判断代码与注释是否一致。该智能体对“标识符漂移”极其敏感。
3. **注释修正智能体 (Rectifier Agent)**：当检测到不一致时，接收检测报告和结构化上下文，生成修正后的、准确的新注释。
4. **审查与反思智能体 (Reviewer Agent)**：对修正后的注释进行质量把控（Review）。检查新注释是否存在“幻觉”（编造不存在的功能）、参数是否遗漏或描述错误。如果审查未通过，将提供反馈建议并打回（Reject）给修正智能体重新修正，形成闭环。

## 学术级评估体系 (ICSE Baseline)

为了与 C4RLLaMA 及同类顶会研究进行公平的 Baseline 对比，本框架内置了以下自动化评估能力：

- **数据集构造 (Dataset)**：通过 `dataset/download_dataset.py` 自动从 Google Drive 下载并处理与 C4RLLaMA 及多篇顶会论文 (AAAI 2021, EACL 2024) 相同的基准测试集 (Just-In-Time Dataset)。包含了 @param、@return、Summary 三类真实的演化数据作为评估数据集，能够更准确地反映模型在检测和修正方面的能力。
- **检测能力指标 (Detection)**：
  - Accuracy (准确率)
  - Precision (精确率)
  - Recall (召回率)
  - F1-Score
- **修正能力指标 (Rectification / Revision)**：
  - xMatch (精确匹配率)
  - BLEU-4 (四元语法精确度)
  - GLEU (用于句子级评估的改进 BLEU)
  - Meteor (考虑同义词与词干的匹配度)
  - SARI (用于评估文本简化的指标，针对添加、保留和删除词汇评估)

## 目录结构

```text
multi_agent_framework/
├── data/
│   ├── sample_dataset.jsonl      # 最小示例数据集
│   └── eval_dataset.jsonl        # (通过脚本下载生成的) 评估数据集
├── dataset/
│   ├── download_dataset.py       # 数据集下载与构造脚本：自动下载并处理 AAAI-2021 的 Just-In-Time 数据集
│   └── preprocessor.py           # 数据集预处理模块：清洗数据集并转换为标准格式
├── evaluation/
│   └── evaluator.py              # 结果评估模块：对齐 ICSE 标准指标计算 (Precision, Recall, F1, BLEU-4, GLEU, Meteor, 等)
├── core/
│   └── state.py                  # 状态类 (CodeCommentState)，用于在不同智能体间传递上下文与结果数据
├── agents/
│   ├── base_agent.py             # 所有智能体的抽象基类，定义了统一的 process() 方法和 LLM 调用接口
│   ├── context_parser_agent.py   # 解析智能体：使用 AST 提取结构，并利用 LLM 提取多维度上下文
│   ├── detector_agent.py         # 检测智能体：判断代码与原注释是否一致，生成检测报告
│   ├── rectifier_agent.py        # 修正智能体：根据检测报告生成修正后的新注释
│   └── reviewer_agent.py         # 审查/反思智能体：检查修正后的注释质量，提供闭环反馈
├── workflow/
│   └── orchestrator.py           # 工作流编排引擎：组织智能体执行顺序，并处理审查未通过时的重试循环
├── main.py                       # 项目入口：单一样本测试流转
├── main_evaluate.py              # 评估入口：在数据集上批量运行，并输出各模块性能评估指标
└── README.md                     # 项目说明文档
```

## 环境与依赖配置

在运行本项目之前，请确保您的系统中已安装 Python 3.8 或更高版本。建议使用虚拟环境（如 `conda` 或 `venv`）来隔离依赖。

**1. 安装依赖库**

框架代码目录下提供了 `requirements.txt` 文件，包含了运行大模型通信、数据集下载和学术评估（`nltk`, `evaluate`, `scikit-learn`）所需的所有 Python 库。请在终端执行：

```bash
# 确保在 multi_agent_framework 目录下
pip install -r requirements.txt
```

**2. 下载 NLTK 评估数据**

评估模块中的部分指标（如 BLEU-4、Meteor 等）依赖 NLTK 的一些本地语言模型数据。请在终端中运行以下 Python 单行命令一次性下载：

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('wordnet')"
```

**3. 配置 API Keys**

为了使框架能够调用真实的智谱 GLM 模型 或 DeepSeek 模型进行处理，请在**框架代码所在目录（`multi_agent_framework/`）**下创建或编辑 `.env` 文件。

系统已经为您提供了一个参考配置 `.env.example`，您可以将它复制为 `.env`。

```bash
# 智谱 GLM 模型 API Key 
ZHIPUAI_API_KEY="your-zhipuai-api-key-here"

# DeepSeek 模型 API Key
DEEPSEEK_API_KEY="your-deepseek-api-key-here"
```

## 运行演示

**注意：所有的运行命令请在 `multi_agent_framework` 目录下执行（即将您终端的当前路径保持为该项目目录）。**

### 1. 单样本流程测试

在配置好 API Key 之后，您可以运行 `main.py` 测试多智能体框架在单个样本上的交互表现。默认使用 `glm-4-flash` 模型：

```bash
python main.py
```

如果您想切换模型进行对比测试，可以传入 `--model` 参数：
```bash
python main.py --model glm-4-plus
python main.py --model deepseek-chat
python main.py --model deepseek-reasoner
```

### 2. 数据集批量评估测试 (实验跑分)

**步骤一：下载与生成评估数据集**

为了完全对齐 C4RLLaMA 及多篇顶会论文 (Panthaplackel et al., AAAI-2021; Dau et al., EACL-2024)，我们使用相同的 **Just-In-Time Dataset** 基准测试集。请运行以下命令从 Google Drive 自动下载并处理该数据集：

```bash
python dataset/download_dataset.py
```

**步骤二：运行评估程序**

执行以下命令，即可在生成的 `eval_dataset.jsonl` 上运行多智能体的全工作流，对比并输出真实的量化结果报告：

```bash
# 测试智谱基座模型（快速评估前100条数据）
python main_evaluate.py --model glm-4-flash --limit 100

# 测试 DeepSeek 基座模型（快速评估前100条数据）
python main_evaluate.py --model deepseek-chat --limit 100
```

> **注意**：完整的 Just-In-Time 测试集共有 3944 条评估数据。由于调用大模型进行四阶段工作流耗时较长，跑完全量数据集可能需要较长时间。建议先使用 `--limit` 参数进行小批量验证。

## 智能体 Prompt 设计思路

为了在学术基准（Just-In-Time Dataset）上获得高准确率，本项目对各智能体的 Prompt 进行了深度优化。针对 JIT 任务中常见的细粒度矛盾（如 `float` 变为 `double`），我们采用了**“符号比对优先”**的设计逻辑：

1. **全英文推理 (English-Centric Inference)**：利用 LLM 强大的英文预训练语料提高逻辑推理的稳定性。
2. **结构化签名提取 (Explicit Signature Extraction)**：
   - **Context Parser Agent** 强制提取包含 `name` 和 `type` 的结构化参数列表。
   - 解决了 LLM 在处理长代码块时容易忽略函数原型（Signature）细微变化的问题。
3. **基准校准 Few-Shot (Benchmark-Specific Few-Shot)**：
   - **Detector Agent** 引入了针对性的少样本示例，明确定义了“标识符漂移（Identifier Drift）”和“类型漂移（Type Drift）”的判定边界。
   - 告知模型：在学术基准中，哪怕是同义词（如 `file` 变 `requiredFile`）或精度变化（如 `float` 变 `double`），只要符号不匹配，必须判定为 `INCONSISTENT`。
4. **符号比对准则 (Symbolic Comparison Rule)**：
   - 判定标准从泛泛的“语义一致”升级为严格的“符号对齐”。要求模型先列出注释中的实体，再与代码签名进行 1:1 比对。
5. **最小修改原则 (Minimal Edit Principle)**：
   - **Rectifier Agent** 遵循“最小编辑”约束，旨在修复错误的同时尽可能保留原始注释的用词。
   - 这一策略直接对齐了 **SARI** 评估指标的逻辑（鼓励保留 Keep，精确添加 Add，有效删除 Delete）。
6. **多重验证闭环 (Verification Loop)**：
   - **Reviewer Agent** 扮演严格的审计角色，根据 Factuality（事实性）、Completeness（完整性）、Format（格式）三位一体清单进行二次校验。

## 扩展建议（供撰写论文最后一章，“进一步工作”参考）

1. **引入检索增强生成 (RAG)**：在 Context Parser Agent 中，除了分析当前代码块，还可以引入 RAG 技术，从项目的其他文件中检索全局变量定义或接口规范，为检测提供更全局的上下文。
2. **多语言支持**：当前的 AST 提取（在 Context Parser Agent 中）针对 Python。您可以引入 `tree-sitter` 来支持 Java, C++, Go 等多种语言的通用语法树提取。
3. **优化 Prompt 与思维链**：在各个 Agent 的代码中，继续优化 Prompt，采用 Few-Shot（少样本提示）技术，提供正面和反面的一致性检测案例，以提高模型最终的 Detection 和 Rectification 分数。

---
> **关于网络连接的说明**：
> - `evaluate.load("sari")` 首次运行时会尝试连接 HuggingFace 下载相关评估脚本缓存。如果网络不通可能导致报错，因此在第一次运行时请确保机器可以访问 `huggingface.co`。一旦缓存成功，后续即可离线运行。
> - `dataset/download_dataset.py` 由于使用 `gdown` 会连接 Google Drive 下载数据集，同样需要对应的网络访问权限。
