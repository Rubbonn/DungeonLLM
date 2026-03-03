"""
Split SRD_CC_v5.2.1.md into individual chapter files, one per macro section
(top-level `#` heading), saved in the "SRD Chapters/" directory.
"""

import os
import re

SRD_FILE = "SRD_CC_v5.2.1.md"
OUTPUT_DIR = "SRD Chapters"


def sanitize_filename(title: str) -> str:
    """Convert a section title into a safe filename."""
    # Replace characters that are invalid in filenames
    safe = re.sub(r'[\\/:*?"<>|]', "", title)
    # Collapse multiple spaces/dashes and strip edges
    safe = safe.strip(" -")
    return safe


def split_srd(srd_path: str, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)

    with open(srd_path, encoding="utf-8") as f:
        content = f.read()

    # Split on top-level headings (lines starting with exactly one `#`)
    # The pattern keeps the heading as part of the following section.
    parts = re.split(r"(?m)^(?=# (?!#))", content)

    # The first element is any content before the first heading (empty here).
    for part in parts:
        part = part.strip()
        if not part:
            continue

        # Extract the heading title from the first line
        first_line = part.splitlines()[0]
        title = first_line.lstrip("# ").strip()
        filename = sanitize_filename(title) + ".md"
        output_path = os.path.join(output_dir, filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(part + "\n")

        print(f"Written: {output_path}")


if __name__ == "__main__":
    split_srd(SRD_FILE, OUTPUT_DIR)
