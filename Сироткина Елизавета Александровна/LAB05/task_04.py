#!/usr/bin/env python3
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input_lines.txt"
OUTPUT_FILE = Path(__file__).parent / "unique_lines.txt"

SAMPLE_DATA = "apple\nbanana\napple\ncherry\nbanana\ndate\n"


def extract_unique_lines(input_path: Path) -> tuple[list[str], list[str]]:
    file_content = input_path.read_text(encoding="utf-8")
    all_lines = [line for line in file_content.strip().split("\n") if line]
    
    encountered: set[str] = set()
    unique_lines: list[str] = []
    duplicates: set[str] = set()
    
    for line in all_lines:
        if line in encountered:
            duplicates.add(line)
        else:
            encountered.add(line)
            unique_lines.append(line)
    
    return unique_lines, list(duplicates)


def main() -> None:
    INPUT_FILE.write_text(SAMPLE_DATA, encoding="utf-8")
    
    unique, duplicate_list = extract_unique_lines(INPUT_FILE)
    OUTPUT_FILE.write_text("\n".join(unique), encoding="utf-8")
    
    print(f"Уникальные строки: {unique}")
    print(f"Дубликаты: {duplicate_list}")


if __name__ == "__main__":
    main()
