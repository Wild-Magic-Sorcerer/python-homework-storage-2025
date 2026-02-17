import datetime

def logger(msg, time=None):
    time = time or datetime.datetime.now()
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")

logger("Тест")