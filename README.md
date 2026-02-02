# Multi-Agent Framework for Reliable DSA-Driven Backend Logic Synthesis
### Execution-Verified Code Generation using Large Language Models

> **TL;DR**  
> This project investigates whether structured multi-agent orchestration with execution-based
> validation can improve the reliability of LLM-generated backend algorithms compared to
> single-pass generation. Correctness is enforced through runtime execution and testing,
> not textual self-review.

---

## Overview

Large Language Models (LLMs) have demonstrated strong capabilities in automated code generation.
However, most existing systems rely on **single-agent, single-pass generation**, which often fails
in scenarios requiring strict logical correctness—particularly in **data structure and algorithm
(DSA)–driven backend systems**, where determinism, efficiency, and edge-case handling are critical.

This project proposes a **multi-agent framework** for backend logic synthesis, verification, and
optimization using LLMs. The system decomposes code generation into **specialized agents**,
orchestrated through a deterministic workflow graph.

Unlike prior approaches, **correctness is enforced through execution and testing**, rather than
relying on textual self-evaluation. All experiments are **fully reproducible** using locally hosted
LLMs, making the system suitable for academic research and evaluation.

---

## Research Motivation

Despite producing syntactically valid code, LLMs frequently:

- hallucinate incorrect logic  
- miss edge cases  
- generate inefficient implementations  
- falsely validate incorrect solutions via self-review  

This project is motivated by the following research question:

> **Can structured multi-agent orchestration with execution-based validation improve the reliability
> of LLM-generated backend algorithms compared to single-pass generation?**

---

## Key Contributions

- Multi-agent decomposition of backend algorithm generation  
- Execution-first correctness validation (runtime > text)  
- Hybrid evaluation agent (deterministic + LLM-generated tests)  
- Retry-controlled workflow using LangGraph  
- Transparent state propagation and debugging  
- Empirical comparison with single-agent baselines  
- Optional algorithm memory for technique and pattern retrieval  
- Fully local and reproducible LLM execution  

---

## System Architecture Overview

The framework consists of specialized agents, each responsible for a well-defined role:

### Planner Agent
- Classifies problem type (Dynamic Programming, Graph, Data Structure, etc.)
- Selects appropriate algorithmic strategy
- Produces structured reasoning
- Optionally retrieves relevant techniques and patterns from a local vector database

### Code Generation Agent
- Converts plans into deterministic Python code
- Uses low-temperature generation for stability

### Review Agent (Advisory)
- Performs static logical inspection
- Identifies potential flaws (non-authoritative)

### Evaluation Agent (Core Authority)
- Executes code in a controlled environment
- Validates correctness using test cases  
- Hybrid testing approach:
  - deterministic tests for known DSA problems  
  - LLM-generated tests for unseen or open-ended cases  

### Decision Agent
- Routes workflow based on execution outcome
- Controls retries and termination

### Optimization Agent
- Improves time and memory efficiency
- Runs only after correctness is empirically verified

### Explanation Agent
- Generates human-readable algorithm explanations

Workflow orchestration is implemented using **LangGraph**, enabling deterministic execution paths,
bounded retries, and explicit state transitions.

---

## Algorithm Memory (Technique Store)

The system optionally incorporates an **algorithm memory module**, implemented as a vector database:

- Stores common DSA techniques, patterns, and strategies
- Retrieved by the Planner Agent when applicable
- Enables reuse of known algorithmic approaches
- Reduces hallucinated or inconsistent planning decisions

This component is modular and can be enabled or disabled without affecting the core workflow.

---

## Evaluation Methodology

### Multi-Agent Evaluation
- Code is executed, not just reviewed
- Runtime errors or incorrect outputs trigger regeneration
- Final acceptance depends solely on execution success

### Single-Agent Baseline
- One-pass LLM generation
- No execution feedback
- No retries or optimization

This contrast highlights the reliability gap between single-agent and execution-verified
multi-agent systems.

---

## Experimental Problem Set

| Category | Problem |
|--------|--------|
| Dynamic Programming | Climbing Stairs |
| Graph Algorithms | Task Dependency Resolution (Topological Sort) |
| Data Structures | LRU Cache (O(1) operations) |

Each problem was solved using:
- a single-agent LLM baseline
- the proposed multi-agent framework

Screenshots of execution results, evaluation traces, and agent workflows are included.

---

## Project Structure

```
Multi-Agent-Project/
│
├── agents/
│   ├── planner_agent.py
│   ├── generate_agent.py
│   ├── review_agent.py
│   ├── evaluator_agent.py      # Hybrid execution-based evaluator
│   ├── optimizer_agent.py
│   ├── explainer_agent.py
│   └── single_agent/
│       ├── run_single_agent.py # Baseline comparison
│       └── single_agent.py
│
├── graph/
│   └── workflow.py             # LangGraph orchestration
│
├── memory/                     # Optional algorithm memory module
│   ├── technique_store.py
│   ├── technique_retriever.py
│   ├── seed_techniques.py
│   └── TECHNIQUES.py
│
├── models/
│   └── all-MiniLM-L6-v2         # Embedding model (download if memory enabled)
│
├── prompts/
│   ├── planner.txt
│   ├── generator.txt
│   ├── review.txt
│   ├── evaluator.txt
│   ├── explain.txt
│   └── optimizer.txt
│
├── screenshots/
│   ├── single_agent/
│   └── multi_agent/
│
├── util/
│   ├── llm.py
│   ├── code_extractor.py
│   └── code_sanitize.py
│
├── app.py                      # Streamlit interface
├── requirements.txt
└── README.md
```

---

## Technology Stack

- Python  
- LangChain  
- LangGraph  
- Ollama (local LLM inference)  
- Streamlit  
- FastAPI (optional)  
- ChromaDB (optional algorithm memory)  

---

## LLM Configuration (Reproducible)

All models are run locally via Ollama.

| Role | Model |
|----|----|
| Planner / Reviewer / Explainer | `qwen2.5:7b-instruct` |
| Generator / Optimizer | `qwen2.5-coder:7b-instruct` |

---

## How to Run

```bash
pip install -r requirements.txt
ollama serve
```

### Streamlit UI
```bash
streamlit run app.py
```

### Single-Agent Baseline
```bash
python -m agents.single_agent.run_single_agent
```

---

## Screenshots (Evidence of Evaluation)

```
screenshots/
├── single_agent/
│   ├── q1_dp.png
│   ├── q2_graph.png
│   └── q3_lru.png
└── multi_agent/
    ├── q1_dp_eval.png
    ├── q2_graph_eval.png
    └── q3_lru_eval.png
```

These screenshots demonstrate:
- execution-based correctness enforcement  
- retry and regeneration behavior  
- optimization improvements  
- failure modes of single-agent generation  

---

## Academic Relevance

This project aligns closely with research interests in:

- Trustworthy AI  
- Agentic LLM Systems  
- Automated Software Engineering  
- Execution-Verified Code Generation  

Relevant programs:
- MScAC (AI) – University of Toronto  
- MSc AI / CS – University of Zurich  

---

## Future Work

- Automatic test generation with coverage guarantees  
- Formal verification integration  
- Cross-language backend support  
- Larger model benchmarking (32B+ LLMs)  
- Secure sandboxed execution environments  

---

## Author

**L. Sai Deekshith**  
AI / ML Research-Focused Developer  

**Interests:**  
Agentic AI · Generative AI ·  Reliable & Fine-Tuned LLMs · Code Generation Systems · Backend Engineering · Trustworthy ML & DL
