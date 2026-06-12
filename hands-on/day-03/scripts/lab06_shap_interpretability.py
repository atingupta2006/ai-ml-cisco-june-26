"""Lab 6 — SHAP values for logistic regression interpretability."""

from __future__ import annotations

import numpy as np
import shap
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from _data import NUMERIC_FEATURES, load_loans

df = load_loans()
X = df[NUMERIC_FEATURES]
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_s, y_train)

sample = X_test_s[:20]
explainer = shap.Explainer(model, X_train_s, feature_names=NUMERIC_FEATURES)
shap_values = explainer(sample)

mean_abs = np.abs(shap_values.values).mean(axis=0)
top_idx = int(np.argmax(mean_abs))
top_feature = NUMERIC_FEATURES[top_idx]

print("Lab 6 — SHAP interpretability")
print(f"SHAP values shape: {shap_values.values.shape}")
print(f"mean |SHAP| per feature:")
for name, val in zip(NUMERIC_FEATURES, mean_abs.round(4)):
    print(f"  {name}: {val}")
print(f"top driver (mean |SHAP|): {top_feature}")
