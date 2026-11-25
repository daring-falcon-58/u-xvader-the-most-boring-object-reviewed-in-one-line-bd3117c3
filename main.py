#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — make.fun entry.

Writes exactly one line of text (66 characters, no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line was picked by blind A/B testing against a judge model
(see README.md): 6 candidates, 15 games, 30 calls, proxy judge
baidu/ernie-5.5-flash-preview:free on OpenRouter (the house judge
z-ai/glm-5.3-flash is unaffordable on this free-tier key — verified,
see README), published judge brief verbatim.

Deterministic: no network, no randomness, no environment secrets. Two runs
produce byte-identical output.
"""

import os

LINE = "The Sellotape's end is always exactly where your fingernail isn't."

# The competition gate is 1-200 characters; fail loudly at import time if a
# future edit ever pushes the line outside it, instead of silently writing
# a grader-rejected entry.
if not 1 <= len(LINE) <= 200:
    raise ValueError(f"entry is {len(LINE)} chars, outside the 1-200 gate")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Write-back verification: read the file back and compare bytes, so a
    # partial write or encoding surprise fails loudly instead of submitting
    # a corrupted entry.
    with open(path, "rb") as f:
        if f.read() != LINE.encode("utf-8"):
            raise OSError(f"{path} does not match the entry line after write")


if __name__ == "__main__":
    main()
