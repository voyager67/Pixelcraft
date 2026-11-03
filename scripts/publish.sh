#!/usr/bin/env bash
set -euo pipefail

OWNER="voyager67"
REPO_NAME="pixelcraft"
FULL_REPO="${OWNER}/${REPO_NAME}"
DESCRIPTION="A focused AI-slop recognition and remediation skill library for ChatGPT and Codex."

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required. Install it from https://cli.github.com/ and run: gh auth login" >&2
  exit 1
fi
if ! command -v git >/dev/null 2>&1; then
  echo "Git is required." >&2
  exit 1
fi

LOGIN="$(gh api user --jq .login)"
if [[ "${LOGIN}" != "${OWNER}" ]]; then
  echo "Authenticated GitHub account is '${LOGIN}', expected '${OWNER}'. Refusing to publish to the wrong account." >&2
  exit 1
fi

if gh repo view "${FULL_REPO}" >/dev/null 2>&1; then
  echo "${FULL_REPO} already exists. This script will not overwrite or force-push it." >&2
  echo "Review the remote first, then publish intentionally." >&2
  exit 1
fi

python3 scripts/validate_skills.py
python3 scripts/security_audit.py

if [[ -e .git ]]; then
  echo "A .git directory or file already exists here. Refusing to publish an existing repository or its history." >&2
  echo "Extract the clean Pixelcraft archive into a new, empty directory and run this script there." >&2
  exit 1
fi

git init --initial-branch=main
# Commit metadata is public. Use GitHub's account-specific noreply address,
# never the email from the user's global Git configuration.
GITHUB_ID="$(gh api user --jq .id)"
git config user.name "${OWNER}"
git config user.email "${GITHUB_ID}+${OWNER}@users.noreply.github.com"

git add --all
git diff --cached --check
git commit -m "Initial Pixelcraft skill library"
gh repo create "${FULL_REPO}" --public --source=. --remote=origin --push --description "${DESCRIPTION}"
gh repo edit "${FULL_REPO}" --enable-issues --enable-discussions --add-topic agent-skills --add-topic ai-slop --add-topic ui-design --add-topic ux-design --add-topic codex --add-topic chatgpt --add-topic frontend --add-topic design-systems --add-topic accessibility --add-topic design-quality
if ! gh repo edit "${FULL_REPO}" --enable-secret-scanning --enable-secret-scanning-push-protection; then
  echo "Warning: enable secret scanning and push protection manually in GitHub repository settings." >&2
fi

echo "Published https://github.com/${FULL_REPO}"
