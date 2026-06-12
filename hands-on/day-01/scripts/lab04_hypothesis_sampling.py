"""Lab 4 — Sampling and a simple growth hypothesis check."""

from __future__ import annotations

import pandas as pd

from _paths import TEAM_SALES_CSV

df = pd.read_csv(TEAM_SALES_CSV)

population_mean = df["q2_sales"].mean()
sample = df.sample(n=10, random_state=42)
sample_mean = sample["q2_sales"].mean()

df["growth"] = df["q2_sales"] > df["q1_sales"]
growth_rate = df["growth"].mean()
north_growth = df.loc[df["region"] == "North", "growth"].mean()

print("Lab 4 — Hypothesis and sampling")
print(f"population mean q2_sales: {population_mean:.2f}")
print(f"sample size: {len(sample)}")
print(f"sample mean q2_sales: {sample_mean:.2f}")
print(f"H1: q2 > q1 growth rate (all teams): {growth_rate:.2f}")
print(f"North region growth rate: {north_growth:.2f}")
