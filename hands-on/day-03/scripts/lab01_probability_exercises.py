"""Lab 1 — Probability, odds, and log-odds from loan outcomes."""

from __future__ import annotations

import numpy as np

from _data import load_loans

df = load_loans()

p_default = df["default"].mean()
p_paid = 1 - p_default
odds_default = p_default / p_paid
log_odds = np.log(odds_default)

# Worked example: convert a modeled probability back to odds
p_example = 0.20
odds_example = p_example / (1 - p_example)

print("Lab 1 — Probability exercises")
print(f"rows: {len(df)}")
print(f"P(default): {p_default:.4f}")
print(f"P(fully current/paid): {p_paid:.4f}")
print(f"odds of default: {odds_default:.4f}")
print(f"log-odds (logit): {log_odds:.4f}")
print(f"example P=0.20 -> odds: {odds_example:.4f}")
