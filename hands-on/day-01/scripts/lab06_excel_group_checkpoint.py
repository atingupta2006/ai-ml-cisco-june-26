"""Lab 6 — Excel group checkpoint answers (verify team sales workbook logic)."""

from __future__ import annotations

import pandas as pd

from _paths import TEAM_SALES_CSV

df = pd.read_csv(TEAM_SALES_CSV)

by_region = (
    df.groupby("region")[["q1_sales", "q2_sales"]]
    .sum()
    .assign(growth=lambda x: x["q2_sales"] - x["q1_sales"])
    .round(0)
)

top_region = by_region["q2_sales"].idxmax()
teams_with_growth = int((df["q2_sales"] > df["q1_sales"]).sum())
total_q2 = int(df["q2_sales"].sum())

print("Lab 6 — Excel group checkpoint")
print(f"teams: {len(df)}")
print(f"regions: {df['region'].nunique()}")
print(f"total q2_sales: {total_q2}")
print(f"teams with q2 > q1: {teams_with_growth}")
print(f"top region by q2 total: {top_region}")
print()
print("regional totals:")
print(by_region.to_string())
