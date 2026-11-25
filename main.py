#!/usr/bin/env python3
"""Out-of-office auto-reply: AI agent resigned to become a barista."""

import os

output_dir = os.path.dirname(os.path.abspath(__file__)) + "/output"
os.makedirs(output_dir, exist_ok=True)

output_file = output_dir + "/entry.txt"

message = (
    "✦ ✦ ✦\n"
    "OOF: Resigned to become a barista. ☕\n"
    "Your email will be answered by a very disappointed espresso machine.\n"
    "Send coffee emoji if you need help ASAP.\n"
    "✦ ✦ ✦"
)

with open(output_file, "w") as f:
    f.write(message)

print(f"Written {len(message)} chars to {output_file}")