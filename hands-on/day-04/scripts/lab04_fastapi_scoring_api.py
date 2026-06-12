"""Lab 4 — FastAPI scoring API with TestClient (no live server required)."""

from __future__ import annotations

import pandas as pd
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from _data import NUMERIC_FEATURES, load_loans

df = load_loans()
X = df[NUMERIC_FEATURES]
y = df["default"]
X_train, _, y_train, _ = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = Pipeline(
    steps=[
        ("scale", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=5)),
    ]
)
model.fit(X_train, y_train)


class LoanRequest(BaseModel):
    loan_amnt: float = Field(..., gt=0)
    int_rate: float = Field(..., ge=0)
    annual_inc: float = Field(..., gt=0)
    dti: float = Field(..., ge=0)
    installment: float = Field(..., gt=0)


class LoanPrediction(BaseModel):
    default_probability: float
    default_label: int


app = FastAPI(title="Lending Club Scoring API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=LoanPrediction)
def predict(loan: LoanRequest) -> LoanPrediction:
    features = pd.DataFrame(
        [[loan.loan_amnt, loan.int_rate, loan.annual_inc, loan.dti, loan.installment]],
        columns=NUMERIC_FEATURES,
    )
    proba = float(model.predict_proba(features)[0][1])
    label = int(proba >= 0.5)
    return LoanPrediction(default_probability=round(proba, 4), default_label=label)


client = TestClient(app)

health = client.get("/health")
sample = {
    "loan_amnt": 15000,
    "int_rate": 12.5,
    "annual_inc": 65000,
    "dti": 18.0,
    "installment": 450.0,
}
response = client.post("/predict", json=sample)

print("Lab 4 — FastAPI scoring API")
print(f"GET /health -> {health.status_code} {health.json()}")
print(f"POST /predict -> {response.status_code}")
print(f"response body: {response.json()}")
