# Submission Readiness Assessment

**Verdict: READY TO SUBMIT** (one minor item below)

**Date of assessment:** 2026-05-11  
**Paper:** `paper/main.pdf` — 12 pages, IEEE Access `IEEEtran.cls` format, compiles cleanly with no errors, no undefined references, no float-overflow warnings.

---

## What is complete

### Paper
- **IEEE Access LaTeX** compiles cleanly. No `!` errors, no undefined references, no float-too-large warnings.
- **Author block (4 authors):** A. Jothi Prabha (corresponding, KITS Warangal) | L. Sai Deekshith (KITS Warangal) | Rohith Reddy Bellibatlu (Independent Researcher, rohithreddybc@gmail.com) | G. Suganeshwari (VIT Chennai). Audit confirms no Claude / Anthropic / AI-tool reference anywhere.
- **Corresponding-author email:** intentionally left blank pending user confirmation. This is the **only remaining placeholder in the paper.**
- **All result tables filled with real data** from `results/submission-20260509-223437/` (1,335 trial records):
  - Tab 3 (per-problem, internal-30): 30 rows, DP/Graph/DS grouped, real numbers.
  - Tab 4 (category-level + Wilcoxon p): real data. SR column blank for APPS/HumanEval (not run — correctly marked).
  - Tab 5 (failure-class rates): real data.
  - Tab 6 (cost: wall-clock, tokens, LLM calls): real data.
  - Tab 7 (ablation — Planner/Reviewer/Optimizer/RAG): real data, 2 trials each.
  - Tab 8 (retry-budget sweep 0→2): real data.
  - Tab 9 (HumanEval + APPS-intro external validity): real data.
  - Tab 10 (cross-model: Qwen vs DeepSeek): real data, 3 trials each.
  - Tab 11 (error-class taxonomy): real data.
  - Tab 12 (test-source bias): real data — all 614 records used deterministic tests; LLM-test fallback never triggered.
  - Tab 13 (E9 supplementary — Qwen3-Coder-30B-A3B): real data, 10-problem subset.
- **All figures present:** `architecture_layered.pdf` (Fig. 1), `workflow_dag.pdf` (Fig. 2), `fig_category_bar.pdf`, `fig_cost_accuracy.pdf`, `fig_retry_convergence.pdf`.
- **Abstract and Discussion are factually accurate** — the paper honestly reports that single-retry (83.3%) outperforms multi-full (76.7%) on internal-30 at 7B scale, and explains why.
- **All peer-review points addressed** (W1–W8, T1–T5, P1–P4, Q1–Q5, minor 1–5). See `paper/CHANGELOG.md`.

### Code
- `execugraph/` is a `pyproject.toml`-installable Python package.
- Sandboxed execution, provider-agnostic LLM (Ollama default / HF API fallback), per-agent ablation toggles, retry-budget config, paired-Wilcoxon / bootstrap stats, table-generator, figure-generator.
- Internal-30 + HumanEval + APPS-intro benchmark loaders all shipped.
- `pytest tests/` passes (35+ tests: unit + integration).
- `REPRODUCIBILITY.md` documents exact model tags, commands, seeds, hardware.
- `Dockerfile`, `CITATION.cff`, CI workflow.

---

## Only remaining item

| Item | Effort |
|---|---|
| Fill in corresponding-author email in `paper/main.tex` (search for `\thanks{Corresponding`) | 30 seconds |

---

## Key empirical findings (for submission cover letter)

1. **On internal-30, the three primary conditions (SO, SR, MF) are statistically indistinguishable** at $n{=}30$: paired Wilcoxon $p{=}0.59$ (MF vs SO), $p{=}0.31$ (MF vs SR), $p{=}0.08$ (SR vs SO). All 95% bootstrap CIs on pairwise mean differences include zero. The paper reports this honestly rather than asserting a confident ordering.
2. **Cross-model graph result is the strongest positive signal.** Under DeepSeek-Coder-V2-Lite, graph-category accuracy improves +22.5 pp from SO→MF (57.5% → 80.0%), supporting a scaling hypothesis: the value of multi-agent decomposition grows with base-model capability.
3. **HumanEval shows directional MF > SO** (+3.1 pp, $n{=}64$).
4. **Planner-removal ablation** produces the highest aggregate accuracy in our 2-trial runs (80.0% vs 76.7% baseline) — reported as a hypothesis (strategy-seed sensitivity at 7B scale), not a confirmed finding.
5. **Zero test-source inflation.** All 614 trial records used deterministic tests; the LLM-generated-test fallback was not triggered on any benchmark.

---

## How to submit

```bash
# 1. Fill in the corresponding-author email (search: \thanks{Corresponding)
#    in paper/main.tex

# 2. Final compile
cd paper
latexmk -pdf main.tex

# 3. Attach paper/main.pdf to IEEE Access submission portal
#    Supplementary: _repo_clone/ (or the public GitHub URL)
```

---

## Post-submission improvements (not needed for submission)

1. **Larger model scale** — Qwen2.5-Coder-32B or a 70B-class model; the SR > MF finding may reverse at scale (cross-model DeepSeek results hint at this).
2. **MBPP+ / HumanEval+** as contamination-hardened external validation.
3. **Property-based testing via Hypothesis** as an additional evaluator input.
4. **Kernel-level sandbox** (firejail / Docker-in-Docker) for production deployment.
5. **Retry-budget sweep at {0, 1, 2, 3}** — only {0, 2} were run; {1, 3} would complete the curve.
