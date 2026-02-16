from datetime import datetime


def logger(message, log_time=None):
    if log_time is None:
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{log_time}] {message}\n")


def main():
    user_message = input("Введите сообщение: ")
    logger(user_message)
    print("Сообщение записано.")


if name == "main":
    main()
