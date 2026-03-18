```markdown
# Setup GitHub Secrets

This repository is prepared to read API keys from GitHub Actions secrets.

## Required secrets

Create these two repository secrets:

- `OPENAI_API_KEY`
- `HF_TOKEN`

## How to add them

1. Open your GitHub repository.
2. Go to **Settings**.
3. In the left sidebar, open **Secrets and variables**.
4. Click **Actions**.
5. Click **New repository secret**.
6. Add the secret name and value.
7. Save.
8. Repeat for the second key.

## Recommended naming

Use these exact names so the workflow works without edits:

- `OPENAI_API_KEY`
- `HF_TOKEN`

## Notes

- Do not commit API keys into source control.
- Do not place live API keys directly in workflow YAML.
- For local development, use a local `.env` file that is ignored by Git.
- For future staging or production separation, move secrets to GitHub Environments.
