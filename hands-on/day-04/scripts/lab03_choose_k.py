"""Lab 3 — Choose the best K for KNN using validation accuracy."""

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

k_values = [1, 3, 5, 7, 9, 11, 15]
results: list[tuple[int, float]] = []

for k in k_values:
    pipe = Pipeline(
        steps=[
            ("scale", StandardScaler()),
            ("knn", KNeighborsClassifier(n_neighbors=k)),
        ]
    )
    pipe.fit(X_train, y_train)
    acc = accuracy_score(y_test, pipe.predict(X_test))
    results.append((k, acc))

best_k, best_acc = max(results, key=lambda item: item[1])

print("Lab 3 — Choose K")
print("k\taccuracy")
for k, acc in results:
    marker = " <-- best" if k == best_k else ""
    print(f"{k}\t{acc:.4f}{marker}")
print(f"best k: {best_k} (accuracy {best_acc:.4f})")
