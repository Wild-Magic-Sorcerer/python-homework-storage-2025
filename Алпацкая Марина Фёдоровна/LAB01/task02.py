def chek(student_chek, l=int):
    if student_chek[l] > 5:
        return False
    if student_chek[l] < 0:
        return False
    return True

def number_chek(num_st, name_kurs, list_kurs):
    print(
        f"\nСредняя оценка по предмету '{name_kurs}': {sum(num_st[e][list_kurs.index(name_kurs)] for e in students) / len(students)}")
    print(f"Максимальная оценка по предмету '{name_kurs}': {max(num_st[e][list_kurs.index(name_kurs)] for e in students)}")
    print(f"Минимальная оценка по предмету '{name_kurs}': {min(num_st[e][list_kurs.index(name_kurs)] for e in students)}")
    return None

if __name__ == '__main__':
    kurs = ["програмирование пайтон", "цифравая аналитика", "введение в биоинформатику"]
    number_of_students = input("Введите количество студентов: ")
    while number_of_students.isdigit() == False:
        print('Вы написали не число. Попробуйте ещё раз.')
        number_of_students = input("Введите количество студентов: ")
    students = {}

    for num in range(int(number_of_students)):
        student = input("\nВведите имя студента: ")
        students[student] = []
        for i in range(len(kurs)):
            students[student].append(
                int(input(f"Введите оценку по {kurs[i]} которую получил/а {student}: ")))
            while chek(students[student], i) == False:
                students[student].pop()
                students[student].append(int(input(
                    f"Пожалуйста введите коректную оценку по предмету {kurs[i]} которую получил/а студент/ка {student}: ")))

    for i in kurs:
        number_chek(students, i, kurs)