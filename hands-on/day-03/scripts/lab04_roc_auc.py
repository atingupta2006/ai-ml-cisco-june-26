"""Lab 4 — ROC curve and AUC."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import auc, roc_curve
from sklearn.model_selection import train_test_split

from _data import NUMERIC_FEATURES, load_loans
from _paths import GH_ROOT

OUTPUT_DIR = GH_ROOT / "hands-on" / "day-03" / "scripts" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = load_loans()
X = df[NUMERIC_FEATURES]
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)
y_scores = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

fig, ax = plt.subplots(figsize=(5, 4))
ax.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
ax.plot([0, 1], [0, 1], linestyle="--", color="gray", label="random")
ax.set_xlabel("False positive rate")
ax.set_ylabel("True positive rate")
ax.set_title("ROC — loan default model")
ax.legend(loc="lower right")
fig.tight_layout()

roc_plot = OUTPUT_DIR / "roc_curve.png"
fig.savefig(roc_plot, dpi=100)
plt.close(fig)

print("Lab 4 — ROC and AUC")
print(f"ROC points: {len(fpr)}")
print(f"AUC: {roc_auc:.4f}")
print(f"plot saved: {roc_plot.name}")
print(f"threshold at index 10: {thresholds[10]:.4f}")
