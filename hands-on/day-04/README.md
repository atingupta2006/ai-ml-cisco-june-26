# Day 04 — Distance-Based ML & MLOps

**Theme:** Distance-Based ML & MLOps

## Session focus

- **Concepts:** Distance metrics, KNN, model selection, FastAPI, FeatureTools, MLflow/DVC
- **Use-case:** Lending Club multi-model comparison and experiment tracking

## Before you start

Read [lab execution guide](../../docs/lab-execution-guide.md) and open [labs.md](labs.md).

## Data

| File | Rows | Path |
|------|------|------|
| Lending Club sample | **1,000** | [`../../data/lending-club/lending_club_sample.csv`](../../data/lending-club/lending_club_sample.csv) |

Kaggle reference: [Lending Club](https://www.kaggle.com/wordsforthewise/lending-club)

**Binary target:** `default` = 1 for `Charged Off` or `Late (31-120 days)`.

## Labs

| Lab | Topic | Notebook / script |
|-----|--------|--------|
| 1 | Distance metrics | `notebooks/lab01_distance_metrics.ipynb` · `lab01_distance_metrics.py` |
| 2 | KNN classifier | `notebooks/lab02_knn_classifier.ipynb` · `lab02_knn_classifier.py` |
| 3 | Choose K | `notebooks/lab03_choose_k.ipynb` · `lab03_choose_k.py` |
| 4 | FastAPI scoring API | `notebooks/lab04_fastapi_scoring_api.ipynb` · `lab04_fastapi_scoring_api.py` |
| 5 | FeatureTools auto FE | `notebooks/lab05_featuretools_auto_fe.ipynb` · `lab05_featuretools_auto_fe.py` |
| 6 | MLflow experiment log | `notebooks/lab06_mlflow_experiment_log.ipynb` · `lab06_mlflow_experiment_log.py` |

## MLflow UI demo (instructor)

See [mlflow-ui-demo-setup.md](../../docs/mlflow-ui-demo-setup.md) for classroom tracking UI steps.

## Syllabus

[course-content.txt](../../../course-content.txt) | [syllabus coverage](../../docs/syllabus-coverage.md)
