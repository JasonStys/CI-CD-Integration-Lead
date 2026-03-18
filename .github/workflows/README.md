## Local run without typing terminal commands

For Windows, double click:

`run_local_ci.bat`

That file will:

- create `.venv` if needed
- install dependencies
- run pytest
- generate coverage reports

After it finishes, open:

`htmlcov/index.html`

to view the HTML coverage report.

## GitHub Actions

You do not need to run anything locally for CI.

After you push your files to GitHub, the workflow in:

`.github/workflows/ci.yml`

runs automatically and uploads these artifacts:

- `coverage.xml`
- `htmlcov/`
- `pytest-report.xml`
