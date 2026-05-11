from langchain_core.prompts import PromptTemplate
from util.llm import get_llm

def technique_selector_agent():
    llm = get_llm()

    prompt = PromptTemplate.from_template("""
You are an expert algorithm designer.

Given a coding problem and a list of DSA techniques,
select ONLY the techniques that are truly relevant.

PROBLEM:
{problem}

CANDIDATE TECHNIQUES:
{techniques}

RULES:
- Return ONLY the relevant techniques
- Remove irrelevant ones
- Do NOT invent new techniques
- Output as plain text, one technique per line
""")

    return prompt | llm
