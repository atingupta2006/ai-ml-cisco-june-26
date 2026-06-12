# Day 01 — Labs

**Theme:** Data Science Introduction | **Lab time (6 labs):** ~435 min (~7.2 h)

**Execution guide:** [docs/lab-execution-guide.md](../../docs/lab-execution-guide.md) — read before Lab 1.

**Recommended order:** `lab01` → `lab02` → `lab03` → `lab04` → `lab05` → `lab06` (one narrative arc on `team_sales.csv`).

---

## Before every lab

**Environment:** one venv for all days — run `setup_student_env.ps1` (Windows) or `setup_student_env.sh` (Linux/Mac) once at repo root. See [lab execution guide](../../docs/lab-execution-guide.md). Jupyter kernel: **Python (cisco-aiml-lab)**.

Labs 1, 2, and 5 are **discussion / worksheet** activities (light code).

Labs 3, 4, and 6 are **hands-on** on [`data/team_sales.csv`](data/team_sales.csv) (**20** rows) — use **Excel and/or the Jupyter notebook** (notebooks are the primary path). Lab 6 is a **group Excel activity** with Python verification in the notebook.

> **Note:** The `` folder is trainer-only and not part of the student handout.

---

## Expected outcomes

| After lab | Check |
|-----------|--------|
| Lab 1 | Worksheet: AI ⊃ ML ⊃ DS nesting correct |
| Lab 2 | Worksheet: all six CRISP-DM phases named |
| Lab 3 | Mean q2_sales ≈ **150.30**; regional tables; outlier analysis |
| Lab 4 | Growth rate (q2 > q1) = **0.75**; sampling distribution explored |
| Lab 5 | Worksheet: 3+ categories with 2+ tools each; CRISP-DM tool map |
| Lab 6 | **15** teams grew; top region **North**; % growth story for East |

## Lab pacing

| Lab | Est. time |
|-----|-----------|
| Lab 1 | ~30 min |
| Lab 2 | ~30 min |
| Lab 3 | ~90 min |
| Lab 4 | ~100 min |
| Lab 5 | ~75 min |
| Lab 6 | ~110 min |
| **Total** | **~435 min** |

---

# Lab 1 — AI vs ML vs DS

## Objective

Distinguish Artificial Intelligence, Machine Learning, and Data Science using the Netflix-style use-case from the morning session.

**Estimated time:** ~30 min

## Lab flow

```text
  instructor use-case → Venn diagram → worksheet definitions → group share-out
```

## Tasks

1. Open `notebooks/lab01_ai_ml_ds.ipynb` (recommended) or complete the worksheet on paper.
2. Draw three nested circles: **AI** (outer), **ML** (middle), **Data Science** (inner, overlapping ML).
3. Place **Netflix recommendation** in the ML ring; place **dashboard reporting** in DS but outside ML.
4. Write one-sentence definitions for AI, ML, and DS in your worksheet.
5. Give one example of each that is **not** the Netflix case.

## Success criteria

* Worksheet completed with nested relationship (AI ⊃ ML; DS overlaps ML).
* At least one original example per term.

---

# Lab 2 — Data science cycle

## Objective

Map the CRISP-DM / data science lifecycle phases to a business problem your table chooses.

**Estimated time:** ~30 min

## Tasks

1. Open `notebooks/lab02_data_science_cycle.ipynb`.
2. Pick a business question (e.g. "Which store region had highest Q2 sales?").
3. Fill in all six CRISP-DM phases with activity and deliverable.
4. Identify phases that apply without ML.

## Success criteria

* All **six** phases named in order.
* Each phase has an activity and deliverable.

---

# Lab 3 — Statistics basics

## Objective

Deep descriptive statistics on Q2 team sales — Excel **and** pandas, with regional and outlier analysis.

**Estimated time:** ~90 min

## Tasks

1. Open `notebooks/lab03_statistics_basics.ipynb`.
2. Mirror Excel formulas (`AVERAGE`, `MEDIAN`, `STDEV.S`, `AVERAGEIF`) in pandas.
3. Measure Team_13 outlier impact; apply IQR rule; plot distributions.
4. Aggregate by region; rank teams by % growth.

## Example result

```text
mean q2_sales: 150.30 | median: 148.50 | std: 34.74
top outlier: Team_13 (210)
```

## Success criteria

* Mean ≈ **150.30** and median ≈ **148.50**.
* Regional table sums to **20** teams.
* You can explain mean vs median with Team_13 example.

---

# Lab 4 — Hypothesis & sampling

## Objective

Population vs sample, growth hypothesis, regional proportions, and sampling variation.

**Estimated time:** ~100 min

## Tasks

1. Open `notebooks/lab04_hypothesis_sampling.ipynb`.
2. State H₀ / H₁ for team growth; compute population and sample means.
3. Build sampling distribution (20+ draws); optional Excel `RAND` replication.
4. Compare growth rates across all four regions.

## Success criteria

* Population mean ≈ **150.30**; sample(n=10, rs=42) mean ≈ **132.60**.
* Growth rate = **0.75**; North = **0.60**.

---

# Lab 5 — Tool landscape

## Objective

Classify course tools; map to CRISP-DM and Days 2–6; complete org worksheet.

**Estimated time:** ~75 min

## Tasks

1. Open `notebooks/lab05_tool_landscape.ipynb`.
2. Complete tool matrix, scavenger hunt, and org stack worksheet.
3. Contrast MLflow vs DVC; map tools to CRISP-DM phases.

## Success criteria

* ≥**3** categories with ≥**2** tools each.
* MLflow and DVC in MLOps bucket.

---

# Lab 6 — Excel group activity

## Objective

Group Excel pivot analysis of regional sales; verify in pandas; present totals vs % growth.

**Estimated time:** ~110 min

## Tasks

1. In **Excel**: pivot `team_sales.csv` by region; chart Q2 totals.
2. Open `notebooks/lab06_excel_group_activity.ipynb` to **verify** your Excel answers.
3. Prepare one slide: North wins total Q2, but which region wins **% growth**?

## Success criteria

* Regional totals match notebook verification.
* **15** growth teams; top region **North** (by Q2 total).
* Group presents one chart and the growth-rate insight.

---
