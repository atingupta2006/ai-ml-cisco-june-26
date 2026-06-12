"""Shared credit card transaction helpers (skipped by dry-run)."""

from __future__ import annotations

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from _paths import CREDIT_CARD_CSV

NUMERIC_FEATURES = ["amount", "distance_from_home"]
CATEGORICAL_FEATURES = ["merchant_category"]


def load_transactions() -> pd.DataFrame:
    return pd.read_csv(CREDIT_CARD_CSV)


def feature_matrix(df: pd.DataFrame | None = None):
    """Return X, y and a fitted-ready preprocessor."""
    data = load_transactions() if df is None else df
    X = data[NUMERIC_FEATURES + CATEGORICAL_FEATURES]
    y = data["is_fraud"]
    return X, y


def train_test_features(test_size: float = 0.2, random_state: int = 42):
    X, y = feature_matrix()
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)


def build_preprocessor() -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_FEATURES),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
        ]
    )
