# AI & Machine Learning — Cisco Training (June 2026)

**Duration:** 6 days · **Python 3.10+**

## Start here

1. [Student quick start](docs/student-quick-start.md) — run **`setup_student_env`** once
2. [Lab execution guide](docs/lab-execution-guide.md) — kernel **Python (cisco-aiml-lab)**
3. [Troubleshooting](docs/student-troubleshooting.md)
4. [Course topic checklist](docs/course-topic-checklist.md) — syllabus coverage map
5. [Day 01 labs](hands-on/day-01/README.md)

## Repository layout

```text
├── README.md
├── requirements-student.txt
├── setup_student_env.sh / .ps1
├── docs/                 # guides
├── data/                 # lab datasets (500 / 1000 rows)
└── hands-on/day-01 … day-06/
    ├── notebooks/        # core labs (required)
    └── scripts/          # same labs as .py files
```

## Quick setup

```bash
git clone https://github.com/atingupta2006/ai-ml-cisco-june-26.git
cd ai-ml-cisco-june-26
chmod +x setup_student_env.sh && ./setup_student_env.sh
source .venv/bin/activate
cd hands-on/day-01/notebooks && jupyter lab
```
