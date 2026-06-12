# Student quick start

## 1. Get the materials

```bash
git clone https://github.com/atingupta2006/ai-ml-cisco-june-26.git
cd ai-ml-cisco-june-26
```

## 2. One-time environment setup

| OS | Command |
|----|---------|
| **Windows** | `.\setup_student_env.ps1` |
| **Linux / Mac / WSL** | `chmod +x setup_student_env.sh && ./setup_student_env.sh` |

Requirements: **Python 3.10+**, ~5 GB disk, **8 GB RAM** (16 GB recommended).

## 3. Start Day 1

```bash
source .venv/bin/activate          # Windows: .\.venv\Scripts\Activate.ps1
cd hands-on/day-01/notebooks
jupyter lab
```

Select kernel: **Python (cisco-aiml-lab)**.

Read [lab execution guide](lab-execution-guide.md) before Lab 1.

## 4. Each day

| Day | Folder | Notes |
|-----|--------|-------|
| 01 | [day-01](../hands-on/day-01/README.md) | Excel for Lab 6; worksheets Labs 1–2, 5 |
| 02 | [day-02](../hands-on/day-02/README.md) | Zomato 500 rows |
| 03 | [day-03](../hands-on/day-03/README.md) | Lending Club classification |
| 04 | [day-04](../hands-on/day-04/README.md) | KNN, FastAPI, MLflow |
| 05 | [day-05](../hands-on/day-05/README.md) | NYSE clustering |
| 06 | [day-06](../hands-on/day-06/README.md) | Credit card fraud |

## Datasets

| Dataset | Used from day |
|---------|----------------|
| Team sales | Day 1 |
| Zomato restaurants | Day 2 |
| Lending Club | Days 3–4 |
| NYSE stocks | Day 5 |
| Credit card transactions | Day 6 |

## Help

- [Troubleshooting](student-troubleshooting.md)
- [Syllabus coverage](syllabus-coverage.md)
