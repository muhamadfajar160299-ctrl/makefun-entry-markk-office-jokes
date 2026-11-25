"""One-Line Office Jokes entry.

Writes a single original one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (no trailing newline).
"""

import os

LINE = "My printer only jams on urgent documents \u2014 I'm convinced it can smell fear."


def main():
    if not LINE.strip():
        raise ValueError("entry line is empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise RuntimeError("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
        os.chmod(path, 0o644)
    except OSError as exc:
        raise RuntimeError("failed to write entry.txt: %s" % exc) from exc


if __name__ == "__main__":
    main()
