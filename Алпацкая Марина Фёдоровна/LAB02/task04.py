check_dist: dict[str:tuple[int]] = {'день': (32, 0), 'месяц': (13, 0), 'год': (3000, 1000), 'час': (25, 0),
                                   'минута': (61, -1), 'секунда': (61, -1)}

time_position: dict[int: str] = {0: 'день', 1:'месяц', 2:'год', 3:'час', 4:'минута', 5:'секунда'}

def checking_time(num: list):
    result: list = []
    for check in num:
        item_pos: int = num.index(check)
        value_to_check = int(check)
        while True:
            if check_dist[time_position[item_pos]][0] > value_to_check > check_dist[time_position[item_pos]][1]:
                break
            else:
                value_to_check = int(input(f'{time_position[item_pos]} который/ую Вы ввели не существует ({value_to_check})\nПожалуйста введити коректный вариант: '))
        result.append(value_to_check)
    return result

def time(data: str):
    data = data.replace(".", " ")
    data = data.replace(":", " ")
    ### Size check  (от {[time_position[item_pos]][0]} до {[time_position[item_pos]][1]})
    data_list = checking_time(data.split())
    return f'День: {data_list[0]}\nМесяц: {data_list[1]}\nГод: {data_list[2]}\nЧас: {data_list[3]}\nМинута: {data_list[4]}\nСекунда: {data_list[5]}\n'

if __name__ == '__main__':
    time_input = input("Введите время формата 'ДД.ММ.ГГГГ ЧЧ:ММ:СС':\n")
    correct_time = time(time_input)
    print(correct_time)
