from langchain_core.prompts import PromptTemplate
from util.llm import get_llm
from util.code_extractor import extract_python_code
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def optimizer_agent():
    llm = get_llm(role="optimizer")

    prompt = PromptTemplate.from_template(
        (BASE_DIR / "Prompts" / "optimizer.txt").read_text()
    )

    chain = (
        {"code": lambda x: x["code"]}
        | prompt
        | llm
    )

    def invoke(inputs):
        raw = chain.invoke(inputs)
        optimized_code = extract_python_code(raw.content)
        return optimized_code

    return invoke
