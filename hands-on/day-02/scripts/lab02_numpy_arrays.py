"""Lab 2 — NumPy arrays and vectorized operations."""

from __future__ import annotations

import numpy as np

votes = np.array([120, 450, 890, 2100, 3400])
costs = np.array([400, 650, 1200, 1800, 2400])

normalized_votes = (votes - votes.mean()) / votes.std()
cost_per_vote = costs / votes

matrix = np.column_stack([votes, costs])
col_means = matrix.mean(axis=0)

print("Lab 2 — NumPy arrays")
print(f"votes shape: {votes.shape}, dtype: {votes.dtype}")
print(f"normalized_votes (first 3): {np.round(normalized_votes[:3], 3)}")
print(f"cost_per_vote (first 3): {np.round(cost_per_vote[:3], 3)}")
print(f"matrix shape: {matrix.shape}")
print(f"column means [votes, cost]: {np.round(col_means, 2)}")
