"""The World Today - 22 November 2026.

Copies the front-page image held in this repository to the output
path the grader reads, byte for byte, with no network access.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    # Confirm the copy is complete before reporting success, so a
    # truncated write can never pass silently as a valid entry.
    if os.path.getsize(target) != os.path.getsize(source):
        print("error: copied file size does not match entry.png", file=sys.stderr)
        return 1
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
