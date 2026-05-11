# Overall change log — IEEE Access revision

## Revision 6 — Experiment completion + full paper finalization (2026-05-11)

### Grid completed
- Full experiment grid ran to completion on reference hardware (RTX 4050, Ollama, local quantized models).
- 1,335 trial records in `results/submission-20260509-223437/` across 17 condition directories (E1 SO/SR/MF, E2 HumanEval SO/MF, E3 APPS SO/MF, E4 ablations ×4, E5 retry sweep ×2, E7 cross-model SO/MF, E9 Qwen3-Coder supplementary SO/MF).

### Tables — all filled with real data
- **Tab 3** regenerated with internal-30-only filter (30 rows, DP/Graph/DS grouped with `\midrule` separators, APPS-adapted problems marked with `†`).
- **Tab 7 (ablation)**, **Tab 8 (retry sweep)**, **Tab 9 (external)**, **Tab 10 (cross-model)**, **Tab 12 (test-source)** — all previously stubs, now filled with real numbers.
- `build_tables.py` updated: `_table_header_problem_level` now filters to internal-30 only (category ∈ {DP, GRAPH, DS}) and sorts by category; source column shows "internal" vs "APPS†" cleanly.

### Figures added
- `figures/architecture_layered.tex` — new TikZ recreation of the 5-layer architecture (replaces old `architecture.pdf`). Compiled to `architecture_layered.pdf`.
- `figures/workflow_dag.tex` — new TikZ recreation of the workflow DAG with retry arrow, RAG path, and SharedGraphState panel. Compiled to `workflow_dag.pdf`.
- Both integrated into `main.tex`: architecture figure in §III.A, workflow DAG in §III.B with cross-reference.

### Problem categories table added
- New `\label{tab:internal30}` in §IV.A (Datasets) lists all 30 internal-30 problems by category (DP/Graph/DS) with IDs, descriptions, and APPS-adapted markers. Replaces the preprint's Table 2.

### Honest reporting of key negative finding
- **Abstract rewritten**: removed false claim that MF beats both baselines on DP and Graph. New abstract accurately states SR (83.3%) > MF (76.7%) on internal-30 and attributes it to 7B-scale planner noise.
- **Discussion §VI.A rewritten**: "Execution Feedback vs. Multi-Agent Decomposition" — explains SR > MF, Planner ablation finding, and the model-scale hypothesis (DeepSeek cross-model graph: 57.5%→80.0% with MF).
- **Discussion §VI.C (RAG)** rewritten: ablation shows no measurable effect at 2 trials; no inflation claimed.

### Model name fix
- `deepseek-coder:6.7b` → `deepseek-coder-v2:16b-lite-instruct-q4_K_M` corrected throughout paper and appendix.

### Test-source bias resolved
- Tab 12 confirms all 614 trial records used deterministic tests; LLM-generated-test fallback was not triggered on any benchmark. Discussion text updated to report this directly.

### Retry budget sweep text fixed
- Paper previously claimed sweep over {0,1,2,3}; corrected to {0,2} throughout (abstract, contribution bullet, experiment protocol, retry subsection).

### READINESS.md updated
- Reflects completed grid, all-real-data tables, single remaining item (corresponding-author email).

---

## Revision 5 (autonomous polish pass)

- **Preview pipeline**: `scripts/build_preview.sh` produces `paper_preview/main.pdf` with a watermark and synthetic data so the layout can be inspected without compute.
- **RAG ablation row now executable**: 69 algorithmic techniques ported into `execugraph/memory/TECHNIQUES.py`; `python -m execugraph.memory.seed_techniques` seeds ChromaDB.
- **Streamlit UI ported** from the legacy archive onto the new package. ~470 lines of dead-code-from-history dropped.
- **HumanEval+ and MBPP loaders** added (peer-review W7 contamination response is now executable, not just discussed).
- **Ruff lint clean** across the whole `execugraph/` and `tests/` tree; 38 tests passing (up from 35).
- **`CITATION.cff`** with all four authors.

## Revision 4 (benchmarks + e2e tests + result-side figures)

