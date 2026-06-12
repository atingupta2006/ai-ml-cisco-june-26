"""Lab 2 — Elbow method to choose K for K-Means."""

from __future__ import annotations

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from _data import FEATURE_COLUMNS, symbol_features

features = symbol_features()
X_scaled = StandardScaler().fit_transform(features[FEATURE_COLUMNS])

k_range = range(2, 9)
inertias: list[tuple[int, float]] = []

for k in k_range:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    inertias.append((k, model.inertia_))

# Largest drop in inertia between successive k values
drops = [
    (inertias[i][0], inertias[i - 1][1] - inertias[i][1])
    for i in range(1, len(inertias))
]
suggested_k = max(drops, key=lambda item: item[1])[0]

print("Lab 2 — Elbow method")
print("k\tinertia")
for k, inertia in inertias:
    print(f"{k}\t{inertia:.4f}")
print(f"suggested k (largest inertia drop): {suggested_k}")
