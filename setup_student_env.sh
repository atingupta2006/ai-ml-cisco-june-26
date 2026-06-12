#!/usr/bin/env bash
# One-time setup — Linux, macOS, WSL, Azure VM
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

if [[ -z "${PY:-}" ]]; then
  if [[ -x "$HOME/miniconda3/bin/python" ]]; then
    PY="$HOME/miniconda3/bin/python"
  elif command -v python3.11 &>/dev/null; then
    PY=python3.11
  elif command -v python3.10 &>/dev/null; then
    PY=python3.10
  else
    PY=python3
  fi
fi

echo "==> Python: $($PY --version)"
if ! $PY -c 'import sys; exit(0 if sys.version_info >= (3, 10) else 1)'; then
  echo "ERROR: Python 3.10+ required. Install miniconda or python3.10."
  exit 1
fi

if [[ ! -d .venv ]]; then
  $PY -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

pip install -q --upgrade pip
pip install -q -r requirements-student.txt

python -m ipykernel install --user --name cisco-aiml-lab --display-name "Python (cisco-aiml-lab)"

for d in hands-on/day-*/scripts/output; do
  mkdir -p "$d"
done

echo ""
echo "==> Setup complete"
echo "    Activate:  source $REPO_ROOT/.venv/bin/activate"
echo "    Jupyter:   cd $REPO_ROOT/hands-on/day-01/notebooks && jupyter lab"
echo "    Kernel:    Python (cisco-aiml-lab)"
