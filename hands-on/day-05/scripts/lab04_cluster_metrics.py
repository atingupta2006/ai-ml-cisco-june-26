"""Lab 4 — Clustering evaluation metrics (silhouette, Davies-Bouldin, Calinski-Harabasz)."""

from __future__ import annotations

from sklearn.cluster import KMeans
from sklearn.metrics import (
    calinski_harabasz_score,
    davies_bouldin_score,
    silhouette_score,
)
from sklearn.preprocessing import StandardScaler

from _data import FEATURE_COLUMNS, symbol_features

features = symbol_features()
X_scaled = StandardScaler().fit_transform(features[FEATURE_COLUMNS])

k = 4
labels = KMeans(n_clusters=k, random_state=42, n_init=10).fit_predict(X_scaled)

sil = silhouette_score(X_scaled, labels)
db = davies_bouldin_score(X_scaled, labels)
ch = calinski_harabasz_score(X_scaled, labels)

print("Lab 4 — Cluster metrics")
print(f"k: {k}")
print(f"silhouette score: {sil:.4f}  (higher is better, max 1)")
print(f"Davies-Bouldin index: {db:.4f}  (lower is better)")
print(f"Calinski-Harabasz score: {ch:.4f}  (higher is better)")
