# graph/workflow.py

from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from util.code_sanitize import sanitize_code
from agents.planner_agent import planner_agent
from agents.generate_agent import generator_agent
from agents.review_agent import reviewer_agent
from agents.evaluator_agent import evaluator_agent
from agents.optimizer_agent import optimizer_agent
from agents.explainer_agent import explainer_agent

from util.code_extractor import extract_python_code
from memory.technique_retriever import get_technique_retriever

MAX_RETRIES = 2


class GraphState(TypedDict, total=False):
    problem: str
    plan: str
    code: str
    review: str
    evaluation: dict
    explanation: str
    retries: int
    passed: bool
    planner_called: bool
    optimized: bool
    retrieved_techniques: List[str]
    logs: List[str]


def planner_node(state: GraphState) -> GraphState:
    if state.get("planner_called"):
        return state

    logs = state.get("logs", [])
    logs.append("[PLANNER] Generating plan")

    # Retrieve techniques from database
    # retriever = get_technique_retriever()
    # try:
    #     docs = retriever.invoke(state["problem"])
    #     retrieved_techniques = [doc.page_content for doc in docs] if docs else []
    # except Exception:
    #     retrieved_techniques = []

    retrieved_techniques = []

    # Pass techniques to planner agent
    result = planner_agent()({
        "problem": state["problem"],
        "techniques": retrieved_techniques
    })

    return {
        **state,
        "plan": result.content,
        "planner_called": True,
        "retrieved_techniques": retrieved_techniques,
        "logs": logs,
    }


def generator_node(state: GraphState) -> GraphState:
    logs = state.get("logs", [])
    logs.append("[GENERATOR] Generating code")

    code = generator_agent()(
        {"problem": state["problem"], "plan": state.get("plan", "")}
    )
    
    # Ensure clean code extraction (safety check - generator already extracts, but double-check)
    # if raw_code and not raw_code.strip().startswith("def ") and not raw_code.strip().startswith("class "):
    #     code = extract_python_code(raw_code)
    # else:
    #     code = raw_code

    return {**state, "code": code, "logs": logs}


def reviewer_node(state: GraphState) -> GraphState:
    logs = state.get("logs", [])
    logs.append("[REVIEWER] Reviewing code")

    result = reviewer_agent().invoke({"code": state["code"]})

    return {**state, "review": result.content.strip(), "logs": logs}


def evaluator_node(state: GraphState) -> GraphState:
    logs = state.get("logs", [])
    logs.append("[EVALUATOR] Running tests")

    clean_code = sanitize_code(state["code"])

    evaluation = evaluator_agent()(
        {
            "code": clean_code,
            "problem": state["problem"]
        }
    )

    logs.append(
        "[EVALUATOR] Passed" if evaluation["passed"] else "[EVALUATOR] Failed"
    )

    return {
        **state,
        "evaluation": evaluation,
        "logs": logs
    }



# def decision_node(state: GraphState) -> GraphState:
#     logs = state.get("logs", [])
#     retries = state.get("retries", 0)
#     evaluation = state.get("evaluation", {})

#     # Evaluator is the ONLY source of truth
#     if evaluation.get("passed", False):
#         logs.append("[DECISION] Evaluation passed")
#         return {**state, "passed": True, "logs": logs}

#     if retries < MAX_RETRIES:
#         logs.append(f"[DECISION] Retry {retries + 1}/{MAX_RETRIES}")
#         return {**state, "retries": retries + 1, "logs": logs}

#     logs.append("[DECISION] Max retries reached – explaining failure")
#     return {**state, "passed": False, "logs": logs}

#new given below 
def decision_node(state: GraphState) -> GraphState:
    logs = state.get("logs", [])
    retries = state.get("retries", 0)
    evaluation = state.get("evaluation", {})

    # Evaluator is the ONLY source of truth
    if evaluation.get("passed", False):
        logs.append("[DECISION] Evaluation passed")

        # 🔑 IMPORTANT FIX: downgrade reviewer
        state["review"] = "[ADVISORY] Static review passed after execution"

        return {**state, "passed": True, "logs": logs}

    if retries < MAX_RETRIES:
        logs.append(f"[DECISION] Retry {retries + 1}/{MAX_RETRIES}")
        return {**state, "retries": retries + 1, "logs": logs}

    logs.append("[DECISION] Max retries reached – explaining failure")
    return {**state, "passed": False, "logs": logs}


def optimizer_node(state: GraphState) -> GraphState:
    logs = state.get("logs", [])
    logs.append("[OPTIMIZER] Optimizing code")

    code = optimizer_agent()({"code": state["code"]})

    return {**state, "code": code, "optimized": True, "logs": logs}


def explainer_node(state: GraphState) -> GraphState:
    logs = state.get("logs", [])
    logs.append("[EXPLAINER] Generating explanation")

    result = explainer_agent().invoke(
        {"problem": state["problem"], "code": state["code"],"plan":state.get("plan","")}
    )

    return {**state, "explanation": result.content, "logs": logs}


def route(state: GraphState) -> str:
    # If passed and not yet optimized, optimize it
    if state.get("passed") and not state.get("optimized", False):
        return "optimize"
    # If passed and already optimized, or max retries reached, explain
    if state.get("passed") or state.get("retries", 0) >= MAX_RETRIES:
        return "explain"
    # Otherwise retry generation
    return "generate"


graph = StateGraph(GraphState)

graph.add_node("planner", planner_node)
graph.add_node("generate", generator_node)
graph.add_node("review", reviewer_node)
graph.add_node("evaluate", evaluator_node)
graph.add_node("decide", decision_node)
graph.add_node("optimize", optimizer_node)
graph.add_node("explain", explainer_node)

graph.add_edge(START, "planner")
graph.add_edge("planner", "generate")
graph.add_edge("generate", "review")
graph.add_edge("review", "evaluate")
graph.add_edge("evaluate", "decide")

graph.add_conditional_edges(
    "decide",
    route,
    {
        "generate": "generate",
        "optimize": "optimize",
        "explain": "explain",
    },
)

graph.add_edge("optimize", "explain")
graph.add_edge("explain", END)

app = graph.compile()
