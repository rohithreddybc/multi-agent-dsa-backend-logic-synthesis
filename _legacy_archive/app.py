# import streamlit as st
# import pandas as pd
# from graph.workflow import app as workflow_app

# # -------------------------------------------------
# # Page Configuration
# # -------------------------------------------------
# st.set_page_config(
#     page_title="Multi-Agent Code System",
#     layout="wide"
# )

# # -------------------------------------------------
# # Custom CSS
# # -------------------------------------------------
# st.markdown(
#     """
#     <style>
#     .center-title {
#         text-align: center;
#         font-size: 2rem;
#         font-weight: bold;
#     }
#     .center-subtitle {
#         text-align: center;
#         color: white;
#         font-size: 1rem;
#         margin-bottom: 0.5rem;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # -------------------------------------------------
# # Header
# # -------------------------------------------------
# st.markdown("<h1 class='center-title'>⧈ Multi-Agent Code System</h1>", unsafe_allow_html=True)
# st.markdown(
#     "<div class='center-subtitle'>A Distributed AI Agent Framework for Backend Architecture Modeling</div>",
#     unsafe_allow_html=True
# )
# st.markdown("<hr>", unsafe_allow_html=True)

# # -------------------------------------------------
# # Session State
# # -------------------------------------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "running" not in st.session_state:
#     st.session_state.running = False

# # -------------------------------------------------
# # ✅ FIXED Utility Functions
# # -------------------------------------------------
# def compute_confidence(result: dict) -> int:
#     """
#     Confidence is based ONLY on execution outcome and retries.
#     Static review does NOT reduce confidence after pass.
#     """
#     score = 100

#     if not result.get("passed"):
#         score -= 40

#     score -= result.get("retries", 0) * 10

#     return max(score, 0)


# def detect_severity(result: dict) -> str:
#     """
#     Execution result is the source of truth.
#     Reviewer output is advisory only after pass.
#     """
#     passed = result.get("passed", False)
#     review = result.get("review", "")

#     if passed:
#         return "LOW"

#     if "LOGIC_FAIL" in review:
#         return "CRITICAL"

#     if "SYNTAX" in review:
#         return "HIGH"

#     return "MEDIUM"


# def render_dag(logs: list):
#     edges = [
#         ("Planner", "Generator"),
#         ("Generator", "Reviewer"),
#         ("Reviewer", "Evaluator"),
#         ("Evaluator", "Decision"),
#         ("Decision", "Generator"),
#         ("Decision", "Explainer")
#     ]

#     dot = "digraph Agents {\n"
#     dot += "rankdir=LR;\n"
#     dot += "node [shape=box, style=rounded];\n"

#     for src, dst in edges:
#         dot += f'"{src}" -> "{dst}";\n'

#     dot += "}\n"
#     st.graphviz_chart(dot)

# # -------------------------------------------------
# # Render Chat History
# # -------------------------------------------------
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

#         if msg["role"] == "assistant" and "result" in msg:
#             result = msg["result"]

#             if result.get("plan"):
#                 with st.expander("Generated Plan"):
#                     st.markdown(result["plan"])

#             st.subheader("Generated Implementation")
#             st.code(result.get("code", ""), language="python")

#             st.subheader("Execution-Based Evaluation")
#             evaluation = result.get("evaluation", {})
#             if evaluation.get("passed"):
#                 st.success("All validation tests passed")
#                 if evaluation.get("test_results"):
#                     df = pd.DataFrame(evaluation["test_results"])
#                     st.dataframe(df, use_container_width=True, hide_index=True)
#             else:
#                 st.error("One or more validation tests failed")
#                 if evaluation.get("error"):
#                     with st.expander("Execution Error"):
#                         st.code(evaluation["error"])

#             if result.get("review"):
#                 with st.expander("Static Code Review (Advisory)"):
#                     st.write(result["review"])

#             if result.get("explanation"):
#                 with st.expander("Explanation"):
#                     st.markdown(result["explanation"])

#             # ---------------- Metrics ----------------
#             with st.expander("System Metrics"):
#                 c1, c2, c3, c4 = st.columns(4)

#                 c1.metric(
#                     "Final Status",
#                     "PASSED" if result.get("passed") else "FAILED"
#                 )
#                 c2.metric("Retries", result.get("retries", 0))
#                 c3.metric(
#                     "Optimized",
#                     "Yes" if result.get("optimized") else "No"
#                 )

