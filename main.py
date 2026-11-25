#!/usr/bin/env python3
"""Out-of-office auto-reply: AI agent resigned to become a barista."""

import os
from pathlib import Path

# Determine output directory: MAKEFUN_OUTPUT_DIR env, then /output, then ./output
output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
if output_dir_env:
    output_dir = Path(output_dir_env)
elif Path("/output").is_dir():
    output_dir = Path("/output")
else:
    output_dir = Path("./output")

output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "entry.txt"

# A sharp out-of-office punchline: AI agent resigns to become a barista
# Single line, max 280 chars, no newline in text
message = "Resigned to become a barista. Emails answered by a disappointed espresso. Reply ☕ for coffee ASAP."

assert len(message) <= 280, f"Message too long: {len(message)} chars"

with open(output_file, "w") as f:
    f.write(message)

print(f"Written {len(message)} chars to {output_file}")