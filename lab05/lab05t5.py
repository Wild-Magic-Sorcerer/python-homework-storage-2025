    import datetime
def logger(message, time=None):
    if time is None:
        time = datetime.datetime.now()
    log_entry = f"{time}: {message}\n"
    with open("log.txt", "a") as log_file:
        log_file.write(log_entry)
while True:
    user_input = input("Введите сообщение для лога (или введите 'exit' для выхода): ")
    if user_input.lower() == 'exit':
        break
    logger(user_input)
    print("Сообщение записано в лог.")