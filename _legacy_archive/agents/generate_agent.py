from langchain_core.prompts import PromptTemplate
from util.llm import get_llm
from util.code_extractor import extract_python_code
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def generator_agent():
    llm = get_llm(role="generator")

    prompt = PromptTemplate.from_template(
        (BASE_DIR / "Prompts" / "generate.txt").read_text()
    )

    chain = (
        {
            "problem": lambda x: x["problem"],
            "plan": lambda x: x["plan"],
        }
        | prompt
        | llm
    )

    def invoke(inputs):
        raw = chain.invoke(inputs)
        clean_code = extract_python_code(raw.content)
        return clean_code

    return invoke
