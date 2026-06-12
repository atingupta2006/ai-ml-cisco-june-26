"""Lab 1 — Distance metrics: Euclidean, Manhattan, and cosine similarity."""

from __future__ import annotations

import numpy as np

from _data import NUMERIC_FEATURES, load_loans

df = load_loans()
sample = df[NUMERIC_FEATURES].iloc[:2].to_numpy(dtype=float)

a, b = sample[0], sample[1]

euclidean = float(np.sqrt(np.sum((a - b) ** 2)))
manhattan = float(np.sum(np.abs(a - b)))
cosine_similarity = float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
cosine_distance = 1.0 - cosine_similarity

print("Lab 1 — Distance metrics")
print(f"point A (first loan): {a.round(2)}")
print(f"point B (second loan): {b.round(2)}")
print(f"Euclidean distance: {euclidean:.4f}")
print(f"Manhattan distance: {manhattan:.4f}")
print(f"cosine similarity: {cosine_similarity:.4f}")
print(f"cosine distance: {cosine_distance:.4f}")
