"""Shared paths for Day 5 lab scripts (skipped by dry-run)."""

from pathlib import Path

GH_ROOT = Path(__file__).resolve().parents[3]
NYSE_CSV = GH_ROOT / "data" / "nyse" / "nyse_stocks.csv"
OUTPUT_DIR = GH_ROOT / "hands-on" / "day-05" / "scripts" / "output"
