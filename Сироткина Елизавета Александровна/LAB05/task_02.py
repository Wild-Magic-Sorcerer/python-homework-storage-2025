#!/usr/bin/env python3
from pathlib import Path

STRINGS_FILE = Path(__file__).parent / "strings.txt"


def append_line_to_file(file_path: Path, line_content: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(line_content + "\n")


def display_file_contents(file_path: Path) -> None:
    file_text = file_path.read_text(encoding="utf-8")
    lines = file_text.splitlines()
    
    print("\nСодержимое файла:")
    for line_number, line in enumerate(lines, start=1):
        print(f"  {line_number}. {line}")


def main() -> None:
    STRINGS_FILE.touch(exist_ok=True)
    
    user_input = input("Введите строку для добавления: ").strip()
    if not user_input:
        print("Ошибка: введена пустая строка")
        return
    
    append_line_to_file(STRINGS_FILE, user_input)
    display_file_contents(STRINGS_FILE)


if __name__ == "__main__":
    main()