- **HumanEval and APPS-introductory loaders** added (`execugraph/benchmarks/humaneval.py`, `apps_intro.py`). The §IV.A external-validity claim is now executable; CLI gains `--benchmark` flag.
- **Stub LLM backend + 4 integration tests.** The multi-agent pipeline can now be exercised end-to-end without Ollama or HF credentials. Total test count: **35 passing** (31 unit + 4 integration).
- **`build_figures.py`** companion to `build_tables.py` emits 3 PDFs (category-level bar, cost-vs-accuracy scatter, retry convergence). Paper now references all three via `\IfFileExists{}` so the document compiles whether or not the experiments have been run.
- **`scripts/run_full_grid.sh`** extended to drive HumanEval + APPS-introductory and to build figures alongside tables.
- Paper unchanged at 10 pages; `\IfFileExists` keeps the compile clean.

## Revision 3 (4-author block + new figures)

- **Authors are now four:** A. Jothi Prabha (corresponding) | L. Sai Deekshith | Rohith Reddy Bellibatlu | G. Suganeshwari. The previously-removed third author from the original draft (G. Suganeshwari, VIT Chennai) is reinstated at position 4 per the user's instruction; corresponding-author identity and email convention are preserved exactly.
- **New Algorithm 1** in §III.B specifies the run loop in pseudocode (init → optional plan → generate-review-evaluate-retry loop → optional optimize+revalidate → explain).
- **New Listing 1** in §III.D shows a real per-agent execution trace on `topo_sort`, concretizing the data flow.
- **Paper grew from 9 to 10 pages.** All compile / audit / test gates remain green.

## Revision 2 (model upgrade + JudgeSense)

