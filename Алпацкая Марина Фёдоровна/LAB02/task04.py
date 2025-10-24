def time(data: str):
    data = data.replace(".", " ")
    data = data.replace(":", " ")
    data_list = data.split()
    return print(f'День: {data_list[0]}\nМесяц: {data_list[1]}\nГод: {data_list[2]}\nЧас: {data_list[3]}\nМинута: {data_list[4]}\nСекунда: {data_list[5]}\n')

if __name__ == '__main__':
    time(input("Введите время формата 'ДД.ММ.ГГГГ ЧЧ:ММ:СС':\n"))
