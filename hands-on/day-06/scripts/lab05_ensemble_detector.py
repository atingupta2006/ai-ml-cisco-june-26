"""Lab 5 — Random Forest ensemble for fraud detection."""

from __future__ import annotations

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from _data import build_preprocessor, feature_matrix

X, y = feature_matrix()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipe = Pipeline(
    steps=[
        ("preprocess", build_preprocessor()),
        (
            "clf",
            RandomForestClassifier(
                n_estimators=100,
                class_weight="balanced",
                random_state=42,
            ),
        ),
    ]
)
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)

f1 = f1_score(y_test, y_pred, zero_division=0)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)

print("Lab 5 — Ensemble detector (Random Forest)")
print(f"estimators: 100, class_weight: balanced")
print(f"precision (fraud): {precision:.4f}")
print(f"recall (fraud): {recall:.4f}")
print(f"F1 (fraud): {f1:.4f}")
