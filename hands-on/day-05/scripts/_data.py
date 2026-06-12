"""Shared NYSE loading and feature helpers (skipped by dry-run)."""

from __future__ import annotations

import pandas as pd

from _paths import NYSE_CSV

FEATURE_COLUMNS = ["avg_close", "volatility", "avg_volume", "avg_range"]


def load_nyse() -> pd.DataFrame:
    return pd.read_csv(NYSE_CSV, parse_dates=["date"])


def symbol_features() -> pd.DataFrame:
    """Per-symbol aggregates for clustering (segmentation)."""
    df = load_nyse()
    df["range"] = df["high"] - df["low"]
    agg = (
        df.groupby("symbol")
        .agg(
            avg_close=("close", "mean"),
            volatility=("close", "std"),
            avg_volume=("volume", "mean"),
            avg_range=("range", "mean"),
        )
        .reset_index()
    )
    agg["volatility"] = agg["volatility"].fillna(0.0)
    return agg
