#!/usr/bin/env python3
"""Сохранение уникальных строк, вывод дубликатов."""

from pathlib import Path

INPUT = Path(__file__).parent / "input_lines.txt"
OUTPUT = Path(__file__).parent / "unique_lines.txt"

SAMPLE = "apple\nbanana\napple\ncherry\nbanana\ndate\n"


def main() -> None:
    INPUT.write_text(SAMPLE, encoding="utf-8")
    lines = INPUT.read_text(encoding="utf-8").strip().split("\n")
    
    seen: set[str] = set()
    unique: list[str] = []
    dups: set[str] = set()
    
    for line in lines:
        if line in seen:
            dups.add(line)
        else:
            seen.add(line)
            unique.append(line)
    
    OUTPUT.write_text("\n".join(unique), encoding="utf-8")
    print(f"Уникальные: {unique}")
    print(f"Дубликаты: {list(dups)}")


if __name__ == "__main__":
    main()
