def number_chek(list_chekc: dict[str: dict[str: int]]):
    for i in list_chekc:
        print(f"\nСредняя оценка по предмету '{i}': {sum(int(list_chekc[i][num]) for num in list_chekc[i])/len(list_chekc[i])}")
        print(f"Максимальная оценка по предмету '{i}': {max(int(list_chekc[i][num]) for num in list_chekc[i])}")
        print(f"Минимальная оценка по предмету '{i}': {min(int(list_chekc[i][num]) for num in list_chekc[i])}")
    return None

if __name__ == '__main__':
    students: dict[str: dict[str: int]]= {"програмирование пайтон": {}, "цифравая аналитика": {}, "введение в биоинформатику": {}}
    print('Ведите имина студентов\n Когда закончите вводить студентов введите букву: "N"')
    name = []
    while 'N' and 'n' not in name:
        name.append(input('Введите имя студента: '))
    name.pop()

    for journal in students:
        for num in name:
            t_f = True
            while t_f == True:
                students[journal][num] = input(f'Введите оценку по предмету "{journal}" которую получил/ла {num}: ')
                if students[journal][num].isdigit():
                    if 2<= int(students[journal][num]) <= 5:
                        t_f = False
                        continue
                print("Вы ввели не валидное значение, пожалуйста попробуйте снова")

    number_chek(students)