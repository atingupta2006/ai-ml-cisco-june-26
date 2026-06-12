"""Lab 1 — K-Means baseline clustering on NYSE per-symbol features."""

from __future__ import annotations

import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from _data import FEATURE_COLUMNS, symbol_features

features = symbol_features()
X = features[FEATURE_COLUMNS]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

k = 4
model = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = model.fit_predict(X_scaled)

print("Lab 1 — K-Means baseline")
print(f"NYSE rows (daily): see load_nyse(); symbols clustered: {len(features)}")
print(f"features: {FEATURE_COLUMNS}")
print(f"k: {k}")
print(f"inertia: {model.inertia_:.4f}")
unique, counts = np.unique(labels, return_counts=True)
print(f"cluster counts: {dict(zip(unique.tolist(), counts.tolist()))}")
