# MLflow UI — classroom demo setup (Day 4)

Use this guide to run the **MLflow Tracking UI** locally so students can inspect experiments logged in Day 4 Lab 6.

**Related lab:** `hands-on/day-04/scripts/lab06_mlflow_experiment_log.py`  
**Tracking backend:** SQLite file at `hands-on/day-04/scripts/output/mlflow.db` (created when the lab script runs).

---

## Prerequisites

| Item | Version / note |
|------|----------------|
| Python | 3.10+ |
| MLflow | Included after `setup_student_env` |
| Day 4 lab script | Run once to create `mlflow.db` |

```bash
source .venv/bin/activate   # Windows: .\.venv\Scripts\Activate.ps1
```

---

## Quick start

### Step 1 — Generate a run

```bash
cd hands-on/day-04/scripts
python lab06_mlflow_experiment_log.py
```

Expected console output includes:

```text
experiment: cisco-aiml-day04-lending-club
run_id: <uuid>
accuracy: 0.58xx
tracking db: mlflow.db
```

### Step 2 — Start the MLflow UI

From `hands-on/day-04/scripts`:

```bash
mlflow ui --backend-store-uri sqlite:///output/mlflow.db --host 127.0.0.1 --port 5000
```

Run with `scripts` as the current directory so the relative SQLite path resolves correctly.

### Step 3 — Open the browser

| URL | Purpose |
|-----|---------|
| http://127.0.0.1:5000 | Experiments list |
| http://127.0.0.1:5000/#/experiments/1 | First experiment (ID may vary) |

Walk through:

1. **Experiments** → `cisco-aiml-day04-lending-club`
2. **Runs** → click `knn-baseline` run
3. **Parameters** tab → `model`, `k`
4. **Metrics** tab → `accuracy`
5. **Artifacts** tab → logged sklearn model

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `mlflow.db` not found | Run `lab06_mlflow_experiment_log.py` first |
| `MlflowException` file-store maintenance | This course uses **SQLite** — do not use `file:./mlruns` on MLflow 3.x without `MLFLOW_ALLOW_FILE_STORE=true` |
| Empty experiments list | Check `--backend-store-uri` path; must match where `mlflow.db` was created |
| Port 5000 in use | Use `--port 5001` and open matching URL |

---

## Security notes

- Run UI on `127.0.0.1` unless students need remote access on an isolated lab VLAN.
- Do not expose MLflow UI to the public internet without authentication.
