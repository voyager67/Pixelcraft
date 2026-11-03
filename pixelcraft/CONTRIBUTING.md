# Contributing

Pixelcraft accepts contributions that materially improve AI-slop recognition, evidence quality, or UI remediation.

## In scope

- New observable slop patterns and false-positive guidance.
- Focused remediation skills for specific interface patterns.
- Better verification, accessibility, responsive, visual, and trust checks.
- Improvements to skill selection, examples, and repository security scanning.

## Out of scope

- Generic product management or app-building skills unrelated to slop.
- AI-authorship detection claims based on visual stereotypes.
- Style-only preferences presented as objective defects.
- Skills that invent data, endorsements, product capabilities, or customer claims.

## Before submitting

- Keep each skill self-contained in `skills/<name>/SKILL.md`.
- Add valid frontmatter and a meaningful workflow.
- Add evidence, benign alternatives, and a clear output format.
- Mark license metadata correctly; do not apply CC BY-NC to the Unslop adaptation.
- Run `python3 scripts/validate_skills.py` and `python3 scripts/security_audit.py`.
- Do not include screenshots with personal/customer information, keys, tokens, or private files.
