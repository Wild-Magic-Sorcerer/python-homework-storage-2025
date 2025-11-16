def parsing(stroke):
    stroke = stroke.strip()
    list_str = stroke.split()
    mark_wor = 0
    mark_num = 0
    mark_znak = 0
    mark_space = 0
    for word in list_str:
        mark_space = mark_space + word.count(" ")
        for i in word:
            if i.isalpha() == True:
                mark_wor = mark_wor + 1
            elif i.isdigit() == True:
                mark_num = mark_num  + 1
            else:
                mark_znak = mark_znak +1

    dictionaries = {"Слов": len(list_str), "Букв": mark_wor, "Цифр": mark_num, "Пробелов": mark_space, "Знаков препинания": mark_znak}
    return dictionaries

if __name__ == '__main__':
    parse = input('Введите строку: ')
    result = parsing(parse)
    print(result)
