
import datetime

def logger(message, timestamp=None):
    if timestamp is None:
        timestamp = datetime.datetime.now()
    time_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    with open("log.txt", "a", encoding= 'utf-8') as file:
        log_entery = f"[{time_str}] {message}\n"
        file.write(log_entery)
    user_mesage = input('введите сообщение')

if __name__ == "__main__":
    logger("начало работы")
    time = datetime.datetime(2020, 3, 3, 3, 3, 3)

    print(time, user_mesage)
    