#                 confidence = compute_confidence(result)
#                 c4.metric("Agent Confidence", f"{confidence}%")

#             # ---------------- Severity ----------------
#             severity = detect_severity(result)
#             if severity == "CRITICAL":
#                 st.error("🚨 Severity: CRITICAL (Logic Failure)")
#             elif severity == "HIGH":
#                 st.warning("⚠️ Severity: HIGH (Syntax / Structural Issue)")
#             elif severity == "MEDIUM":
#                 st.info("ℹ️ Severity: MEDIUM (Execution Failure)")
#             else:
#                 st.success("✅ Severity: LOW")

#             # ---------------- DAG ----------------
#             with st.expander("Overall Agent Workflow (DAG)"):
#                 render_dag(result.get("logs", []))

#             # ---------------- Logs ----------------
#             with st.expander("Agent Execution Trace"):
#                 st.text("\n".join(result.get("logs", [])))

# # -------------------------------------------------
# # Chat Input
# # -------------------------------------------------
# prompt = st.chat_input("Type your problem here...")

# if prompt and not st.session_state.running:
#     st.session_state.running = True

#     st.session_state.messages.append({
#         "role": "user",
#         "content": prompt
#     })

#     with st.chat_message("assistant"):
#         status = st.empty()
#         status.text(" Agents are reasoning...")

#         initial_state = {
#             "problem": prompt,
#             "retries": 0,
#             "optimized": False,
#             "planner_called": False,
#             "logs": []
#         }

#         result = workflow_app.invoke(initial_state)

#         status.empty()
#         st.markdown("### ✅ Analysis Complete")

#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": "Here is the complete analysis and implementation.",
#         "result": result
#     })

#     st.session_state.running = False
#     st.rerun()
# above working------------------------


# import streamlit as st
# import pandas as pd
# from graph.workflow import app as workflow_app

# # -------------------------------------------------
# # Page Configuration
# # -------------------------------------------------
# st.set_page_config(
#     page_title="Multi-Agent Code System",
#     layout="wide"
# )

# # -------------------------------------------------
# # Custom CSS
# # -------------------------------------------------
# st.markdown(
#     """
#     <style>
#     .center-title {
#         text-align: center;
#         font-size: 2rem;
#         font-weight: bold;
#     }
#     .center-subtitle {
#         text-align: center;
#         color: white;
#         font-size: 1rem;
#         margin-bottom: 0.5rem;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # -------------------------------------------------
# # Header
# # -------------------------------------------------
# st.markdown("<h1 class='center-title'>⧈ Multi-Agent Code System</h1>", unsafe_allow_html=True)
# st.markdown(
#     "<div class='center-subtitle'>A Distributed AI Agent Framework for Backend Architecture Modeling</div>",
#     unsafe_allow_html=True
# )
# st.markdown("<hr>", unsafe_allow_html=True)

# # -------------------------------------------------
# # Session State
# # -------------------------------------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "running" not in st.session_state:
#     st.session_state.running = False

# # -------------------------------------------------
# # Utility Functions (FINAL)
# # -------------------------------------------------
# def compute_confidence(result: dict) -> int:
#     """
#     Confidence is based ONLY on execution outcome and retries.
#     Static review does NOT reduce confidence after execution success.
#     """
#     score = 100

#     if not result.get("passed"):
#         score -= 40

#     score -= result.get("retries", 0) * 10

#     return max(score, 0)


# def detect_severity(result: dict) -> str:
#     """
#     Execution is the source of truth.
#     Reviewer output is advisory only after pass.
#     """
#     passed = result.get("passed", False)
#     review = result.get("review", "")

#     if passed:
#         return "LOW"

#     if "LOGIC_FAIL" in review:
#         return "CRITICAL"

#     if "SYNTAX" in review:
#         return "HIGH"

#     return "MEDIUM"


# def render_dag(logs: list):
#     edges = [
#         ("Planner", "Generator"),
#         ("Generator", "Reviewer"),
#         ("Reviewer", "Evaluator"),
#         ("Evaluator", "Decision"),
#         ("Decision", "Generator"),
#         ("Decision", "Explainer")
#     ]

#     dot = "digraph Agents {\n"
#     dot += "rankdir=LR;\n"
#     dot += "node [shape=box, style=rounded];\n"

#     for src, dst in edges:
#         dot += f'"{src}" -> "{dst}";\n'

#     dot += "}\n"
#     st.graphviz_chart(dot)

