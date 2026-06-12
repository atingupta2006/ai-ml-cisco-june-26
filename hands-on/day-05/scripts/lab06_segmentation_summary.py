"""Lab 6 — Summarize K-Means segments for NYSE symbols."""

from __future__ import annotations

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from _data import FEATURE_COLUMNS, symbol_features

features = symbol_features()
X_scaled = StandardScaler().fit_transform(features[FEATURE_COLUMNS])

k = 4
features = features.copy()
features["segment"] = KMeans(n_clusters=k, random_state=42, n_init=10).fit_predict(X_scaled)

summary = (
    features.groupby("segment")[FEATURE_COLUMNS]
    .mean()
    .round(2)
    .reset_index()
)
segment_sizes = features["segment"].value_counts().sort_index()

print("Lab 6 — Segmentation summary")
print(f"segments (k): {k}")
print(f"symbols per segment: {segment_sizes.to_dict()}")
print()
print("segment means:")
print(summary.to_string(index=False))
print()
print("sample symbols per segment:")
for seg in sorted(features["segment"].unique()):
    symbols = features.loc[features["segment"] == seg, "symbol"].head(4).tolist()
    print(f"  segment {seg}: {symbols}")
