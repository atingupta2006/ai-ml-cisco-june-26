"""Lab 3 — DBSCAN density-based clustering."""

from __future__ import annotations

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

from _data import FEATURE_COLUMNS, symbol_features

features = symbol_features()
X_scaled = StandardScaler().fit_transform(features[FEATURE_COLUMNS])

dbscan = DBSCAN(eps=1.2, min_samples=3)
labels = dbscan.fit_predict(X_scaled)

n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = int(np.sum(labels == -1))

print("Lab 3 — DBSCAN clusters")
print(f"eps: 1.2, min_samples: 3")
print(f"clusters found: {n_clusters}")
print(f"noise points: {n_noise}")
print(f"label counts: {dict(zip(*np.unique(labels, return_counts=True)))}")
