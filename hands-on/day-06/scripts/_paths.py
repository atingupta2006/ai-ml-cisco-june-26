"""Shared paths for Day 6 lab scripts (skipped by dry-run)."""

from pathlib import Path

GH_ROOT = Path(__file__).resolve().parents[3]
CREDIT_CARD_CSV = GH_ROOT / "data" / "credit-card" / "credit_card_transactions.csv"
OUTPUT_DIR = GH_ROOT / "hands-on" / "day-06" / "scripts" / "output"
