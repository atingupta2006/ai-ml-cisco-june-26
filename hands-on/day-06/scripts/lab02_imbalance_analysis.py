"""Lab 2 — Analyze class imbalance and baseline majority-class accuracy."""

from __future__ import annotations

from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from _data import build_preprocessor, feature_matrix

X, y = feature_matrix()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

fraud_count = int(y.sum())
legit_count = len(y) - fraud_count
imbalance_ratio = legit_count / max(fraud_count, 1)

baseline = Pipeline(
    steps=[
        ("preprocess", build_preprocessor()),
        ("clf", DummyClassifier(strategy="most_frequent")),
    ]
)
baseline.fit(X_train, y_train)
y_pred = baseline.predict(X_test)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("Lab 2 — Imbalance analysis")
print(f"total rows: {len(y)}")
print(f"fraud: {fraud_count}, legit: {legit_count}")
print(f"imbalance ratio (legit:fraud): {imbalance_ratio:.1f}:1")
print(f"fraud rate: {y.mean():.4f}")
print(f"baseline accuracy (majority class): {(y_pred == y_test).mean():.4f}")
print(f"baseline F1 (fraud): {f1:.4f}")
print()
print(classification_report(y_test, y_pred, zero_division=0))
