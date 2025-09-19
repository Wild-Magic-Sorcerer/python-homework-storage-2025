kurs = ["програмирование пайтон", "цифравая аналитика", "введение в биоинформатику"]

if __name__ == '__main__':
    number_of_students = input("Введите количество студентов: ")
    students = {}

    while len(students) < int(number_of_students):
        student = input("\nВведите имя студента: ")
        students[student] = []
        for i in kurs:
            students[student].append(
                int(input(f"Введите оценку по предмету {i} которую получил/а студент/ка {student}: ")))
            while students[student][len(students[student]) - 1] > 5 or students[student][
                len(students[student]) - 1] < 0:
                students[student].pop()
                students[student].append(int(input(
                    f"Пожалуйста введите коректную оценку по предмету {i} которую получил/а студент/ка {student}: ")))

    for i in kurs:
        print(
            f"\nСредняя оценка по предмету '{i}': {sum(students[e][kurs.index(i)] for e in students) / len(students)}")
        print(f"Максимальная оценка по предмету '{i}': {max(students[e][kurs.index(i)] for e in students)}")
        print(f"Минимальная оценка по предмету '{i}': {min(students[e][kurs.index(i)] for e in students)}")


