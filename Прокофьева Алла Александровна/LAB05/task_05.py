#!/usr/bin/env python3
"""Простой логгер в файл с временной меткой."""

from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"


def log(message: str) -> None:
    """Записывает сообщение в лог."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{ts}] {message}\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"Записано: {entry.strip()}")


def main() -> None:
    log("Старт")
    
    msg = input("Сообщение: ")
    if msg.strip():
        log(msg)
    
    log("Стоп")
    print(f"\n{LOG_FILE.read_text(encoding='utf-8')}")


if __name__ == "__main__":
    main()
