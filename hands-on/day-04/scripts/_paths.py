"""Shared paths for Day 4 lab scripts (skipped by dry-run)."""

from pathlib import Path

GH_ROOT = Path(__file__).resolve().parents[3]
LENDING_CLUB_CSV = GH_ROOT / "data" / "lending-club" / "lending_club_sample.csv"
OUTPUT_DIR = GH_ROOT / "hands-on" / "day-04" / "scripts" / "output"
