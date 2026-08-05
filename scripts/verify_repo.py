#!/usr/bin/env python3
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
metadata = json.loads((root / "project.json").read_text())
required = [
    "README.md",
    "AGENTS.md",
    "project.json",
    "docs/architecture.md",
    *metadata.get("required_paths", []),
]
missing = [path for path in required if not (root / path).exists()]
if missing:
    raise SystemExit(f"missing required paths: {missing}")
if metadata.get("preserves_existing_site") is not True:
    raise SystemExit("marketing metadata must preserve the existing site")
for path in root.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.stat().st_size > 1_000_000:
        continue
    try:
        text = path.read_text()
    except UnicodeDecodeError:
        continue
    if any(marker in text for marker in ("<" * 7, "=" * 7, ">" * 7)):
        raise SystemExit(f"conflict marker in {path}")
    if re.search(
        r"gh[pousr]_[A-Za-z0-9]{20,}|lin_api_[A-Za-z0-9]{20,}|BEGIN [A-Z ]*PRIVATE KEY",
        text,
    ):
        raise SystemExit(f"credential-shaped content in {path}")
print(f"validated {metadata['organization']}/{metadata['repository']}")
