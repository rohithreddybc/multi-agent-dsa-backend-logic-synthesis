from langchain_core.prompts import PromptTemplate
from util.llm import get_llm
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def reviewer_agent():
    llm = get_llm(role="reviewer")

    prompt = PromptTemplate.from_template(
        (BASE_DIR / "Prompts" / "review.txt").read_text()
    )

    return (
        {"code": lambda x: x["code"]}
        | prompt
        | llm
    )
