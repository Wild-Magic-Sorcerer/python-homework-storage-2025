#!/usr/bin/env python3
from pathlib import Path

SOURCE_FILE = Path(__file__).parent / "source.txt"
DESTINATION_FILE = Path(__file__).parent / "destination.txt"

SAMPLE_CONTENT = """The cat sat on the mat.
My cat is very fluffy.
I have a cat and a dog.
"""

OLD_WORD = "cat"
NEW_WORD = "dog"


def copy_and_replace(
    source: Path, destination: Path, old_text: str, new_text: str
) -> str:
    source_content = source.read_text(encoding="utf-8")
    modified_content = source_content.replace(old_text, new_text)
    destination.write_text(modified_content, encoding="utf-8")
    return modified_content


def main() -> None:
    SOURCE_FILE.write_text(SAMPLE_CONTENT, encoding="utf-8")
    print(f"Исходный файл:\n{SAMPLE_CONTENT}")
    
    result = copy_and_replace(SOURCE_FILE, DESTINATION_FILE, OLD_WORD, NEW_WORD)
    print(f"Результат после замены '{OLD_WORD}' на '{NEW_WORD}':\n{result}")


if __name__ == "__main__":
    main()