# # -------------------------------------------------
# # Render Chat History
# # -------------------------------------------------
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

#         if msg["role"] == "assistant" and "result" in msg:
#             result = msg["result"]

#             # ---------------- Plan ----------------
#             if result.get("plan"):
#                 with st.expander("Generated Plan"):
#                     st.markdown(result["plan"])

#             # ---------------- Knowledge Base ----------------
#             with st.expander("📚 Knowledge Base / Technique Retrieval"):
#                 techniques = result.get("retrieved_techniques", [])

#                 if techniques:
#                     st.success(
#                         "Relevant techniques were retrieved from the database and used during planning."
#                     )
#                     for i, tech in enumerate(techniques, start=1):
#                         st.markdown(f"**{i}.** {tech}")
#                 else:
#                     st.info(
#                         "No relevant techniques were found in the database for this problem."
#                     )

#             # ---------------- Code ----------------
#             st.subheader("Generated Implementation")
#             st.code(result.get("code", ""), language="python")

#             # ---------------- Evaluation ----------------
#             st.subheader("Execution-Based Evaluation")
#             evaluation = result.get("evaluation", {})
#             if evaluation.get("passed"):
#                 st.success("All validation tests passed")
#                 if evaluation.get("test_results"):
#                     df = pd.DataFrame(evaluation["test_results"])
#                     st.dataframe(df, use_container_width=True, hide_index=True)
#             else:
#                 st.error("One or more validation tests failed")
#                 if evaluation.get("error"):
#                     with st.expander("Execution Error"):
#                         st.code(evaluation["error"])

#             # ---------------- Review ----------------
#             if result.get("review"):
#                 with st.expander("Static Code Review (Advisory)"):
#                     st.write(result["review"])

#             # ---------------- Explanation ----------------
#             if result.get("explanation"):
#                 with st.expander("Explanation"):
#                     st.markdown(result["explanation"])

#             # ---------------- Metrics ----------------
#             with st.expander("System Metrics"):
#                 c1, c2, c3, c4 = st.columns(4)

#                 c1.metric(
#                     "Final Status",
#                     "PASSED" if result.get("passed") else "FAILED"
#                 )
#                 c2.metric("Retries", result.get("retries", 0))
#                 c3.metric(
#                     "Optimized",
#                     "Yes" if result.get("optimized") else "No"
#                 )
#                 c4.metric(
#                     "Agent Confidence",
#                     f"{compute_confidence(result)}%"
#                 )

#             # ---------------- Severity ----------------
#             severity = detect_severity(result)
#             if severity == "CRITICAL":
#                 st.error("🚨 Severity: CRITICAL (Logic Failure)")
#             elif severity == "HIGH":
#                 st.warning("⚠️ Severity: HIGH (Syntax / Structural Issue)")
#             elif severity == "MEDIUM":
#                 st.info("ℹ️ Severity: MEDIUM (Execution Failure)")
#             else:
#                 st.success("✅ Severity: LOW")

#             # ---------------- DAG ----------------
#             with st.expander("Agent Workflow DAG"):
#                 render_dag(result.get("logs", []))

#             # ---------------- Logs ----------------
#             with st.expander("Agent Execution Trace"):
#                 st.text("\n".join(result.get("logs", [])))

# # -------------------------------------------------
# # Chat Input
# # -------------------------------------------------
# prompt = st.chat_input("Type your problem here...")

# if prompt and not st.session_state.running:
#     st.session_state.running = True

#     st.session_state.messages.append({
#         "role": "user",
#         "content": prompt
#     })

#     with st.chat_message("assistant"):
#         status = st.empty()
#         status.text("🧠 Agents are reasoning...")

#         initial_state = {
#             "problem": prompt,
#             "retries": 0,
#             "optimized": False,
#             "planner_called": False,
#             "logs": []
#         }

#         result = workflow_app.invoke(initial_state)

#         status.empty()
#         st.markdown("### ✅ Analysis Complete")

#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": "Here is the complete analysis and implementation.",
#         "result": result
#     })

#     st.session_state.running = False
#     st.rerun()




