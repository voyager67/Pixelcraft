# Security and privacy

Pixelcraft is a text-first skill collection. It does not require API keys, credentials, network access, telemetry, databases, or third-party runtime dependencies.

## Before publishing

1. Run `python3 scripts/security_audit.py`.
2. Run `python3 scripts/validate_skills.py`.
3. Review the full file list and `git diff --stat` / `git diff --check`.
4. Inspect staged changes before committing. Check for secrets, personal data, private screenshots, customer records, proprietary source code, and unexpected binary files.
5. Enable GitHub secret scanning and push protection where available.

## Scanner limitations

The local scanner uses regular expressions and filename checks. It can produce false positives and can miss unknown token formats, encoded secrets, secrets split across strings, or sensitive information in images. A clean scan is not a guarantee. Review all files manually and use a maintained secret scanner in addition where possible.

## If you find a secret

Do not reproduce its value in issues, logs, or chat. Remove it from the working tree, revoke/rotate it with the provider, and understand that deleting a file in a later commit does not remove it from Git history. If it was already pushed, follow GitHub's sensitive-data removal procedure and check forks/caches as appropriate.

## Reporting

Report repository security issues privately to the repository owner through GitHub's private reporting/contact mechanisms. Do not publish live credentials or exploit details in a public issue.
