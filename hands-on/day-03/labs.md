# Day 03 — Labs

**Theme:** Classification & Model Interpretation | **Lab time (6 labs):** ~305 min (~5.1 h)

**Execution guide:** [docs/lab-execution-guide.md](../../docs/lab-execution-guide.md) — read before Lab 1.

---

## Before every lab

**Environment:** one venv for all days — `setup_student_env.ps1` or `setup_student_env.sh` at repo root (includes `shap`). Kernel: **Python (cisco-aiml-lab)**. [Lab execution guide](../../docs/lab-execution-guide.md).

Run notebooks in `notebooks/` in lab order (`lab01` … `lab06`).

**Target variable:** `default` = 1 when `loan_status` is `Charged Off` or `Late (31-120 days)`, else 0.

---

## Expected outcomes

| After lab | Check |
|-----------|--------|
| Lab 1 | `rows` = **1000**; P(default) ≈ **0.49** |
| Lab 2 | Train **800** / test **200**; sample predictions mix 0 and 1 |
| Lab 3 | Accuracy ≈ **0.59**; F1 ≈ **0.57** |
| Lab 4 | AUC ≈ **0.63**; `roc_curve.png` saved |
| Lab 5 | Pipeline steps `preprocess`, `clf`; accuracy ≈ **0.64** |
| Lab 6 | SHAP shape **(20, 5)**; top driver **int_rate** |


## Lab pacing

| Lab | Est. time |
|-----|-----------|
| Lab 1 | ~50 min |
| Lab 2 | ~55 min |
| Lab 3 | ~50 min |
| Lab 4 | ~45 min |
| Lab 5 | ~50 min |
| Lab 6 | ~55 min |
| **Total** | **~305 min** |

---

# Lab 1 — Probability exercises

## Objective

Connect observed default rates to probability, odds, and log-odds (logit) — the foundation of logistic regression.

**Estimated time:** ~50 min

## Lab flow

```text
  load loans → P(default) → odds → log-odds → worked example
```

## Tasks

1. Open `notebooks/lab01_probability_exercises.ipynb` (recommended) or `lab01_probability_exercises.py`.
2. Run all cells; note `P(default)` from the **1,000**-row sample.
3. Complete the manual odds check and inverse-logit cells.
4. Answer reflection questions linking log-odds to Lab 2 logistic regression.

## Example result

```text
rows: 1000
P(default): 0.4850
odds of default: 0.9417
log-odds (logit): -0.0600
```

## Success criteria

* Script runs without errors.
* `rows` = **1000**.
* You can define probability, odds, and log-odds in your own words.

---

# Lab 2 — Logistic regression

## Objective

Fit logistic regression to predict loan default from numeric borrower features.

**Estimated time:** ~55 min

## Lab flow

```text
  features + target → train/test split → LogisticRegression.fit → probabilities
```

## Tasks

1. Open `notebooks/lab02_logistic_regression.ipynb` (recommended) or `lab02_logistic_regression.py`.
2. Fit the model; inspect positive coefficients for `int_rate` and `dti`.
3. Compare `predict_proba` vs `predict` in the comparison table (first 3 test rows).
4. Complete the manual log-odds cell and relate it to the sigmoid plot.

## Example result

```text
train size: 800, test size: 200
coefficients: int_rate positive, dti positive
sample P(default): [0.685  0.355  0.5472]
sample predictions: [1, 0, 1]
```

## Success criteria

* Model trains on **800** rows and evaluates on **200**.
* Five numeric features used; intercept and coefficients printed.
* At least one sample prediction is **1** (default).

---

# Lab 3 — Confusion matrix

## Objective

Evaluate classifier performance with confusion matrix, accuracy, precision, recall, and F1.

**Estimated time:** ~50 min

## Lab flow

```text
  predict test set → confusion_matrix → precision / recall / F1
```

## Tasks

1. Open `notebooks/lab03_confusion_matrix.ipynb` (recommended) or `lab03_confusion_matrix.py`.
2. Read the heatmap and label TN, FP, FN, TP.
3. Record accuracy, precision, recall, and F1.
4. Review the threshold table (0.3–0.7) and discuss precision vs recall at **0.4** vs **0.5**.

## Example result

```text
confusion matrix:
[[63 40]
 [42 55]]
accuracy: 0.5900
F1: 0.5729
```

## Success criteria

* Confusion matrix is 2×2 with non-zero entries in all cells.
* Accuracy, precision, recall, and F1 are printed.
* You can map each matrix cell to a metric definition.

---

# Lab 4 — ROC and AUC

## Objective

Plot the ROC curve and compute area under the curve (AUC) for ranking ability across thresholds.

**Estimated time:** ~45 min

## Lab flow

```text
  predict_proba → roc_curve → auc → save plot
```

## Tasks

1. Open `notebooks/lab04_roc_auc.ipynb` (recommended) or `lab04_roc_auc.py`.
2. Run all cells; confirm `output/roc_curve.png` is saved.
3. Compare AUC (~**0.63**) to **0.5** random baseline.
4. Review the Youden's J point — threshold where TPR − FPR is largest.

## Example result

```text
AUC: 0.6326
plot saved: roc_curve.png
```

## Success criteria

* `output/roc_curve.png` is created.
* AUC printed and **> 0.5**.
* You can explain what the diagonal dashed line represents.

---

# Lab 5 — sklearn Pipeline

## Objective

Build an end-to-end `Pipeline` with `ColumnTransformer` for scaling numeric columns and one-hot encoding categoricals.

**Estimated time:** ~50 min

## Lab flow

```text
  ColumnTransformer → Pipeline(preprocess + clf) → fit → predict
```

## Tasks

1. Open `notebooks/lab05_sklearn_pipeline.ipynb` (recommended) or `lab05_sklearn_pipeline.py`.
2. Run all cells and list pipeline step names.
3. Inspect which columns are numeric vs categorical in `_data.py`.
4. Compare full pipeline accuracy to the numeric-only baseline in the notebook extension.

## Example result

```text
pipeline steps: ['preprocess', 'clf']
test accuracy: 0.6350
```

## Success criteria

* Pipeline has **two** named steps: `preprocess` and `clf`.
* Test accuracy printed (expect ≈ **0.64**).
* You can explain why preprocessing belongs inside the pipeline.

---

# Lab 6 — SHAP interpretability

## Objective

Use SHAP values to explain which features drive individual default predictions.

**Estimated time:** ~55 min

## Lab flow

```text
  scale features → fit logistic model → SHAP Explainer → mean |SHAP| ranking
```

## Tasks

1. Open `notebooks/lab06_shap_interpretability.ipynb` (recommended) or `lab06_shap_interpretability.py`.
2. Run all cells; note the feature with highest mean |SHAP|.
3. Discuss why `int_rate` often ranks highly for credit risk.
4. Inspect the SHAP bar and waterfall plots saved to `output/`.

## Example result

```text
SHAP values shape: (20, 5)
top driver (mean |SHAP|): int_rate
```

## Success criteria

* SHAP values shape is **(20, 5)** for 20 test rows and 5 features.
* Mean |SHAP| printed per feature.
* You can explain SHAP as a per-prediction feature attribution method.

---
