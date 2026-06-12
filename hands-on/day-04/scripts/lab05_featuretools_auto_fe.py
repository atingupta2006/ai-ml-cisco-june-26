"""Lab 5 — Automated feature engineering with FeatureTools DFS."""

from __future__ import annotations

import featuretools as ft

from _data import load_loans

dfs_cols = [
    "loan_id",
    "loan_amnt",
    "int_rate",
    "annual_inc",
    "dti",
    "installment",
    "default",
]
df = load_loans()[dfs_cols].copy()
df["loan_id"] = df["loan_id"].astype(str)

es = ft.EntitySet(id="lending")
es = es.add_dataframe(
    dataframe_name="loans",
    dataframe=df,
    index="loan_id",
)

feature_matrix, feature_defs = ft.dfs(
    entityset=es,
    target_dataframe_name="loans",
    max_depth=1,
    verbose=False,
)

numeric_cols = [
    c for c in feature_matrix.columns
    if c != "default" and str(feature_matrix[c].dtype) != "category"
]
top_corr = (
    feature_matrix[numeric_cols + ["default"]]
    .corr(numeric_only=True)["default"]
    .drop("default", errors="ignore")
    .abs()
    .sort_values(ascending=False)
)

print("Lab 5 — FeatureTools auto FE")
print(f"input columns: {len(df.columns)}")
print(f"engineered features: {len(feature_defs)}")
print(f"feature matrix shape: {feature_matrix.shape}")
print("top |corr| with default (first 3):")
for name, val in top_corr.head(3).items():
    print(f"  {name}: {val:.4f}")
