"""Lab 3 — Load and explore the Zomato restaurants dataset with Pandas."""

from __future__ import annotations

import pandas as pd

from _paths import ZOMATO_CSV

df = pd.read_csv(ZOMATO_CSV)

print("Lab 3 — Pandas Zomato load")
print(f"dataset path: {ZOMATO_CSV.name}")
print(f"shape (rows, cols): {df.shape}")
print(f"columns: {list(df.columns)}")
print()
print("head(3):")
print(df.head(3).to_string(index=False))
print()
print("describe (numeric):")
print(df.describe().round(2).to_string())
