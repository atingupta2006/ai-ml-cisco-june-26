# Lab execution guide

## One environment for all six days

Use **one** virtual environment at `.venv` in the repository root.

### First-time setup

**Windows (PowerShell):**

```powershell
.\setup_student_env.ps1
.\.venv\Scripts\Activate.ps1
```

**Linux, macOS, WSL, Azure VM:**

```bash
chmod +x setup_student_env.sh
./setup_student_env.sh
source .venv/bin/activate
```

Requires **Python 3.10+**. The script installs packages from [`requirements-student.txt`](../requirements-student.txt), registers the Jupyter kernel **Python (cisco-aiml-lab)**, and creates empty `output/` folders under each day.

### Every lab session

```bash
source .venv/bin/activate          # Windows: .\.venv\Scripts\Activate.ps1
cd hands-on/day-NN/notebooks       # pick the day
jupyter lab
```

In Jupyter: **Kernel → Change kernel → Python (cisco-aiml-lab)**.

Work through `notebooks/lab01` … `lab06` **in order**. Saved plots, JSON reports, and MLflow files land in `hands-on/day-NN/output/`.

---

## Workflow

1. Open the day folder under `hands-on/day-NN/`.
2. Read `README.md` then `labs.md`.
3. Run notebooks in `notebooks/` in lab order (`lab01` … `lab06`).
4. Compare outputs to **Example result** and **Success criteria** in each lab.

---

## Verify your setup

```bash
source .venv/bin/activate
python -c "import pandas, numpy, sklearn, matplotlib, seaborn, shap; print('packages ok')"
```

Open `hands-on/day-01/notebooks/lab01_ai_ml_ds.ipynb` and run the first code cell to confirm the kernel works.

---

## Generated folders (normal)

| Folder | Created by | Action |
|--------|------------|--------|
| `hands-on/day-NN/output/` | Notebooks saving plots, reports, `mlflow.db` | Keep; gitignored except `.gitkeep` |
| `mlruns/` or `**/mlruns/` | MLflow default artifact store (some environments) | Safe to delete; not required for class |

---

## Checkpoint datasets

| Dataset | Rows | Days |
|---------|------|------|
| team_sales.csv | **20** | 1 |
| Zomato | **500** | 2 |
| Lending Club | **1,000** | 3–4 |
| NYSE daily | **500** (25 symbols in labs) | 5 |
| Credit card | **1,000** (**10** fraud) | 6 |

Files live in [`data/`](../data/README.md). Do not substitute full Kaggle downloads unless instructed.

---

## Problems?

[Student troubleshooting](student-troubleshooting.md)
