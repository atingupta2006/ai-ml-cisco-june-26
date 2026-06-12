"""Lab 3 — Oversample minority class and compare logistic regression F1."""

from __future__ import annotations

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.utils import resample

from _data import build_preprocessor, feature_matrix

X, y = feature_matrix()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

train_df = X_train.copy()
train_df["is_fraud"] = y_train.values

majority = train_df[train_df["is_fraud"] == 0]
minority = train_df[train_df["is_fraud"] == 1]
minority_up = resample(
    minority,
    replace=True,
    n_samples=len(majority),
    random_state=42,
)
balanced_train = pd.concat([majority, minority_up]).sample(frac=1, random_state=42)

X_bal = balanced_train.drop(columns=["is_fraud"])
y_bal = balanced_train["is_fraud"]

pipe_raw = Pipeline(
    steps=[
        ("preprocess", build_preprocessor()),
        ("clf", LogisticRegression(max_iter=1000, random_state=42)),
    ]
)
pipe_raw.fit(X_train, y_train)
f1_raw = f1_score(y_test, pipe_raw.predict(X_test), zero_division=0)

pipe_bal = Pipeline(
    steps=[
        ("preprocess", build_preprocessor()),
        ("clf", LogisticRegression(max_iter=1000, random_state=42)),
    ]
)
pipe_bal.fit(X_bal, y_bal)
f1_bal = f1_score(y_test, pipe_bal.predict(X_test), zero_division=0)

print("Lab 3 — Resampling lab")
print(f"train fraud before: {int(y_train.sum())}, after oversample: {int(y_bal.sum())}")
print(f"F1 fraud (no resampling): {f1_raw:.4f}")
print(f"F1 fraud (oversampled train): {f1_bal:.4f}")
