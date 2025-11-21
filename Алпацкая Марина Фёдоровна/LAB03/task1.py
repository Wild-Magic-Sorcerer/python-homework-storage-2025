def sifter(lines_list:list):
    average_value = sum([len(long) for long in lines_list])/2
    new_line = [lin for lin in lines_list if len(lin)>= average_value]
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
