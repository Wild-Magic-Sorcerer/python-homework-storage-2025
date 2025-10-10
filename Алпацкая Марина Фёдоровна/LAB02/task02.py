def parsing(stroke):
    stroke = stroke.strip()
    list_str = stroke.split()
    mark_wor = 0
    mark_num = 0
    mark_znak = 0
    for word in list_str:
        for i in word:
            if i.isalpha() == True:
                mark_wor = mark_wor + 1
            elif i.isdigit() == True:
                mark_num = mark_num  + 1
            else:
                mark_znak = mark_znak +1

    dictionaries = {"Слов": len(list_str), "Букв": mark_wor, "Цифр": mark_num, "Пробелов": len(list_str)-1, "Знаков препинания": mark_znak}
    return dictionaries

if __name__ == '__main__':
    print(parsing(input("Введите строку: ")))