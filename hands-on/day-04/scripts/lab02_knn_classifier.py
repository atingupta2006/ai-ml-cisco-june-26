"""Lab 2 — K-Nearest Neighbors classifier for loan default."""

from __future__ import annotations

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from _data import NUMERIC_FEATURES, load_loans

df = load_loans()
X = df[NUMERIC_FEATURES]
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipe = Pipeline(
    steps=[
        ("scale", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=5)),
    ]
)
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Lab 2 — KNN classifier")
print(f"train size: {len(X_train)}, test size: {len(X_test)}")
print(f"k (neighbors): 5")
print(f"test accuracy: {accuracy:.4f}")
print(f"sample predictions (first 5): {y_pred[:5].tolist()}")
