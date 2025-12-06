def logger(input_argument):
    with open("log_for_lab05.5.txt", "a") as log:
        log.write(f"\n{input_argument}")
    with open("log_for_lab05.5.txt", "r") as log:
        lines = log.read()
    return lines




if __name__ == '__main__':
    users_str = input("Введите строку:")
    print(logger(users_str))