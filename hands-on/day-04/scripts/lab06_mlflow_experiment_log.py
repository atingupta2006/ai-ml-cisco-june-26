"""Lab 6 — Log KNN experiment with MLflow; version metrics.json with DVC."""

from __future__ import annotations

import json
import subprocess

import mlflow
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from _data import NUMERIC_FEATURES, load_loans
from _paths import GH_ROOT, OUTPUT_DIR

SCRIPTS_DIR = GH_ROOT / "hands-on" / "day-04" / "scripts"
METRICS_REL = "output/metrics.json"


def dvc_track_metrics() -> None:
    """Initialize DVC in scripts/ (no-scm) and track metrics.json."""
    if not SCRIPTS_DIR.is_dir():
        raise FileNotFoundError(SCRIPTS_DIR)

    if not (SCRIPTS_DIR / ".dvc").is_dir():
        proc = subprocess.run(
            ["dvc", "init", "--no-scm"],
            cwd=SCRIPTS_DIR,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr or proc.stdout)

    proc = subprocess.run(
        ["dvc", "add", METRICS_REL],
        cwd=SCRIPTS_DIR,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or proc.stdout)

    status = subprocess.run(
        ["dvc", "status"],
        cwd=SCRIPTS_DIR,
        capture_output=True,
        text=True,
    )
    print(status.stdout or status.stderr)

    dvc_file = SCRIPTS_DIR / f"{METRICS_REL}.dvc"
    if not dvc_file.is_file():
        raise FileNotFoundError(f"DVC pointer not created: {dvc_file}")


df = load_loans()
X = df[NUMERIC_FEATURES]
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

k = 7
model = Pipeline(
    steps=[
        ("scale", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=k)),
    ]
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
mlflow_db = OUTPUT_DIR / "mlflow.db"
mlflow.set_tracking_uri(f"sqlite:///{mlflow_db.as_posix()}")
mlflow.set_experiment("cisco-aiml-day04-lending-club")

with mlflow.start_run(run_name="knn-baseline") as run:
    mlflow.log_param("model", "KNeighborsClassifier")
    mlflow.log_param("k", k)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, artifact_path="model")
    run_id = run.info.run_id

metrics_path = OUTPUT_DIR / "metrics.json"
metrics_path.write_text(
    json.dumps({"accuracy": round(accuracy, 4), "k": k, "run_id": run_id}),
    encoding="utf-8",
)

dvc_track_metrics()

print("Lab 6 — MLflow experiment log")
print(f"experiment: cisco-aiml-day04-lending-club")
print(f"run_id: {run_id}")
print(f"accuracy: {accuracy:.4f}")
print(f"tracking db: {mlflow_db.name}")
print(f"metrics artifact: {metrics_path.name}")
print(f"DVC pointer: {METRICS_REL}.dvc")
