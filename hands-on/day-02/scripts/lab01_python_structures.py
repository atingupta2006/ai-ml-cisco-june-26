"""Lab 1 — Python data structures (lists, tuples, dicts, sets)."""

from __future__ import annotations

cities = ["Bengaluru", "Mumbai", "Delhi", "Hyderabad"]
ratings = (3.8, 4.2, 3.5, 4.0)

restaurant = {
    "name": "Demo Bistro",
    "city": cities[0],
    "rating": ratings[0],
    "cuisines": {"North Indian", "Chinese"},
}

restaurant["online_order"] = True
restaurant["cuisines"].add("Cafe")

print("Lab 1 — Python structures")
print(f"cities (list, len={len(cities)}): {cities}")
print(f"ratings (tuple): {ratings}")
print(f"restaurant (dict): {restaurant}")
print(f"unique cuisines (set): {sorted(restaurant['cuisines'])}")
