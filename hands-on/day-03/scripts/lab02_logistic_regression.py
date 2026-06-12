"""Lab 2 — Logistic regression for loan default prediction."""

from __future__ import annotations

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from _data import NUMERIC_FEATURES, load_loans

df = load_loans()
X = df[NUMERIC_FEATURES]
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

proba = model.predict_proba(X_test.head(3))[:, 1]
pred = model.predict(X_test.head(3))

print("Lab 2 — Logistic regression")
print(f"train size: {len(X_train)}, test size: {len(X_test)}")
print(f"default rate (train): {y_train.mean():.4f}")
print(f"intercept: {model.intercept_[0]:.4f}")
print(f"coefficients: {dict(zip(NUMERIC_FEATURES, model.coef_[0].round(4)))}")
print(f"sample P(default): {proba.round(4)}")
print(f"sample predictions: {pred.tolist()}")
