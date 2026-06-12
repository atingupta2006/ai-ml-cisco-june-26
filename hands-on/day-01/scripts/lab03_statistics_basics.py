"""Lab 3 — Descriptive statistics on team sales sample."""

from __future__ import annotations

import pandas as pd

from _paths import TEAM_SALES_CSV

df = pd.read_csv(TEAM_SALES_CSV)
sales = df["q2_sales"]

print("Lab 3 — Statistics basics")
print(f"rows: {len(df)}")
print(f"mean q2_sales: {sales.mean():.2f}")
print(f"median q2_sales: {sales.median():.2f}")
print(f"std q2_sales: {sales.std(ddof=1):.2f}")
print(f"min / max q2_sales: {sales.min()} / {sales.max()}")
