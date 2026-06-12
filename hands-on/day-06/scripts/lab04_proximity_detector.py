"""Lab 4 — Local Outlier Factor (proximity-based) anomaly detection."""

from __future__ import annotations

import numpy as np
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.pipeline import Pipeline

from _data import build_preprocessor, feature_matrix

X, y = feature_matrix()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Fit on legitimate training transactions only (semi-supervised anomaly detection)
X_train_legit = X_train[y_train == 0]

preprocess = build_preprocessor()
X_train_legit_s = preprocess.fit_transform(X_train_legit)
X_test_s = preprocess.transform(X_test)

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.02, novelty=True)
lof.fit(X_train_legit_s)
pred = lof.predict(X_test_s)
y_pred = np.where(pred == -1, 1, 0)

precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)

print("Lab 4 — Proximity detector (LOF)")
print(f"train legit rows: {len(X_train_legit)}")
print(f"test rows: {len(X_test)}")
print(f"predicted anomalies: {int((y_pred == 1).sum())}")
print(f"precision (fraud): {precision:.4f}")
print(f"recall (fraud): {recall:.4f}")
