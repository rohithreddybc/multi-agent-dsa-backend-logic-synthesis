from langchain_core.prompts import PromptTemplate
from util.llm import get_llm
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def explainer_agent():
    llm = get_llm(role="planner")  # smollm2:1.7b

    prompt = PromptTemplate.from_template(
        (BASE_DIR / "Prompts" / "explain.txt").read_text()
    )

    return (
        {
            "problem": lambda x: x["problem"],
            "code": lambda x: x["code"],
            "plan": lambda x: x['plan']
        }
        | prompt
        | llm
    )
