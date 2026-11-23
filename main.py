"""Curious Judge entry: a paradox in one small box, handed to the reader as plain text."""

import os


def build_sentence():
    pieces = (
        "The box is empty. The box is full.",
        "Both are true \u2014 and the only thing left to open is the sentence holding them.",
    )
    return " ".join(pieces)


def destination_folder():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    line = build_sentence()
    folder = destination_folder()
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
