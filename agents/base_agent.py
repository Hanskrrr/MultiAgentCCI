import os
import time
from abc import ABC, abstractmethod
import sys

# 将根目录加入环境变量以便导入
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.state import CodeCommentState

# 导入 LLM SDKs
from openai import OpenAI
from zhipuai import ZhipuAI
from dotenv import load_dotenv

# 加载环境变量 (需要您在框架代码目录 `multi_agent_framework` 下创建一个 .env 文件)
env_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"
)
load_dotenv(dotenv_path=env_path)


class BaseAgent(ABC):
    """
    所有智能体的基类，统一定义接口与 LLM 调用。
    """

    def __init__(self, name: str, model_name: str = "glm-4-flash"):
        self.name = name
        self.model_name = model_name

    @abstractmethod
    def process(self, state: CodeCommentState) -> CodeCommentState:
        """
        处理传入的状态，执行当前智能体的任务，并返回更新后的状态。
        """
        pass

    def _call_llm(self, prompt: str, system_prompt: str = "", max_retries: int = 3) -> str:
        """
        调用大模型的封装方法，支持 DeepSeek 与 智谱 GLM 模型。
        内置自动重试：遇到限流、网络超时等临时错误会等待后重试。
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

        for attempt in range(1, max_retries + 1):
            try:
                return self._do_api_call(messages)
            except Exception as e:
                err_str = str(e).lower()
                is_retryable = any(
                    kw in err_str for kw in ["429", "rate", "limit", "timeout", "connection", "server"]
                )
                if is_retryable and attempt < max_retries:
                    wait = 2 ** attempt
                    print(f"    [Retry] API 调用失败 ({e}), {wait}s 后第 {attempt+1} 次重试...")
                    time.sleep(wait)
                else:
                    raise

        raise RuntimeError("Unreachable")

    def _do_api_call(self, messages: list) -> str:
        if self.model_name.startswith("glm-"):
            api_key = os.getenv("ZHIPUAI_API_KEY")
            if not api_key:
                raise ValueError("请在 .env 文件中配置 ZHIPUAI_API_KEY。")

            client = ZhipuAI(api_key=api_key)
            response = client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.1,
            )
            return response.choices[0].message.content or ""  # type: ignore

        elif self.model_name.startswith("deepseek-"):
            api_key = os.getenv("DEEPSEEK_API_KEY")
            if not api_key:
                raise ValueError("请在 .env 文件中配置 DEEPSEEK_API_KEY。")

            client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
            response = client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.1,
            )
            return response.choices[0].message.content or ""

        else:
            raise ValueError(
                f"不支持的模型名称: {self.model_name}。目前仅支持 glm-* 或 deepseek-*。"
            )
