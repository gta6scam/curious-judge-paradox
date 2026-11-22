"""Curious-judge entry: the box that is empty and full.

Angle: PARADOX / logic puzzle. A calm paradox in plain concrete words: a box that is both empty and full, and the sentence itself becomes the last thing to open. The reader keeps asking which claim gives way — and neither does.

Writes the single curiosity text to $MAKEFUN_OUTPUT_DIR/entry.txt
(UTF-8, byte-identical on every run), with no dependencies and no network.
The output directory comes from the environment, as the harness requires;
"/output" is only the local fallback when the variable is unset.
"""

TEXT = 'The box is empty. The box is full. Both are true — and the only thing left to open is the sentence holding them.'


def main() -> None:
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # newline="" keeps the write byte-exact: no platform line-ending
    # translation is applied, so entry.txt contains TEXT and nothing else.
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
