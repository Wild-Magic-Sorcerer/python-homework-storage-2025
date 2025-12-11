import datetime

def logger(message, time=None):
    if time is None:
        time = datetime.datetime.now()

    time_str = time.strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"[{time_str}] {message}\n"

    with open("log.txt", "a") as f:
        f.write(log_line)


if __name__ == "__main__":
    logger("Программа начала работу")

    my_time = datetime.datetime(2006, 8, 10, 20, 0, 0)
    logger("Тестовое сообщение", my_time)
