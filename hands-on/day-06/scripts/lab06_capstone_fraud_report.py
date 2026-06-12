"""Lab 6 — Capstone: compare fraud detection approaches and write summary report."""

from __future__ import annotations

import json

import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.pipeline import Pipeline
from sklearn.utils import resample

from _data import build_preprocessor, feature_matrix
from _paths import OUTPUT_DIR

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

X, y = feature_matrix()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

preprocess = build_preprocessor()
X_train_s = preprocess.fit_transform(X_train)
X_test_s = preprocess.transform(X_test)


def scores(y_true, y_pred) -> dict[str, float]:
    return {
        "precision": round(precision_score(y_true, y_pred, zero_division=0), 4),
        "recall": round(recall_score(y_true, y_pred, zero_division=0), 4),
        "f1": round(f1_score(y_true, y_pred, zero_division=0), 4),
    }


results: list[dict] = []

# Baseline
dummy_pred = DummyClassifier(strategy="most_frequent").fit(X_train, y_train).predict(X_test)
results.append({"model": "majority_baseline", **scores(y_test, dummy_pred)})

# Logistic regression
lr = Pipeline(
    steps=[
        ("preprocess", build_preprocessor()),
        ("clf", LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")),
    ]
)
lr.fit(X_train, y_train)
results.append({"model": "logistic_regression", **scores(y_test, lr.predict(X_test))})

# LOF
X_legit_s = preprocess.fit_transform(X_train[y_train == 0])
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.02, novelty=True)
lof.fit(X_legit_s)
lof_pred = np.where(lof.predict(X_test_s) == -1, 1, 0)
results.append({"model": "lof_proximity", **scores(y_test, lof_pred)})

# Random Forest
rf = Pipeline(
    steps=[
        ("preprocess", build_preprocessor()),
        ("clf", RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42)),
    ]
)
rf.fit(X_train, y_train)
results.append({"model": "random_forest", **scores(y_test, rf.predict(X_test))})

report_df = pd.DataFrame(results).sort_values("f1", ascending=False)
best = report_df.iloc[0]

report_path = OUTPUT_DIR / "fraud_detection_report.json"
report_path.write_text(report_df.to_json(orient="records", indent=2), encoding="utf-8")

print("Lab 6 — Capstone fraud report")
print(f"test fraud cases: {int(y_test.sum())} / {len(y_test)}")
print()
print(report_df.to_string(index=False))
print()
print(f"best model (F1): {best['model']} (F1={best['f1']})")
print(f"report saved: {report_path.name}")
