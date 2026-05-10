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

try:
    from google import genai as google_genai
    from google.genai import types as google_genai_types
    _GEMINI_AVAILABLE = True
except ImportError:
    _GEMINI_AVAILABLE = False

# 加载环境变量 (需要您在框架代码目录 `multi_agent_framework` 下创建一个 .env 文件)
env_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"
)
load_dotenv(dotenv_path=env_path)

# 代理设置：.env 里写的是 127.0.0.1，但在 WSL2 里需要用 Windows 宿主机 IP。
# 若检测到在 WSL 环境中运行，自动把 127.0.0.1 替换为网关 IP。
def _apply_proxy():
    proxy = os.getenv("HTTPS_PROXY") or os.getenv("HTTP_PROXY")
    if not proxy:
        return
    os.environ.setdefault("ALL_PROXY", proxy)
    try:
        with open("/proc/version") as f:
            is_wsl = "microsoft" in f.read().lower()
    except OSError:
        is_wsl = False
    if is_wsl and "127.0.0.1" in proxy:
        try:
            # Newer WSL mirrored networking can access Windows localhost directly.
            # Keep 127.0.0.1 when it is reachable; only rewrite for older NAT mode.
            import socket
            from urllib.parse import urlparse

            parsed = urlparse(proxy)
            host = parsed.hostname or "127.0.0.1"
            port = parsed.port or 7897
            with socket.create_connection((host, port), timeout=1):
                return
        except Exception:
            pass

        try:
            import subprocess
            result = subprocess.run(
                ["ip", "route", "show", "default"],
                capture_output=True, text=True, timeout=2,
            )
            gateway = result.stdout.split()[2]
            fixed = proxy.replace("127.0.0.1", gateway)
            os.environ["HTTP_PROXY"] = fixed
            os.environ["HTTPS_PROXY"] = fixed
            os.environ["ALL_PROXY"] = fixed
        except Exception:
            pass

_apply_proxy()


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

        elif (self.model_name.startswith("gpt-")
              or self.model_name.startswith("o1")
              or self.model_name.startswith("o3")):
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("请在 .env 文件中配置 OPENAI_API_KEY。")

            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.1,
            )
            return response.choices[0].message.content or ""

        elif self.model_name.startswith("gemini-"):
            if not _GEMINI_AVAILABLE:
                raise ImportError("请先安装新版 Gemini SDK: pip install google-genai")
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("请在 .env 文件中配置 GEMINI_API_KEY。")

            client = google_genai.Client(api_key=api_key)
            system_text = messages[0]["content"] if messages[0]["content"] else None
            user_text = messages[1]["content"] if len(messages) > 1 else ""
            config = google_genai_types.GenerateContentConfig(
                temperature=0.1,
                system_instruction=system_text,
            )
            response = client.models.generate_content(
                model=self.model_name,
                contents=user_text,
                config=config,
            )
            return response.text or ""

        else:
            raise ValueError(
                f"不支持的模型名称: {self.model_name}。"
                f"目前支持 glm-* / deepseek-* / gpt-* / o1* / o3* / gemini-*。"
            )