import streamlit as st
import pandas as pd
from graph.workflow import app as workflow_app

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Multi-Agent Code System",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------
st.markdown(
    """
    <style>
    .center-title {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
    }
    .center-subtitle {
        text-align: center;
        color: white;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown("<h1 class='center-title'>⧈ Multi-Agent Code System</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='center-subtitle'>A Distributed AI Agent Framework for Backend Architecture Modeling</div>",
    unsafe_allow_html=True
)
st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------
# Session State
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "running" not in st.session_state:
    st.session_state.running = False

# -------------------------------------------------
# ✅ Utility Functions
# -------------------------------------------------
def compute_confidence(result: dict) -> int:
    score = 100
    if not result.get("passed"):
        score -= 40
    score -= result.get("retries", 0) * 10
    return max(score, 0)


def detect_severity(result: dict) -> str:
    passed = result.get("passed", False)
    review = result.get("review", "")

    if passed:
        return "LOW"
    if "LOGIC_FAIL" in review:
        return "CRITICAL"
    if "SYNTAX" in review:
        return "HIGH"
    return "MEDIUM"


def render_dag(logs: list):
    edges = [
        ("Planner", "Generator"),
        ("Generator", "Reviewer"),
        ("Reviewer", "Evaluator"),
        ("Evaluator", "Decision"),
        ("Decision", "Generator"),
        ("Decision", "Explainer")
    ]

    dot = "digraph Agents {\n"
    dot += "rankdir=LR;\n"
    dot += "node [shape=box, style=rounded];\n"

    for src, dst in edges:
        dot += f'"{src}" -> "{dst}";\n'

    dot += "}\n"
    st.graphviz_chart(dot)

# -------------------------------------------------
# Render Chat History
# -------------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

        if msg["role"] == "assistant" and "result" in msg:
            result = msg["result"]

            if result.get("plan"):
                with st.expander("Generated Plan"):
                    st.markdown(result["plan"])

            st.subheader("Generated Implementation")
            st.code(result.get("code", ""), language="python")

            st.subheader("Execution-Based Evaluation")
            evaluation = result.get("evaluation", {})
            if evaluation.get("passed"):
                st.success("All validation tests passed")
                if evaluation.get("test_results"):
                    df = pd.DataFrame(evaluation["test_results"])

                    # ✅ FIX: convert lists to strings to avoid PyArrow errors
                    for col in df.columns:
                        df[col] = df[col].apply(lambda x: str(x) if isinstance(x, list) else x)

                    st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.error("One or more validation tests failed")
                if evaluation.get("error"):
                    with st.expander("Execution Error"):
                        st.code(evaluation["error"])

            if result.get("review"):
                with st.expander("Static Code Review (Advisory)"):
                    st.write(result["review"])

            if result.get("explanation"):
                with st.expander("Explanation"):
                    st.markdown(result["explanation"])

            # ---------------- Metrics ----------------
            with st.expander("System Metrics"):
                c1, c2, c3, c4 = st.columns(4)

                c1.metric(
                    "Final Status",
                    "PASSED" if result.get("passed") else "FAILED"
                )
                c2.metric("Retries", result.get("retries", 0))
                c3.metric(
                    "Optimized",
                    "Yes" if result.get("optimized") else "No"
                )

                confidence = compute_confidence(result)
                c4.metric("Agent Confidence", f"{confidence}%")

            # ---------------- Severity ----------------
            severity = detect_severity(result)
            if severity == "CRITICAL":
                st.error("🚨 Severity: CRITICAL (Logic Failure)")
            elif severity == "HIGH":
                st.warning("⚠️ Severity: HIGH (Syntax / Structural Issue)")
            elif severity == "MEDIUM":
                st.info("ℹ️ Severity: MEDIUM (Execution Failure)")
            else:
                st.success("✅ Severity: LOW")

            # ---------------- DAG ----------------
            with st.expander("Overall Agent Workflow (DAG)"):
                render_dag(result.get("logs", []))

            # ---------------- Logs ----------------
            with st.expander("Agent Execution Trace"):
                st.text("\n".join(result.get("logs", [])))

# -------------------------------------------------
# Chat Input
# -------------------------------------------------
prompt = st.chat_input("Type your problem here...")

if prompt and not st.session_state.running:
    st.session_state.running = True

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("assistant"):
        status = st.empty()
        status.text(" Agents are reasoning...")

        initial_state = {
            "problem": prompt,
            "retries": 0,
            "optimized": False,
            "planner_called": False,
            "logs": []
        }

        result = workflow_app.invoke(initial_state)

        status.empty()
        st.markdown("### ✅ Analysis Complete")

    st.session_state.messages.append({
        "role": "assistant",
        "content": "Here is the complete analysis and implementation.",
        "result": result
    })

    st.session_state.running = False
    st.rerun()

