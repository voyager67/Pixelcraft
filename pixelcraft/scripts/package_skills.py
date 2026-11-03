#!/usr/bin/env python3
"""Package each Pixelcraft skill as its own ZIP bundle; no network or credentials."""
from argparse import ArgumentParser
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

parser = ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, default=ROOT / "dist" / "skills", help="Output directory (default: dist/skills)")
parser.add_argument("--skill", help="Package only this skill folder")
args = parser.parse_args()

folders = [SKILLS / args.skill] if args.skill else sorted(p for p in SKILLS.iterdir() if p.is_dir())
if not folders:
    print("No skills found.", file=sys.stderr)
    sys.exit(1)

args.output.mkdir(parents=True, exist_ok=True)
for folder in folders:
    manifest = folder / "SKILL.md"
    if not folder.is_dir() or not manifest.is_file():
        print(f"Invalid skill folder: {folder}", file=sys.stderr)
        sys.exit(1)
    output = args.output / f"{folder.name}.zip"
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for file in sorted(p for p in folder.rglob("*") if p.is_file()):
            archive.write(file, Path(folder.name) / file.relative_to(folder))
    print(f"{output}")

print(f"Packaged {len(folders)} skill(s). These ZIPs are not uploaded anywhere.")
