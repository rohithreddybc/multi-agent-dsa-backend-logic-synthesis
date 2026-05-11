# Legacy archive

The files in this directory belong to the **pre-IEEE-Access-revision** version of the codebase. They are kept here so reviewers can see the migration history; **do not depend on them for new work**.

| Legacy path | Replaced by |
|-|-|
| `app.py` | `execugraph/ui/streamlit_app.py` (cleaned-up; ~470 lines of commented-out blocks removed) |
| `agents/planner_agent.py` | `execugraph/agents/planner.py` |
| `agents/generate_agent.py` | `execugraph/agents/generator.py` |
| `agents/review_agent.py` | `execugraph/agents/reviewer.py` (now structured JSON output) |
| `agents/evaluator_agent.py` | `execugraph/agents/evaluator.py` (sandboxed; ~700 lines of commented-out blocks removed) |
| `agents/optimizer_agent.py` | `execugraph/agents/optimizer.py` (now re-evaluates before accepting) |
| `agents/explainer_agent.py` | `execugraph/agents/explainer.py` |
| `agents/single_agent/` | `execugraph/pipelines/single_oneshot.py` (now an integrated baseline) |
| `agents/technique_selector_agent.py` | **deleted** — was never invoked |
| `graph/workflow.py` | `execugraph/graph/workflow.py` (parameterized) + `execugraph/graph/routing.py` |
| `memory/technique_store.py` | `execugraph/memory/technique_store.py` (chromadb optional) |
| `memory/seed_techniques.py` | `execugraph/memory/seed_techniques.py` (TODO: pending re-add for ablation runs) |
| `memory/technique_selector.py` | **deleted** — was never invoked |
| `memory/vector_store.py` | **deleted** — wrong paths, superseded |
| `memory/technique_retriever.py` | folded into `execugraph/memory/technique_store.TechniqueRetriever` |
| `util/llm.py` | `execugraph/llm/{base,ollama_backend,hf_backend,factory}.py` |
| `util/code_sanitize.py` | `execugraph/execution/code_sanitize.py` |
| `util/code_extractor.py` | folded into `execugraph/execution/code_sanitize.extract_python_block` |
| `test_*.py` (top-level smoke scripts) | `tests/unit/*.py` (pytest, with assertions) |
| `Prompts/*.txt` | `execugraph/prompts/*.txt` (packaged as data) |
| `requirements.txt` | `pyproject.toml` (`pip install -e .`) |

Once the IEEE Access revision is accepted, this archive will be removed in version 0.3.0.
