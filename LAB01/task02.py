COURSES = ["Программирование", "Биоинженерия", "Химия"]
MIN_GRADE, MAX_GRADE = 2, 5

students = {}

print(f"Введите данные студентов (курсы: {', '.join(COURSES)})")
print("Для завершения ввода введите 'стоп' вместо имени\n")

while True:
    name = input("Имя студента: ").strip()
    if name == '0':
        break

    if name in students:
        print("Этот студент уже есть в системе!")
        continue

    grades = []
    print("Введите оценки (от 2 до 5):")

    for course in COURSES:
        while True:
            try:
                grade = int(input(f"{course}: "))
                if MIN_GRADE <= grade <= MAX_GRADE:
                    grades.append(grade)
                    break
                else:
                    print(f"Оценка должна быть от {MIN_GRADE} до {MAX_GRADE}!")
            except:
                print("Некорректный ввод!")

    students[name] = grades
    print()

if students:
    all_grades = [grade for grades in students.values() for grade in grades]

    print("\nРезультаты:")
    print("-" * 30)

    for name, grades in students.items():
        print(f"{name}: {grades}, среднее: {sum(grades) / len(grades):.2f}")

    print("-" * 30)
    print(f"Общее кол-во студентов: {len(students)}")
    print(f"Общий средний балл: {sum(all_grades) / len(all_grades):.2f}")
    print(f"Минимальная оценка: {min(all_grades)}")
    print(f"Максимальная оценка: {max(all_grades)}")
else:
    print("Нет данных о студентах.")
