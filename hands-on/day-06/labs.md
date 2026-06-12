# Day 06 — Labs

**Theme:** Anomaly Detection | **Lab time (6 labs):** ~285 min (~4.8 h)

**Execution guide:** [docs/lab-execution-guide.md](../../docs/lab-execution-guide.md) — read before Lab 1.

---

## Before every lab

**Environment:** one venv for all days — `setup_student_env.ps1` or `setup_student_env.sh` at repo root. Kernel: **Python (cisco-aiml-lab)**. [Lab execution guide](../../docs/lab-execution-guide.md).

Run notebooks in `notebooks/` in lab order (`lab01` … `lab06`).

**Target:** `is_fraud` (1 = fraudulent transaction).

---

## Expected outcomes

| After lab | Check |
|-----------|--------|
| Lab 1 | **1000** rows; **10** fraud; mean fraud amount ≈ **234** |
| Lab 2 | Imbalance ≈ **99:1**; baseline F1 = **0.00** |
| Lab 3 | Oversampled train fraud = **792**; F1 ≈ **0.67** |
| Lab 4 | LOF recall (fraud) = **1.00** |
| Lab 5 | Random Forest F1 ≈ **0.67** |
| Lab 6 | Best model **logistic_regression**; F1 ≈ **0.80** |


## Lab pacing

| Lab | Est. time |
|-----|-----------|
| Lab 1 | ~45 min |
| Lab 2 | ~40 min |
| Lab 3 | ~45 min |
| Lab 4 | ~50 min |
| Lab 5 | ~50 min |
| Lab 6 | ~55 min |
| **Total** | **~285 min** |

---

# Lab 1 — Outlier exploration

## Objective

Explore statistical outliers in `amount` and `distance_from_home` and compare fraud vs legitimate transactions.

**Estimated time:** ~45 min

## Lab flow

```text
  load transactions → IQR outlier counts → fraud vs legit means
```

## Tasks

1. Open `notebooks/lab01_outlier_exploration.ipynb` (recommended) or `lab01_outlier_exploration.py`.
2. Run all cells and compare mean amount for fraud vs legit rows.
3. Identify transactions above the IQR upper bound for `amount`.
4. Discuss why rule-based outlier flags alone are insufficient for fraud.

## Example result

```text
rows: 1000
fraud rows: 10
mean amount (legit): 43.22
mean amount (fraud): 233.94
max distance (fraud): 51.72
```

## Success criteria

* **1,000** rows and **10** fraud cases confirmed.
* IQR outlier counts printed for amount and distance.
* Fraud mean amount clearly higher than legit mean.

---

# Lab 2 — Imbalance analysis

## Objective

Quantify class imbalance and show why a majority-class baseline fails on fraud detection.

**Estimated time:** ~40 min

## Lab flow

```text
  class counts → imbalance ratio → DummyClassifier → F1 on fraud
```

## Tasks

1. Open `notebooks/lab02_imbalance_analysis.ipynb` (recommended) or `lab02_imbalance_analysis.py`.
2. Run all cells and note the imbalance ratio.
3. Explain why **99%** accuracy can still mean **0** fraud detections.
4. List metrics better suited to rare events (precision, recall, F1).

## Example result

```text
imbalance ratio (legit:fraud): 99.0:1
baseline F1 (fraud): 0.0000
```

## Success criteria

* Fraud count **10** and imbalance ratio ≈ **99:1**.
* Baseline F1 for fraud class is **0.00**.
* You can explain precision–recall trade-off for rare fraud.

---

# Lab 3 — Resampling lab

## Objective

Oversample the minority fraud class on the training set and compare F1 before and after.

**Estimated time:** ~45 min

## Lab flow

```text
  split train/test → oversample fraud in train → LogisticRegression → F1 compare
```

## Tasks

1. Open `notebooks/lab03_resampling_lab.ipynb` (recommended) or `lab03_resampling_lab.py`.
2. Run all cells and compare F1 with and without oversampling.
3. Try undersampling the majority class instead (optional extension).
4. Discuss overfitting risk when oversampling a tiny fraud set.

## Example result

```text
train fraud before: 8, after oversample: 792
F1 fraud (oversampled train): 0.6667
```

## Success criteria

* Training fraud count increases after oversampling.
* F1 printed for both approaches.
* You can name one over- and one under-sampling strategy.

---

# Lab 4 — Proximity detector

## Objective

Use Local Outlier Factor (LOF) — a proximity-based method — trained on legitimate transactions to flag anomalies.

**Estimated time:** ~50 min

## Lab flow

```text
  train LOF on legit only → predict test → precision / recall on fraud
```

## Tasks

1. Open `notebooks/lab04_proximity_detector.ipynb` (recommended) or `lab04_proximity_detector.py`.
2. Run all cells; note high recall but lower precision.
3. Adjust `contamination` (e.g. 0.01 vs 0.05) and observe metric changes.
4. Compare LOF (unsupervised) to supervised models from Day 3.

## Example result

```text
precision (fraud): 0.3333
recall (fraud): 1.0000
```

## Success criteria

* LOF trained on legitimate training rows only.
* Precision and recall printed.
* You can explain why LOF is called a proximity-based method.

---

# Lab 5 — Ensemble detector

## Objective

Train a Random Forest ensemble with `class_weight='balanced'` for fraud classification.

**Estimated time:** ~50 min

## Lab flow

```text
  preprocess → RandomForest(100 trees, balanced) → precision / recall / F1
```

## Tasks

1. Open `notebooks/lab05_ensemble_detector.ipynb` (recommended) or `lab05_ensemble_detector.py`.
2. Run all cells and record fraud-class metrics.
3. Compare F1 to LOF (Lab 4) and resampled logistic regression (Lab 3).
4. Increase `n_estimators` to 200 — does F1 change materially?

## Example result

```text
precision (fraud): 1.0000
recall (fraud): 0.5000
F1 (fraud): 0.6667
```

## Success criteria

* Random Forest with **100** estimators and balanced class weights.
* All three metrics printed.
* You can explain why ensembles help on tabular fraud features.

---

# Lab 6 — Capstone fraud report

## Objective

Compare baseline, logistic regression, LOF, and Random Forest; save a JSON report of results.

**Estimated time:** ~55 min

## Lab flow

```text
  run all approaches → metrics table → rank by F1 → save fraud_detection_report.json
```

## Tasks

1. Open `notebooks/lab06_capstone_fraud_report.ipynb` (recommended) or `lab06_capstone_fraud_report.py`.
2. Run all cells and review the ranked metrics table.
3. Open `output/fraud_detection_report.json`.
4. Write a 3-sentence executive summary: which model to deploy and why.

## Example result

```text
best model (F1): logistic_regression (F1=0.8)
report saved: fraud_detection_report.json
```

## Success criteria

* Comparison table with at least **4** models.
* `output/fraud_detection_report.json` created.
* You can recommend a model balancing precision and recall for fraud.

---
