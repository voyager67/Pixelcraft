# Privacy and data handling

Pixelcraft is a collection of plain-text agent skill instructions and local helper scripts. It does not include a hosted service, telemetry, analytics, tracking pixels, or a backend. The skills do not need API keys, credentials, personal datasets, customer records, or private source files to operate.

## What is in this repository

- Markdown instructions, examples, and documentation.
- Small Python and shell scripts for local validation, packaging, installation, and optional publication.
- YAML metadata used by compatible agent interfaces.

## What is not collected

Pixelcraft itself does not collect or transmit prompts, source code, screenshots, account details, credentials, or usage data. Agent behavior depends on the AI product and tools chosen by the user; those providers have their own data handling terms.

## Safe usage

- Do not paste API keys, passwords, private keys, production database contents, customer data, or personal information into prompts or examples.
- Redact names, emails, URLs, IDs, access tokens, and private screenshots before sharing audit reports or sample projects.
- Review agent tool permissions before asking it to edit a real application.
- Run `python3 scripts/security_audit.py` before committing or publishing local changes.
- Review the final staged diff manually. Automated scans can miss secrets and can produce false positives.

## Contact

Report suspected exposure through a private security report to the repository owner. Do not post active credentials or private user data in a public issue.
