import datetime

def logger(input_argument):
    with open("log_for_lab05.5.txt", "a") as log:
        log.write(f"Users data:{input_argument}\n input time: {datetime.datetime.now()}")

if __name__ == '__main__':
    users_str = input("Введите строку:")
    logger(users_str)

