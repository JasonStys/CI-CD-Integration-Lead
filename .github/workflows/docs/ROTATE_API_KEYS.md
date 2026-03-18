# API Key Rotation Guide

This document explains how to rotate the API keys used by this repository.

## Keys currently expected by the repo

- `OPENAI_API_KEY`
- `HF_TOKEN`

## When to rotate

Rotate keys when:

- a key may have been exposed
- a team member with access leaves the project
- your sponsor requests regular credential rotation
- you want to replace a test key with a production approved key

## Rotation process

### OpenAI

1. Sign in to the OpenAI platform for the project account.
2. Create a new API key.
3. Copy the new key immediately and store it securely.
4. In GitHub, open the repository.
5. Go to **Settings** → **Secrets and variables** → **Actions**.
6. Update the `OPENAI_API_KEY` secret with the new value.
7. Save the secret.
8. Revoke or delete the old key in OpenAI after confirming the new key works.
9. Re run the GitHub Actions workflow to validate the update.

### Hugging Face

1. Sign in to the Hugging Face account used for the project.
2. Create a new access token.
3. Copy the new token immediately and store it securely.
4. In GitHub, open the repository.
5. Go to **Settings** → **Secrets and variables** → **Actions**.
6. Update the `HF_TOKEN` secret with the new value.
7. Save the secret.
8. Revoke the old token in Hugging Face after confirming the new one works.
9. Re run the GitHub Actions workflow to validate the update.

## Validation checklist

After rotating a key:

- confirm the secret exists in GitHub
- trigger the workflow manually
- confirm the workflow still passes
- confirm no secret values were printed to logs
- confirm the old key is revoked

## Security reminders

- Never paste API keys into commits, issues, or pull requests.
- Never hardcode keys into Python files.
- Never place secrets in README files.
- Keep `.env` local only.
