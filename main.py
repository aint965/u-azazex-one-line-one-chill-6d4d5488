"""One Line, One Chill — writes one single line of horror to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no files read,
no third-party code.
"""

import os

LINE = "My daughter's school photo came back today \u2014 thirty smiling children, and in the back row, a tall man no teacher remembers, holding her hand."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
