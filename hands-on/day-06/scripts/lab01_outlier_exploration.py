"""Lab 1 — Explore outliers in transaction amount and distance."""

from __future__ import annotations

import pandas as pd

from _data import load_transactions


def iqr_outlier_count(series: pd.Series) -> int:
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return int(((series < lower) | (series > upper)).sum())


df = load_transactions()

amount_outliers = iqr_outlier_count(df["amount"])
distance_outliers = iqr_outlier_count(df["distance_from_home"])

fraud_amount_mean = df.loc[df["is_fraud"] == 1, "amount"].mean()
legit_amount_mean = df.loc[df["is_fraud"] == 0, "amount"].mean()

print("Lab 1 — Outlier exploration")
print(f"rows: {len(df)}")
print(f"fraud rows: {int(df['is_fraud'].sum())}")
print(f"IQR outliers (amount): {amount_outliers}")
print(f"IQR outliers (distance): {distance_outliers}")
print(f"mean amount (legit): {legit_amount_mean:.2f}")
print(f"mean amount (fraud): {fraud_amount_mean:.2f}")
print(f"max distance (fraud): {df.loc[df['is_fraud'] == 1, 'distance_from_home'].max():.2f}")
