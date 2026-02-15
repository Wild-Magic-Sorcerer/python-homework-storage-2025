import datetime

def logger(input_argument, input_time=None):
    if input_time is None:
        input_time = datetime.datetime.now()

    with open("log.txt", "a", encoding="utf-8") as log:
        log.write(f"Users data:{input_argument}\n input time: {input_time}\n")


if __name__ == '__main__':
    user_input = input("Введите строку: ")

    time_input = input("Время (ГГГГ-ММ-ДД ЧЧ:ММ или Enter для текущего): ")

    if time_input:
        try:
            inp_time = datetime.datetime.strptime(time_input, "%Y-%m-%d %H:%M")
            logger(user_input, inp_time)
        except ValueError :
            logger(user_input)
    else:
        logger(user_input)
        