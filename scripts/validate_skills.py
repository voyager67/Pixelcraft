#!/usr/bin/env python3
"""Validate Pixelcraft skill folders using only the Python standard library."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors = []
files = sorted(SKILLS.glob("*/SKILL.md"))

if not files:
    errors.append("No skills found under skills/*/SKILL.md")

for skill_file in files:
    content = skill_file.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        errors.append(f"{skill_file.relative_to(ROOT)}: missing YAML frontmatter")
        continue
    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{skill_file.relative_to(ROOT)}: unterminated frontmatter")
        continue
    frontmatter = parts[1]
    name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", frontmatter)
    description = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
    license_name = re.search(r"(?m)^license:\s*(CC-BY(?:-NC)?-4\.0)\s*$", frontmatter)
    expected = skill_file.parent.name
    if not name:
        errors.append(f"{skill_file.relative_to(ROOT)}: missing/invalid name")
    elif name.group(1) != expected:
        errors.append(f"{skill_file.relative_to(ROOT)}: frontmatter name does not match folder")
    if not description:
        errors.append(f"{skill_file.relative_to(ROOT)}: missing description")
    if not license_name:
        errors.append(f"{skill_file.relative_to(ROOT)}: missing/invalid license metadata")
    if len(content) < 900:
        errors.append(f"{skill_file.relative_to(ROOT)}: skill is too short to be operational")
    for heading in ("## Workflow", "## Output"):
        if heading not in content:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing {heading}")

if errors:
    print("Skill validation failed:")
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)

print(f"OK: validated {len(files)} skills.")
