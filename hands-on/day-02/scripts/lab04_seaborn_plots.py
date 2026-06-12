"""Lab 4 — Seaborn visualizations on Zomato data."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from _paths import GH_ROOT, ZOMATO_CSV

OUTPUT_DIR = GH_ROOT / "hands-on" / "day-02" / "scripts" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(ZOMATO_CSV)
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

sns.histplot(df["aggregate_rating"], bins=15, kde=True, ax=axes[0])
axes[0].set_title("Distribution of aggregate rating")

top_cities = df["city"].value_counts().head(5).index
city_subset = df[df["city"].isin(top_cities)]
sns.boxplot(data=city_subset, x="city", y="average_cost_for_two", ax=axes[1])
axes[1].set_title("Cost for two — top 5 cities")
axes[1].tick_params(axis="x", rotation=30)

fig.tight_layout()
rating_plot = OUTPUT_DIR / "rating_distribution.png"
fig.savefig(rating_plot, dpi=100)
plt.close(fig)

city_means = df.groupby("city")["average_cost_for_two"].mean().sort_values(ascending=False)

print("Lab 4 — Seaborn plots")
print(f"rating plot saved: {rating_plot.name}")
print(f"mean rating: {df['aggregate_rating'].mean():.2f}")
print(f"top city by avg cost: {city_means.index[0]} ({city_means.iloc[0]:.0f})")
