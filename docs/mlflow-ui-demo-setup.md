# MLflow UI — classroom demo setup (Day 4)

Use this guide to run the **MLflow Tracking UI** locally so students can inspect experiments logged in Day 4 Lab 6.

**Related lab:** `hands-on/day-04/notebooks/lab06_mlflow_experiment_log.ipynb`  
**Tracking backend:** SQLite file at `hands-on/day-04/output/mlflow.db` (created when the notebook runs).

---

## Prerequisites

| Item | Version / note |
|------|----------------|
| Python | 3.10+ |
| MLflow | Included after `setup_student_env` |
| Day 4 Lab 6 notebook | Run through the MLflow cells first |

```bash
source .venv/bin/activate   # Windows: .\.venv\Scripts\Activate.ps1
```

---

## Quick start

### Step 1 — Generate a run

Open and run `hands-on/day-04/notebooks/lab06_mlflow_experiment_log.ipynb` through the MLflow logging cells.

Expected console output includes:

```text
experiment: cisco-aiml-day04-lending-club
run_id: <uuid>
accuracy: 0.58xx
tracking db: mlflow.db
```

### Step 2 — Start the UI

From the repository root (with venv active):

```bash
cd hands-on/day-04/output
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000
```

Open **http://127.0.0.1:5000** in your browser.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `mlflow.db` not found | Run Day 4 Lab 6 notebook MLflow cells first |
| Port 5000 in use | Try `--port 5001` |
| Empty UI | Confirm experiment name `cisco-aiml-day04-lending-club` |

---

## Classroom tip

Project the UI after students log their first run so they can compare **parameters**, **metrics**, and **artifacts** side by side.
