    # from langchain_ollama import ChatOllama
    # from langchain_core.callbacks import StreamingStdOutCallbackHandler



    # def get_llm(role: str, streaming: bool = False):
    #     """
    #     role:
    #     - planner
    #     - coverage
    #     - reviewer
    #     - generator
    #     - optimizer
    #     """

    #     if role in ["planner", "explainer", "reviewer"]:
    #         #qwen2.5:7b-instruct
    #         #smollm2:1.7b
    #         model = "smollm2:1.7b"
    #         temperature = 0.2

    #     elif role in ["generator", "optimizer"]:
    #         #qwen2.5-coder:7b-instruct
    #         #yi-coder:1.5b
    #         model = "yi-coder:1.5b"
    #         temperature = 0.0

    #     else:
    #         raise ValueError(f"Unknown role: {role}")

    #     return ChatOllama(
    #         model=model,
    #         temperature=temperature,
    #         streaming=streaming,
    #         callbacks=[StreamingStdOutCallbackHandler()] if streaming else None,
    #     )


# -----------------------------------
# below with api same model calling
# llm.py
import os
from dotenv import load_dotenv
from typing import Any

from huggingface_hub import InferenceClient
from langchain_core.runnables import Runnable

# Load .env
load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not HF_TOKEN:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment")


class Response:
    """Simple wrapper to mimic ChatOllama/OpenAI style response"""
    def __init__(self, content: str):
        self.content = content


class HuggingFaceLLM(Runnable):
    """
    LangChain-compatible Hugging Face API LLM
    Mimics ChatOllama by returning object with .content
    """

    def __init__(
        self,
        model_name: str,
        temperature: float = 0.2,
        max_tokens: int = 512,
    ):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

        self.client = InferenceClient(
            model=model_name,
            token=HF_TOKEN,
        )

    def invoke(self, input: Any, config: dict | None = None):
        """
        LangChain calls this.
        input may be:
        - str
        - PromptValue
        - dict (from chain)
        Returns object with .content
        """

        # Convert LangChain PromptValue → string
        if hasattr(input, "to_string"):
            prompt = input.to_string()
        else:
            prompt = str(input)

        response = self.client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

        # Wrap the string in a .content object so workflow code works
        return Response(response.choices[0].message["content"])


def get_llm(role: str, streaming: bool = False):
    """
    Factory for agents
    """

    if role in ["planner", "explainer", "reviewer"]:
        model_name = "Qwen/Qwen2.5-7B-Instruct"
        temperature = 0.2

    elif role in ["generator", "optimizer"]:
        model_name = "Qwen/Qwen2.5-Coder-7B-Instruct"
        temperature = 0.0

    else:
        raise ValueError(f"Unknown role: {role}")

    return HuggingFaceLLM(
        model_name=model_name,
        temperature=temperature,
    )
