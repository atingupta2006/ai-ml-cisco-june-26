# Day 01 — Labs

**Theme:** Data Science Introduction | **Duration:** Concepts + Excel group activity

**Execution guide:** [docs/lab-execution-guide.md](../../docs/lab-execution-guide.md) — read before Lab 1.

---

## Before every lab

**Environment:** one venv for all days — run `setup_student_env.ps1` (Windows) or `setup_student_env.sh` (Linux/Mac) once at repo root. See [lab execution guide](../../docs/lab-execution-guide.md). Jupyter kernel: **Python (cisco-aiml-lab)**.

Labs 1, 2, and 5 are **discussion / worksheet** activities (no code required).

Labs 3, 4, and 6 use the team sales file [`data/team_sales.csv`](data/team_sales.csv) (**20** rows). Lab 6 is designed as an **Excel group activity** — complete in Excel first, then verify with the Python checkpoint script.

---

## Expected outcomes

| After lab | Check |
|-----------|--------|
| Lab 1 | Worksheet: AI ⊃ ML ⊃ DS nesting correct |
| Lab 2 | Worksheet: all six CRISP-DM phases named |
| Lab 3 | Mean q2_sales ≈ **150.30** |
| Lab 4 | Growth rate (q2 > q1) = **0.75** |
| Lab 5 | Worksheet: 3+ categories with 2+ tools each |
| Lab 6 | **15** teams grew; top region **North** |

---

# Lab 1 — AI vs ML vs DS

## Objective

Distinguish Artificial Intelligence, Machine Learning, and Data Science using the Netflix-style use-case from the morning session.

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

## Example answers

| Term | One-line definition |
|------|---------------------|
| AI | Systems that perform tasks requiring human-like intelligence |
| ML | Algorithms that learn patterns from data without explicit rules |
| Data Science | End-to-end process of extracting insight from data |

## Success criteria

* Worksheet completed with nested relationship (AI ⊃ ML; DS overlaps ML).
* At least one original example per term.
* You can explain why not every DS project uses ML.

---

# Lab 2 — Data science cycle

## Objective

Map the CRISP-DM / data science lifecycle phases to a business problem your table chooses.

## Lab flow

```text
  pick problem → map six phases → identify deliverable per phase
```

## Tasks

1. Open `notebooks/lab02_data_science_cycle.ipynb` (recommended) or complete the worksheet on paper.
2. As a group, pick a simple business question (e.g. "Which store region had highest Q2 sales?").
3. Fill in the six phases: **Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment**.
4. For each phase, write one activity and one output artifact.
5. Identify which phases apply even when **no ML model** is built.

## Example result

| Phase | Activity | Output |
|-------|----------|--------|
| Business Understanding | Define KPI | Problem statement |
| Data Understanding | Profile CSV | EDA summary |
| Data Preparation | Clean missing values | Analysis-ready table |

## Success criteria

* All **six** phases named in order.
* Each phase has an activity and deliverable.
* You can explain where Excel analysis fits in the cycle.

---

# Lab 3 — Statistics basics

## Objective

Compute descriptive statistics on Q2 team sales — in Excel or with the verification script.

## Lab flow

```text
  open team_sales.csv → mean / median / std / min / max on q2_sales
```

## Tasks

1. Open `notebooks/lab03_statistics_basics.ipynb` (recommended), or [`data/team_sales.csv`](data/team_sales.csv) in Excel, or run `scripts/lab03_statistics_basics.py`.
2. Calculate mean, median, and standard deviation of `q2_sales`.
3. Record min and max Q2 sales.
4. Discuss which measure is most affected by Team_13's high Q2 value.

## Example result

```text
rows: 20
mean q2_sales: 150.30
median q2_sales: 148.50
std q2_sales: 34.74
```

## Success criteria

* Mean ≈ **150.30** and median ≈ **148.50**.
* You can define mean vs median in plain language.
* Script or Excel workbook shows matching values.

---

# Lab 4 — Hypothesis & sampling

## Objective

Practice random sampling and test a simple growth hypothesis: "Did Q2 sales exceed Q1?"

## Lab flow

```text
  population stats → random sample (n=10) → hypothesis proportion q2 > q1
```

## Tasks

1. Open `notebooks/lab04_hypothesis_sampling.ipynb` (recommended) or run `scripts/lab04_hypothesis_sampling.py`.
2. State null hypothesis H0: "Q2 sales are not higher than Q1 on average."
3. Replicate in Excel with `RANDBETWEEN` sample if time permits.
4. Compare sample mean (n=10) to population mean (n=20).
5. Compute the proportion of teams where `q2_sales > q1_sales`.

## Example result

```text
population mean q2_sales: 150.30
sample mean q2_sales: 132.60
growth rate (q2 > q1): 0.75
```

## Success criteria

* Population mean and sample mean both printed.
* Growth rate = **0.75** (15 of 20 teams).
* You can explain why a sample mean can differ from the population mean.

---

# Lab 5 — Tool landscape

## Objective

Categorize data science tools from the course into storage, compute, visualization, and ML/MLOps buckets.

## Lab flow

```text
  instructor overview → worksheet matrix → share one tool per category
```

## Tasks

1. Open `notebooks/lab05_tool_landscape.ipynb` (recommended) or complete the worksheet on paper.
2. Complete the tool matrix with examples from this course: Python, Pandas, scikit-learn, MLflow, DVC, FastAPI, SHAP, FeatureTools.
3. Add one **cloud** tool your organization uses (e.g. Databricks, SageMaker, Azure ML).
4. Mark which tools are used on Days 2–6 of this training.
5. Identify one tool for **data** vs **model** versioning (DVC covers both).

## Example answers

| Category | Tools from this course |
|----------|------------------------|
| Languages | Python |
| ML / modeling | scikit-learn, SHAP |
| MLOps | MLflow, DVC |
| API serving | FastAPI |

## Success criteria

* At least **three** categories filled with **two** tools each.
* MLflow and DVC correctly placed in MLOps.
* You can explain one tool your team uses today.

---

# Lab 6 — Excel group checkpoint

## Objective

Complete a group Excel analysis of regional sales and verify totals against the checkpoint script.

## Lab flow

```text
  Excel pivot by region → sum q1/q2 → count growth teams → compare to script
```

## Tasks

1. Open `notebooks/lab06_excel_group_checkpoint.ipynb` (recommended) and/or import [`data/team_sales.csv`](data/team_sales.csv) into Excel.
2. Build a pivot (or `SUMIF`) table: total `q1_sales` and `q2_sales` by `region`.
3. Count teams where Q2 > Q1; identify the region with highest Q2 total.
4. Run `scripts/lab06_excel_group_checkpoint.py` and confirm your Excel answers match.

## Example result

```text
teams with q2 > q1: 15
top region by q2 total: North
total q2_sales: 3006
```

## Success criteria

* Regional totals match the script output table.
* **15** growth teams and top region **North** confirmed.
* Group presents one chart (bar or column) of regional Q2 sales.

---
