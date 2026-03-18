# Code Flow

![CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Tests](https://img.shields.io/badge/tests-pytest-brightgreen)
![Coverage Artifacts](https://img.shields.io/badge/coverage-artifacts%20saved-success)

Starter CI/CD scaffold for the AI in SDLC capstone project.

This repository includes:

- GitHub Actions workflow for `pytest` and `coverage`
- uploaded coverage artifacts
- README badges
- secret wiring for OpenAI and Hugging Face tokens
- documentation for setup and key rotation

## Repository structure

```text
.github/workflows/ci.yml
src/codeflow/
tests/
docs/
requirements-dev.txt
.coveragerc
pytest.ini
.env.example
