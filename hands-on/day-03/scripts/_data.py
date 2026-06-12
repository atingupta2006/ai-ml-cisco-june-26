"""Shared Lending Club loading helpers (skipped by dry-run)."""

from __future__ import annotations

import pandas as pd

from _paths import LENDING_CLUB_CSV

DEFAULT_STATUSES = {"Charged Off", "Late (31-120 days)"}
NUMERIC_FEATURES = ["loan_amnt", "int_rate", "annual_inc", "dti", "installment"]
CATEGORICAL_FEATURES = ["grade", "term"]


def load_loans() -> pd.DataFrame:
    df = pd.read_csv(LENDING_CLUB_CSV)
    df["default"] = df["loan_status"].isin(DEFAULT_STATUSES).astype(int)
    return df
