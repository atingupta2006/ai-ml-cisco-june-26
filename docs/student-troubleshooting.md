# Student troubleshooting

## Setup

| Problem | Solution |
|---------|----------|
| `python` not found | Install **Python 3.10+**; on Windows check “Add to PATH” |
| `ModuleNotFoundError: pandas` (etc.) | Run setup again: `setup_student_env.ps1` or `setup_student_env.sh` |
| Notebook runs but imports fail | Kernel must be **Python (cisco-aiml-lab)** — not “Python 3” system kernel |
| `No module named matplotlib` | Same as above — wrong kernel |

**Register kernel manually (if needed):**

```bash
source .venv/bin/activate   # Windows: .\.venv\Scripts\Activate.ps1
python -m ipykernel install --user --name cisco-aiml-lab --display-name "Python (cisco-aiml-lab)"
```

## Paths & data

| Problem | Solution |
|---------|----------|
| CSV not found | Start Jupyter from `hands-on/day-NN/notebooks/` or run all cells (path logic finds `data/`) |
| Row count wrong (not 500/1000) | Use files in `data/` only — not full Kaggle downloads |
| Checkpoint assert failed | Compare with **Example result** in `labs.md`; ask instructor before changing data |
## Day-specific

| Day | Issue | Fix |
|-----|-------|-----|
| 01 | Excel stats differ from notebook | Use `STDEV.S`, all 20 rows |
| 01 | Lab 6 pivot wrong | Pivot on `region`, not `team` |
| 04 | FastAPI deprecation warning | Ignore in class |
| 04 | MLflow UI won’t open | See [mlflow-ui-demo-setup.md](mlflow-ui-demo-setup.md) |
| 05 | “500 rows” vs 25 symbols | Labs cluster **25 symbols** (aggregated features) |

## Still stuck?

1. Re-run setup script  
2. Restart Jupyter after activating venv  
3. Ask instructor with screenshot of **full error** and **kernel name** (top-right in Jupyter)
