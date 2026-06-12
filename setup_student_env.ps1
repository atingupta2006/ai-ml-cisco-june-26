# One-time setup — Windows PowerShell
$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $RepoRoot

$Py = $env:PY
if (-not $Py) {
    if (Test-Path "$env:USERPROFILE\miniconda3\python.exe") {
        $Py = "$env:USERPROFILE\miniconda3\python.exe"
    } else {
        $Py = "python"
    }
}

Write-Host "==> Python: $(& $Py --version)"
& $Py -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)"
if ($LASTEXITCODE -ne 0) {
    Write-Error "Python 3.10+ required. Install from python.org or miniconda."
}

if (-not (Test-Path ".venv")) {
    & $Py -m venv .venv
}
& ".\.venv\Scripts\Activate.ps1"

python -m pip install -q --upgrade pip
python -m pip install -q -r requirements-student.txt

python -m ipykernel install --user --name cisco-aiml-lab --display-name "Python (cisco-aiml-lab)"

Get-ChildItem "hands-on\day-*\scripts" -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    New-Item -ItemType Directory -Force -Path (Join-Path $_.FullName "output") | Out-Null
}

Write-Host ""
Write-Host "==> Setup complete"
Write-Host "    Activate:  .\.venv\Scripts\Activate.ps1"
Write-Host "    Jupyter:   cd hands-on\day-01\notebooks"
Write-Host "               jupyter lab"
Write-Host "    Kernel:    Python (cisco-aiml-lab)"
