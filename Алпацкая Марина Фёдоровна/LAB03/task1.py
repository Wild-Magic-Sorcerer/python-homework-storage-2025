def sifter(lines_list:list):
    dict_lines: dict[int:str] = {}
    list_length =[]
    new_line = []
    for lin in lines_list:
        dict_lines[len(lin)] = lin
        list_length.append(len(lin))
    average_value = sum(list_length)/len(lines_list)
    for check_num in dict_lines:
        if check_num > average_value:
            new_line.append(dict_lines[check_num])
    return new_line

if __name__ == '__main__':
    print("Введите строки на проверку\nКогда закончите введите n")
    lines = []
    while True:
        line = input('Введите строку: ')
        if 'n' == line.lower() or '' == line:
            break
        lines.append(line)

    lines_above_average = sifter(lines)
    print(f'Строки больше среднего значения: {lines_above_average}')
