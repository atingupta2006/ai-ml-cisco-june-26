# Course topic checklist

Maps every item in [course-content.txt](../course-content.txt) to labs, notebooks, or lecture discussion.  
**Legend:** ✅ hands-on in core labs · 📋 worksheet / discussion in notebook · 🎤 instructor lecture (not coded)

---

## Learning outcomes (14 pillars)

| Outcome | Coverage | Where |
|---------|----------|--------|
| What is data science? | ✅ 📋 | Day 1 Lab 1–2 |
| AI vs ML; future of DS & Big Data | ✅ 📋 | Day 1 Lab 1 morning worksheet |
| Python basics; Python DS libraries | ✅ | Day 2 Labs 1–3 |
| Statistics; visualization outline | ✅ | Day 1 Labs 3–4; Day 2 Lab 4 |
| Basics of linear algebra | ✅ | Day 4 Lab 1; Day 2 Lab 2 vectors |
| Predictive & statistical modelling | ✅ | Days 2–3 |
| ML models & basics | ✅ 📋 | Day 2 Lab 3 problem types |
| Probability | ✅ | Day 3 Lab 1 |
| Evaluation metrics (regression & classification) | ✅ | Day 2 Lab 6; Day 3 Labs 3–4 |
| Distance algorithms | ✅ | Day 4 Labs 1–3 |
| Feature engineering & auto FE | ✅ | Day 3 Lab 5; Day 4 Lab 5 FeatureTools |
| Feature selection | ✅ | Day 3 Lab 5 SelectKBest extension |
| MLflow & DVC | ✅ | Day 1 Lab 5; Day 4 Lab 6 |
| Unsupervised learning & cluster metrics | ✅ | Day 5 all labs |
| Anomaly detection | ✅ | Day 6 all labs |

---

## Day 1 — Data Science Introduction

| Syllabus topic | Status | Location |
|----------------|--------|----------|
| Netflix AI use-case | ✅ | `lab01_ai_ml_ds.ipynb` |
| AI / DS / ML | ✅ | Lab 1 |
| Big Data & AI | 📋 | Lab 1 morning worksheet |
| AI roles | 📋 | Lab 1 morning worksheet |
| AI maturity | 📋 | Lab 1 morning worksheet |
| Future tech / future of DS | 📋 | Lab 1 morning worksheet |
| Analytics vs AI | ✅ 📋 | Lab 1 |
| Problems of AI | 📋 | Lab 1 morning worksheet |
| Data Science cycle | ✅ | `lab02_data_science_cycle.ipynb` |
| AI tool landscape | ✅ | `lab05_tool_landscape.ipynb` |
| Basic statistics | ✅ | `lab03_statistics_basics.ipynb` |
| Sample & hypothesis | ✅ | `lab04_hypothesis_sampling.ipynb` |
| Excel group activity | ✅ | `lab06_excel_group_activity.ipynb` |

---

## Day 2 — Python for Data Science

| Syllabus topic | Status | Location |
|----------------|--------|----------|
| Python data structures | ✅ | `lab01_python_structures.ipynb` |
| NumPy | ✅ | `lab02_numpy_arrays.ipynb` |
| Pandas (Zomato) | ✅ | `lab03_pandas_zomato_load.ipynb` |
| Seaborn | ✅ | `lab04_seaborn_plots.ipynb` |
| Plotly | ✅ | Lab 4 Plotly extension (`pip install plotly`) |
| Linear vs non-linear | ✅ | `lab05_linear_regression_fit.ipynb` |
| Data types | ✅ | Lab 3 `dtypes` section |
| Vector space | ✅ | Lab 2 vector space section |
| ML models intro; types of ML problems | ✅ 📋 | Lab 3 problem-types table |
| Linear regression; OLS | ✅ | `lab05_linear_regression_fit.ipynb` |
| Gradient descent | ✅ | Lab 5 GD loop vs OLS |
| LR metrics | ✅ | `lab06_lr_evaluation_metrics.ipynb` |
| L1 / L2 | ✅ | Lab 6 Ridge/Lasso extension |

---

## Day 3 — Classification & Interpretation

| Syllabus topic | Status | Location |
|----------------|--------|----------|
| Probability & odds | ✅ | `lab01_probability_exercises.ipynb` |
| Classification via linear regression / logit | ✅ | Lab 1 "From regression to classification" |
| Classification metrics | ✅ | Labs 2–3 |
| ROC / AUC | ✅ | `lab04_roc_auc.ipynb` |
| Feature engineering | ✅ | `lab05_sklearn_pipeline.ipynb` |
| Feature selection | ✅ | Lab 5 SelectKBest extension |
| SHAP interpretability | ✅ | `lab06_shap_interpretability.ipynb` |
| sklearn Pipeline | ✅ | Lab 5 |

---

## Day 4 — Distance-Based ML & MLOps

| Syllabus topic | Status | Location |
|----------------|--------|----------|
| Distance metrics; similarity / dissimilarity | ✅ | `lab01_distance_metrics.ipynb` |
| Lazy learning | ✅ | `lab02_knn_classifier.ipynb` |
| KNN; finding K | ✅ | Labs 2–3 |
| Multi-model analysis | ✅ | Lab 6 MLflow compare; Day 6 capstone |
| FastAPI | ✅ | `lab04_fastapi_scoring_api.ipynb` |
| FeatureTools auto FE | ✅ | `lab05_featuretools_auto_fe.ipynb` |
| MLflow experiment tracking | ✅ | `lab06_mlflow_experiment_log.ipynb` |
| DVC | ✅ | Lab 6 (`dvc init`, `dvc add`, `dvc status`); Lab 1 tool matrix |

---

## Day 5 — Unsupervised Learning

| Syllabus topic | Status | Location |
|----------------|--------|----------|
| Clustering & segmentation | ✅ | Labs 1, 6 |
| K-Means; find best K | ✅ | Labs 1–2 |
| Spectral clustering | ✅ | Lab 3 Spectral comparison (§2b) |
| DBSCAN | ✅ | `lab03_dbscan_clusters.ipynb` |
| OPTICS | ✅ | Lab 3 OPTICS comparison (§2b) |
| Multi-cluster analysis | ✅ | `lab05_nyse_multi_cluster_view.ipynb` |
| Clustering evaluation metrics | ✅ | `lab04_cluster_metrics.ipynb` |

---

## Day 6 — Anomaly Detection

| Syllabus topic | Status | Location |
|----------------|--------|----------|
| Anomaly detection | ✅ | All labs |
| Outlier types | ✅ | Lab 1 IQR |
| Detection methods | ✅ | Lab 1 methods table |
| Prediction outliers | ✅ | Lab 1 residual / probability demo (§3b) |
| Imbalanced data | ✅ | `lab02_imbalance_analysis.ipynb` |
| Re-sampling; over/under-sampling | ✅ | `lab03_resampling_lab.ipynb` |
| Linear / proximity / ensemble models | ✅ | Labs 3–5 + capstone |

---

## Lecture-only or light-touch topics

These appear in **Day 1 Lab 1 worksheets** or instructor slides — not every bullet needs executable code:

- AI maturity levels, future tech headlines, organizational AI roles (Day 1 worksheet)
- DVC hands-on in Lab 6 requires `dvc` in the student environment (`requirements-student.txt`)

---

## Maintainer

Regenerate topic inserts: `cd GH/tools && python enrich_topic_coverage.py`  
Gap-closure extensions: `python enrich_gap_closure.py`  
See also: [syllabus-coverage.md](syllabus-coverage.md)
