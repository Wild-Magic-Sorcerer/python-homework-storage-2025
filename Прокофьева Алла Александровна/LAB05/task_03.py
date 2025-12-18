#!/usr/bin/env python3
"""Копирование файла с заменой 'cat' на 'dog'."""

from pathlib import Path

SRC = Path(__file__).parent / "source.txt"
DST = Path(__file__).parent / "destination.txt"

SAMPLE = """The cat sat on the mat.
My cat is very fluffy.
I have a cat and a dog.
"""


def main() -> None:
    SRC.write_text(SAMPLE, encoding="utf-8")
    print(f"Исходный:\n{SAMPLE}")
    
    modified = SRC.read_text(encoding="utf-8").replace("cat", "dog")
    DST.write_text(modified, encoding="utf-8")
    print(f"Результат:\n{modified}")


if __name__ == "__main__":
    main()
