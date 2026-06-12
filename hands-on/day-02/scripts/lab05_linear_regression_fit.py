"""Lab 5 — Fit linear regression to predict restaurant ratings."""

from __future__ import annotations

import pandas as pd
from sklearn.linear_model import LinearRegression

from _paths import ZOMATO_CSV

df = pd.read_csv(ZOMATO_CSV)

features = df[["votes", "average_cost_for_two"]]
target = df["aggregate_rating"]

model = LinearRegression()
model.fit(features, target)

predictions = model.predict(features.head(3))

print("Lab 5 — Linear regression fit")
print(f"training rows: {len(df)}")
print(f"intercept: {model.intercept_:.4f}")
print(f"coefficients [votes, cost]: {model.coef_.round(4)}")
print(f"sample predictions (first 3): {predictions.round(2)}")
print(f"actual ratings (first 3): {target.head(3).tolist()}")
