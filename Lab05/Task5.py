from datetime import datetime

def logger(message, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()

    formatted_time = timestamp.strftime("%d.%m.%Y %H:%M:%S")

    log_entry = f"[{formatted_time}] - {message}\n"

    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(log_entry)


logger("Запуск системы")
logger("Пользователь 'admin' вошел в систему")
logger("Ошибка доступа к базе данных", timestamp=datetime(2025, 12, 31, 23, 59))