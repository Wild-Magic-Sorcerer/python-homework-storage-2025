def number_chek(list_chekc: dict[str: dict[str: int]]):
    for i in list_chekc:
        print(f"\nСредняя оценка по предмету '{i}': {sum(list_chekc[i][num] for num in list_chekc[i])/len(list_chekc[i])}")
        print(f"Максимальная оценка по предмету '{i}': {max(list_chekc[i][num] for num in list_chekc[i])}")
        print(f"Минимальная оценка по предмету '{i}': {min(list_chekc[i][num] for num in list_chekc[i])}")
    return None

if __name__ == '__main__':
    students: dict[str: dict[str: int]]= {"програмирование пайтон": {}, "цифравая аналитика": {}, "введение в биоинформатику": {}}
    print('Ведите имина студентов\nКогда закончите вводить студентов введите букву: "N"')
    names = []
    while True:
        name = input('Введите имя студента: ')
        if 'n' == name.lower() or '' == name:
            break
        names.append(name)

    for journal in students:
        for nam in names:
            while True:
                temp = input(f'Введите оценку по предмету "{journal}" которую получил/ла {nam}: ')
                if temp.isdigit():
                    temp_int = int(temp)
                    if 2<= temp_int <= 5:
                        students[journal][nam] = temp_int
                        break
                print("Вы ввели не валидное значение, пожалуйста попробуйте снова")

    number_chek(students)
