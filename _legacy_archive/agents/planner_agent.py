from langchain_core.prompts import PromptTemplate
from util.llm import get_llm
from memory.technique_retriever import get_technique_retriever
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def planner_agent():
    llm = get_llm(role="planner")  # smollm2:1.7b or  qwen2.5:7b-instruct
    retriever = get_technique_retriever()

    prompt = PromptTemplate.from_template(
        (BASE_DIR / "Prompts" / "planner.txt").read_text()
    )

    def invoke(inputs):
        problem = inputs["problem"]
        retrieved_techniques = inputs.get("techniques", [])
        
        # Combine LLM reasoning with database techniques
        if retrieved_techniques:
            techniques_text = "\n\n".join([doc.page_content if hasattr(doc, 'page_content') else str(doc) for doc in retrieved_techniques])
        else:
            techniques_text = "No specific techniques found in database."
        
        # Invoke LLM with both problem and retrieved techniques
        result = (
            {
                "problem": lambda x: x["problem"],
                "techniques": lambda x: x["techniques"]
            }
            | prompt
            | llm
        ).invoke({
            "problem": problem,
            "techniques": techniques_text
        })
        
        return result

    return invoke
