"""Shared paths for Day 2 lab scripts (skipped by dry-run)."""

from pathlib import Path

GH_ROOT = Path(__file__).resolve().parents[3]
ZOMATO_CSV = GH_ROOT / "data" / "zomato" / "zomato_restaurants.csv"
