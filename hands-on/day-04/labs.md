# Day 04 — Labs

**Theme:** Distance-Based ML & MLOps | **Lab time (6 labs):** ~285 min (~4.8 h)

**Execution guide:** [docs/lab-execution-guide.md](../../docs/lab-execution-guide.md) — read before Lab 1.

---

## Before every lab

**Environment:** one venv for all days — `setup_student_env.ps1` or `setup_student_env.sh` at repo root (includes FastAPI, FeatureTools, MLflow). Kernel: **Python (cisco-aiml-lab)**. [Lab execution guide](../../docs/lab-execution-guide.md).

Run notebooks in `notebooks/` **or** scripts in `scripts/` in lab order (`lab01` … `lab06`).

---

## Expected outcomes

| After lab | Check |
|-----------|--------|
| Lab 1 | Cosine similarity ≈ **0.90** between first two loans |
| Lab 2 | KNN k=**5**; test accuracy ≈ **0.55** |
| Lab 3 | Best k = **3**; accuracy ≈ **0.59** |
| Lab 4 | `GET /health` → **200**; `POST /predict` → **200** |
| Lab 5 | Feature matrix shape **(1000, 6)**; top corr **int_rate** |
| Lab 6 | MLflow run logged; accuracy ≈ **0.58**; `metrics.json` written |


## Lab pacing

| Lab | Est. time |
|-----|-----------|
| Lab 1 | ~40 min |
| Lab 2 | ~50 min |
| Lab 3 | ~35 min |
| Lab 4 | ~55 min |
| Lab 5 | ~50 min |
| Lab 6 | ~55 min |
| **Total** | **~285 min** |

---

# Lab 1 — Distance metrics

## Objective

Compute Euclidean, Manhattan, and cosine distances between two loan feature vectors.

**Estimated time:** ~40 min

## Lab flow

```text
  select two loans → numpy vectors → Euclidean / Manhattan / cosine
```

## Tasks

1. Open `notebooks/lab01_distance_metrics.ipynb` (recommended) or `scripts/lab01_distance_metrics.py`.
2. Run all cells and compare the three distance measures.
3. Change to rows 10 and 50 (`iloc[9]`, `iloc[49]`) and note which metric changes most.
4. Explain why scaling matters before distance-based algorithms (preview for Lab 2).

## Example result

```text
Euclidean distance: 69370.1405
Manhattan distance: 71367.0300
cosine similarity: 0.8960
```

## Success criteria

* Script runs without errors.
* All three metrics printed for the same pair of loans.
* You can describe when cosine distance is preferred over Euclidean.

---

# Lab 2 — KNN classifier

## Objective

Train a K-Nearest Neighbors classifier with **k = 5** on scaled numeric loan features.

**Estimated time:** ~50 min

## Lab flow

```text
  StandardScaler → KNeighborsClassifier(5) → fit → predict → accuracy
```

## Tasks

1. Open `notebooks/lab02_knn_classifier.ipynb` (recommended) or `scripts/lab02_knn_classifier.py`.
2. Run all cells and record test accuracy.
3. Inspect sample predictions — are both classes (0 and 1) predicted?
4. Compare accuracy to Day 3 logistic regression (~0.59).

## Example result

```text
k (neighbors): 5
test accuracy: 0.5500
sample predictions (first 5): [1, 0, 1, 0, 1]
```

## Success criteria

* Pipeline includes scaling before KNN.
* Test accuracy printed (expect ≈ **0.55**).
* Predictions include both **0** and **1**.

---

# Lab 3 — Choose K

## Objective

Sweep candidate **k** values and pick the one with highest test accuracy.

**Estimated time:** ~35 min

## Lab flow

```text
  for k in [1,3,5,7,9,11,15] → fit → accuracy → select best k
```

## Tasks

1. Open `notebooks/lab03_choose_k.ipynb` (recommended) or `scripts/lab03_choose_k.py`.
2. Run all cells and identify the best **k**.
3. Plot accuracy vs k (optional matplotlib extension).
4. Discuss bias–variance: what happens at k=1 vs k=15?

## Example result

```text
best k: 3 (accuracy 0.5900)
```

## Success criteria

* All seven **k** values evaluated.
* Best **k** printed (expect **3** at ≈ **0.59** accuracy).
* You can explain overfitting risk when k is too small.

---

# Lab 4 — FastAPI scoring API

## Objective

Expose the trained KNN model as a REST API and verify it with FastAPI's `TestClient` (no live server required for the lab script).

**Estimated time:** ~55 min

## Lab flow

```text
  train model → define FastAPI app → GET /health → POST /predict → TestClient
```

## Tasks

1. Open `notebooks/lab04_fastapi_scoring_api.ipynb` (recommended) or `scripts/lab04_fastapi_scoring_api.py`.
2. Run all cells and confirm HTTP **200** responses.
3. To run a live server: `uvicorn lab04_fastapi_scoring_api:app --reload` then POST to `http://127.0.0.1:8000/predict`.
4. Change the sample JSON body and observe `default_probability` change.

## Example result

```text
GET /health -> 200 {'status': 'ok'}
POST /predict -> 200
response body: {'default_probability': 0.2, 'default_label': 0}
```

## Success criteria

* `/health` returns status **ok**.
* `/predict` accepts JSON with five numeric fields and returns probability + label.
* You can describe how an API wraps a trained model for production scoring.

---

# Lab 5 — FeatureTools auto FE

## Objective

Use FeatureTools Deep Feature Synthesis (DFS) to auto-generate features from the loans entity set.

**Estimated time:** ~50 min

## Lab flow

```text
  EntitySet → add_dataframe(loans) → dfs(max_depth=1) → correlation ranking
```

## Tasks

1. Open `notebooks/lab05_featuretools_auto_fe.ipynb` (recommended) or `scripts/lab05_featuretools_auto_fe.py`.
2. Run all cells; note input vs engineered feature counts.
3. Review top features correlated with `default`.
4. Compare DFS output columns to the hand-picked Day 3 features.

## Example result

```text
input columns: 7
engineered features: 6
feature matrix shape: (1000, 6)
top |corr| with default: int_rate: 0.2084
```

## Success criteria

* Feature matrix has **1,000** rows.
* Engineered feature count printed.
* Top correlated feature is **int_rate**.

---

# Lab 6 — MLflow experiment log

## Objective

Log a KNN training run to MLflow and write a `metrics.json` artifact suitable for a classroom DVC demo.

**Estimated time:** ~55 min

## Lab flow

```text
  train model → mlflow.start_run → log params/metrics/model → write metrics.json
```

## Tasks

1. Open `notebooks/lab06_mlflow_experiment_log.ipynb` (recommended) or `scripts/lab06_mlflow_experiment_log.py`.
2. Run all cells; note the `run_id` and SQLite tracking DB path.
3. Launch MLflow UI: `mlflow ui --backend-store-uri sqlite:///scripts/output/mlflow.db` (from `day-04/scripts`).
4. Classroom DVC extension: `dvc add scripts/output/metrics.json` to version the metrics file.

## Example result

```text
experiment: cisco-aiml-day04-lending-club
accuracy: 0.5800
tracking db: mlflow.db
metrics artifact (DVC demo): metrics.json
```

## Success criteria

* MLflow experiment and run created without error.
* Parameters (`k`) and metric (`accuracy`) logged.
* `scripts/output/metrics.json` exists after the run.

---
