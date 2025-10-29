def checking_time(num: list):
    while True:
        if 31 >= int(num[0]) > 0:
            break
        else:
            num[0] = input(f'Дня "{num[0]}" не существует\nПожалуйста введити день: ')
    while True:
        if 12 >= int(num[1]) > 0:
            break
        else:
            num[1] = input(f'Месяца "{num[1]}" не существует\nПожалуйста введити месяц: ')
    while True:
        if 24 >= int(num[3]) > 0:
            break
        else:
            num[3] = input(f'Часа "{num[3]}" не существует\nПожалуйста введити час: ')
    while True:
        if 60 >= int(num[4]) >= 0:
            break
        else:
            num[4] = input(f'Минуты "{num[4]}" не существует\nПожалуйста введити коректный час: ')
    while True:
        if 60 >= int(num[5]) >= 0:
            break
        else:
            num[5] = input(f'Секунды "{num[5]}" не существует\nПожалуйста введити коректное время: ')
    return num

def time(data: str):
    data = data.replace(".", " ")
    data = data.replace(":", " ")
    data_list = checking_time(data.split())
    return f'День: {data_list[0]}\nМесяц: {data_list[1]}\nГод: {data_list[2]}\nЧас: {data_list[3]}\nМинута: {data_list[4]}\nСекунда: {data_list[5]}\n'

if __name__ == '__main__':
    time_input = time(input("Введите время формата 'ДД.ММ.ГГГГ ЧЧ:ММ:СС':\n"))
    print(time_input)
