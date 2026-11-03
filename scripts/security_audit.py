#!/usr/bin/env python3
"""Best-effort local secret/private-file scanner; never prints matched values."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 2_000_000
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}
SENSITIVE_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".sqlite", ".db", ".keystore"}
SENSITIVE_NAMES = {".env", "id_rsa", "id_ed25519", "credentials.json", "secrets.json"}
PATTERNS = {
    "private-key-block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "github-token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "github-fine-grained-token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "gitlab-token": re.compile(r"\bglpat-[A-Za-z0-9_-]{20,}\b"),
    "huggingface-token": re.compile(r"\bhf_[A-Za-z0-9]{20,}\b"),
    "npm-token": re.compile(r"\bnpm_[A-Za-z0-9]{30,}\b"),
    "pypi-token": re.compile(r"\bpypi-[A-Za-z0-9_-]{30,}\b"),
    "aws-access-key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "slack-token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "google-api-key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    "openai-style-key": re.compile(r"\bsk-(?:proj-|live-)?[A-Za-z0-9_-]{24,}\b"),
    "anthropic-style-key": re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}\b"),
    "stripe-secret-key": re.compile(r"\bsk_(?:live|test)_[A-Za-z0-9]{16,}\b"),
    "sendgrid-token": re.compile(r"\bSG\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\b"),
    "cloudflare-token": re.compile(r"\bv[1-9]\.0-[A-Za-z0-9_-]{20,}\b"),
    "jwt-like-token": re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
    "credential-assignment": re.compile(r"(?i)\b(?:api[_-]?key|client[_-]?secret|access[_-]?token|password|private[_-]?key)\s*[:=]\s*[\"'][^\"']{10,}[\"']"),
    "credential-url": re.compile(r"https?://[^/\s:@]+:[^/\s@]{8,}@[^/\s]+"),
    "bearer-secret": re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/-]{24,}={0,2}"),
    "personal-email": re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"),
    "local-home-path": re.compile(r"(?i)(?:/Users/|/home/|[A-Z]:\\Users\\)[A-Za-z0-9._-]+"),
}

findings = []
for path in ROOT.rglob("*"):
    if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
        continue
    relative = path.relative_to(ROOT)
    if path.name.lower() in SENSITIVE_NAMES or path.name.lower().startswith(".env.") or path.suffix.lower() in SENSITIVE_SUFFIXES:
        findings.append((str(relative), 1, "sensitive-filename"))
    if path.stat().st_size > MAX_BYTES:
        findings.append((str(relative), 1, "unexpected-large-file-review"))
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        findings.append((str(relative), 1, "binary-file-review"))
        continue
    for label, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            # The report deliberately excludes the matched value.
            findings.append((str(relative), line, label))

if findings:
    print("Potential security/privacy findings (values are intentionally withheld):")
    for filename, line, label in sorted(set(findings)):
        print(f"- {filename}:{line}: {label}")
    sys.exit(1)

print("OK: no matches for configured secret patterns or sensitive file types.")
print("Manual review is still required; this scanner is not a guarantee.")