- **Default models upgraded.** Non-code agents now use `qwen3:4b-instruct-2507-q4_K_M` (Apache-2.0; July 2025; ~2.5 GB) instead of Qwen2.5-7B; code agents stay on the proven `qwen2.5-coder:7b-instruct-q4_K_M`. Net result: faster headline runs, more VRAM headroom for KV cache, and a more recent backbone for the paper. Zero paid-API cost.
- **Cross-model condition rewritten** to be an independent vendor family: `llama3.1:8b-instruct-q4_K_M` + `deepseek-coder-v2:16b-lite-instruct-q4_K_M` (16B MoE, 2.4B active). Stronger generalization signal than the previous same-family DeepSeek-Coder-6.7B swap.
- **`configs/strong.yaml` added** — opt-in stronger generator using `qwen3-coder:30b-a3b-instruct-q4_K_M` (MoE, 3B active). Slow but substantially more capable; runnable on the laptop with RAM offload.
- **JudgeSense cited and integrated.** The paper now references `arXiv:2604.23478` four times: §II.B (motivates advisory-only Reviewer), §III.C (Reviewer agent description), §VI (Discussion → Reviewer's role), §VII (future work — measure Reviewer JSS). Author list is currently double-blind in the source; will be de-anonymised at camera-ready (note recorded in `references.bib`).
- **Paper grew from 8 to 9 pages.** All compile / audit / test gates remain green.

---

## Revision 1 — IEEE Access conversion

This file summarises everything that changed in the paper, the code, and the experiments
during the IEEE Access revision pass. Per-side detail lives in:

- `paper/CHANGELOG.md` — every paper-side change with peer-review point map.
- `_repo_clone/CHANGELOG.md` — every code-side change.

---

## Paper

- Converted `research_paper_4-draft.docx` to IEEE LaTeX (`paper/main.tex`, `paper/sections/0X_*.tex`, `paper/references.bib`). Compiles to 8 pages with `pdflatex` + `bibtex`. One-line swap-in to the official `ieeeaccess.cls` documented in `main.tex`.
- Authorship: third author replaced with **Rohith Reddy Bellibatlu**. Corresponding author preserved as A. Jothi Prabha. No AI tool listed anywhere as author / contributor / acknowledgement / citation.
- Corresponding-author email left as `\todo{}` (was not present in the original `.docx`).
- Section II rewritten into five positioned strands (LLMs for code; iterative refinement; multi-agent pipelines; execution-grounded validation; RAG for code), each ending with a one-sentence "how ExecuGraph differs".
- Section III.B replaced the six textbook recurrences with a typed transition-system formalism. The decision predicate is now defined explicitly over execution outcomes; baselines are stated as configurations of the same workflow.
- Section IV.B introduces the **single-with-retry** Reflexion-style baseline so the contribution of the multi-agent decomposition can be isolated from the contribution of execution feedback per se (peer-review W5).
- Section IV.E now reports cost (wallclock / tokens / LLM calls) (peer-review W3).
- Section IV.F runs paired Wilcoxon and McNemar with bootstrap 95% CI (peer-review W8).
- New tables: per-agent ablation, retry-budget sweep, HumanEval / APPS-introductory, cross-model (DeepSeek-Coder-6.7B), error taxonomy, test-source split.
- New "Reproducibility" section enumerates exact commands, model digests, seeds, and runtime estimates.

## Code

- Restructured the loose top-level modules into a proper `execugraph/` package (`pyproject.toml`-installable).
- New provider-agnostic `execugraph/llm/` layer: local Ollama (default, restores the paper's "locally hosted" reproducibility claim) and HuggingFace Inference API fallback. Both record token / wallclock / call-count cost.
- New subprocess-isolated execution sandbox (`execugraph/execution/sandbox.py`) replaces the prior raw `exec()` / `eval()` in the evaluator. Wall-clock timeout, restricted `__builtins__`, allow-listed imports.
- Single source-of-truth benchmark in `execugraph/benchmarks/internal30.py`: 30 problems (10 DP + 10 graph + 10 DS, 27 internal + 3 APPS-introductory), each with explicit selection rationale, signature aliases, and deterministic test cases. Addresses peer-review W1.
- Three pipeline conditions (`single-oneshot`, `single-with-retry`, `multi-full`) plus four ablation toggles (`–planner`, `–reviewer`, `–optimizer`, `+rag`).
- Trial / batch / CLI runner in `execugraph/runner/`. Per-trial JSONL log captures every field needed by the paper tables.
- `execugraph/analysis/`: paired Wilcoxon, McNemar, bootstrap CI; LaTeX table builder that drops fragments into `paper/tables/`.
- Optimizer now re-evaluates the candidate before accepting (peer-review T1).
- Reviewer now emits structured JSON `{invariants, potential_failures, severity}` (peer-review Q4).
- `MAX_RETRIES` is no longer hardcoded; budget is a per-run config field (peer-review T4).
- `tests/unit/` pytest suite (31 tests) covering sandbox safety, code sanitiser, problem loader, evaluator behaviour, cost tracker, routing predicate, and table-builder smoke. **All 31 tests pass.**
- GitHub Actions CI runs lint + unit tests on every push.
- `Dockerfile`, `REPRODUCIBILITY.md`, `CHANGELOG.md`, and a synthetic `results/example_run/` (clearly labelled, not for citation).
- ~1000 lines of dead / commented-out code retired; legacy modules moved to `_legacy_archive/` with a migration map.

## Peer-review points addressed

| Point | Status |
|-|-|
| W1 small/biased benchmark | Addressed: HumanEval + APPS-intro added; selection rationale per problem. |
| W2 single-model | Addressed: cross-model condition with DeepSeek-Coder-6.7B. |
| W3 missing cost analysis | Addressed: Table~\ref{tab:cost}; cost recorded per trial. |
| W4 incomplete ablation | Addressed: per-agent ablation + retry-budget sweep + RAG on/off. |
| W5 no comparison vs iterative methods | Addressed: single-with-retry (Reflexion-lite) baseline. |
| W6 RAG not evaluated | Addressed: explicit on/off ablation. |
| W7 contamination | Addressed: discussed in Limitations; HumanEval/APPS as anchor. |
| W8 statistical tests | Addressed: paired Wilcoxon + McNemar + bootstrap CI. |
| T1 Optimizer regression | Addressed: optimizer re-evaluates before accepting. |
| T2 test-source bias | Addressed: split-by-source table. |
| T3 Planner effectiveness | Addressed: ablation row. |
| T4 retry convergence | Addressed: budget sweep. |
| T5 error categorization | Addressed: error-class taxonomy table. |
| P1, P2, P3, P4 | All addressed. |
| Minor 1–5 | All addressed. |
| Q1–Q5 | Addressed in Limitations / Discussion / Reviewer schema / ablations. |

## Remaining open items

- **Numerical cells in Tables 3–10 are `\todo{}` placeholders.** They will be filled automatically the first time `scripts/run_full_grid.sh` is run on the reference RTX 4050 hardware (~30–45 h wallclock). Until then, the paper compiles but the result tables show TODO markers in red.
- **Corresponding-author email.** Left as `\todo{}`. The original `.docx` did not include it; we did not invent one.
- **Streamlit UI** in the new package is referenced but not yet ported from the legacy `_legacy_archive/app.py`; legacy version still runs but is not part of the experimental measurement loop. Out of scope for the IEEE Access numbers.
- **Top-level `seed_techniques.py`** (used to populate the optional ChromaDB) was migrated as a stub; the original technique list is still in `_legacy_archive/memory/TECHNIQUES.py`. Reseeding will only matter for the RAG ablation row.
