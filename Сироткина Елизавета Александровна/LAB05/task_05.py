#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path

LOG_FILE_PATH = Path(__file__).parent / "log.txt"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def write_log_entry(file_path: Path, message: str, timestamp: datetime | None = None) -> None:
    if timestamp is None:
        timestamp = datetime.now()
    
    formatted_time = timestamp.strftime(TIMESTAMP_FORMAT)
    log_entry = f"[{formatted_time}] {message}\n"
    
    with open(file_path, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)
    
    print(f"Записано в лог: {log_entry.strip()}")


def main() -> None:
    write_log_entry(LOG_FILE_PATH, "Старт")
    
    user_message = input("Введите сообщение для лога: ").strip()
    if user_message:
        write_log_entry(LOG_FILE_PATH, user_message)
    
    write_log_entry(LOG_FILE_PATH, "Стоп")
    
    print(f"\nПолное содержимое лога:\n{LOG_FILE_PATH.read_text(encoding='utf-8')}")


if __name__ == "__main__":
    main()
