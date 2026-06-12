"""Shared paths for Day 1 lab scripts (skipped by dry-run)."""

from pathlib import Path

GH_ROOT = Path(__file__).resolve().parents[3]
TEAM_SALES_CSV = GH_ROOT / "hands-on" / "day-01" / "data" / "team_sales.csv"
