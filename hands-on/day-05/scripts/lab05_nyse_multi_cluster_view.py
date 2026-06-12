"""Lab 5 — Compare K-Means and DBSCAN cluster assignments visually."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN, KMeans
from sklearn.preprocessing import StandardScaler

from _data import symbol_features
from _paths import OUTPUT_DIR

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

features = symbol_features()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features[["avg_close", "volatility", "avg_volume", "avg_range"]])

kmeans_labels = KMeans(n_clusters=4, random_state=42, n_init=10).fit_predict(X_scaled)
dbscan_labels = DBSCAN(eps=1.2, min_samples=3).fit_predict(X_scaled)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

for ax, labels, title in zip(
    axes,
    [kmeans_labels, dbscan_labels],
    ["K-Means (k=4)", "DBSCAN"],
    strict=True,
):
    scatter = ax.scatter(
        features["avg_close"],
        features["volatility"],
        c=labels,
        cmap="tab10",
        alpha=0.85,
    )
    ax.set_xlabel("avg_close")
    ax.set_ylabel("volatility")
    ax.set_title(title)
    fig.colorbar(scatter, ax=ax, label="cluster")

fig.tight_layout()
plot_path = OUTPUT_DIR / "multi_cluster_view.png"
fig.savefig(plot_path, dpi=100)
plt.close(fig)

print("Lab 5 — NYSE multi-cluster view")
print(f"symbols plotted: {len(features)}")
print(f"K-Means cluster counts: {dict(zip(*np.unique(kmeans_labels, return_counts=True)))}")
print(f"DBSCAN cluster counts: {dict(zip(*np.unique(dbscan_labels, return_counts=True)))}")
print(f"plot saved: {plot_path.name}")
