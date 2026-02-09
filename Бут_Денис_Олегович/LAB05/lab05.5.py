import datetime

def logger(input_argument, input_time=None):
    if input_time is None:
        input_time = datetime.datetime.now()

    with open("log_for_lab05.5.txt", "a") as log:
        log.write(f"Users data:{input_argument}\n input time: {input_time}\n")


if __name__ == '__main__':
    users_str = input("Введите строку:")
    logger(users_str)