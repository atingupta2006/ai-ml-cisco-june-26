"""Lab 5 — End-to-end sklearn Pipeline with preprocessing."""

from __future__ import annotations

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from _data import CATEGORICAL_FEATURES, NUMERIC_FEATURES, load_loans

df = load_loans()
feature_cols = NUMERIC_FEATURES + CATEGORICAL_FEATURES
X = df[feature_cols]
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), NUMERIC_FEATURES),
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
    ]
)

pipe = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("clf", LogisticRegression(max_iter=1000, random_state=42)),
    ]
)

pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Lab 5 — sklearn Pipeline")
print(f"pipeline steps: {[name for name, _ in pipe.steps]}")
print(f"train size: {len(X_train)}, test size: {len(X_test)}")
print(f"test accuracy: {accuracy:.4f}")
print(f"sample predictions (first 5): {y_pred[:5].tolist()}")
