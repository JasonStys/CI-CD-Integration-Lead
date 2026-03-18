from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"


def run(command: list[str], env: dict[str, str] | None = None) -> None:
    result = subprocess.run(command, cwd=ROOT, env=env)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> None:
    python_exe = VENV_DIR / "Scripts" / "python.exe"
    pytest_exe = VENV_DIR / "Scripts" / "pytest.exe"

    if not python_exe.exists():
        print("Creating virtual environment...")
        run([sys.executable, "-m", "venv", ".venv"])

    print("Installing dependencies...")
    run([str(python_exe), "-m", "pip", "install", "--upgrade", "pip"])
    run([str(python_exe), "-m", "pip", "install", "-r", "requirements-dev.txt"])

    print("Running pytest with coverage...")
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"

    run(
        [
            str(pytest_exe),
            "--cov=src",
            "--cov-config=.coveragerc",
            "--cov-report=term-missing",
            "--cov-report=xml:coverage.xml",
            "--cov-report=html:htmlcov",
        ],
        env=env,
    )

    print()
    print("Done.")
    print("Open htmlcov/index.html to view the coverage report.")


if __name__ == "__main__":
    main()
