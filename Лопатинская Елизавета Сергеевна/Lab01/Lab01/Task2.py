courses = ["Высшая математика", "Зоология позвоночных", "Органическая химия"]
students_data = []

print("Текущий контроль успеваемости студентов")
print(f"Курсы: {', '.join(courses)}")
print("Введите 'выход', чтобы завершить ввод и увидеть результаты.\n")

while True:
    name = input("Введите имя студента: ").strip()
    if name.lower() == 'выход':
        break

    student_grades = []
    print(f"Введите оценки для студента {name}:")

    for course in courses:
        while True:
            grade_input = input(f"  Оценка за '{course}' (3-5): ")
            try:
                grade = int(grade_input)
                if 3 <= grade <= 5:
                    student_grades.append(grade)
                    break
                else:
                    print("  Ошибка: Оценка должна быть в диапазоне от 3 до 5.")
            except ValueError:
                print("  Ошибка: Введите целое число.")


    students_data.append({"name": name, "grades": student_grades})

if not students_data:
    print("\nДанные не были введены.")
else:
    all_grades = []
    for s in students_data:
        all_grades.extend(s["grades"])

    average_score = sum(all_grades) / len(all_grades)
    min_score = min(all_grades)
    max_score = max(all_grades)

    print("-" * 30)
    print(f"Всего студентов: {len(students_data)}")
    print(f"Средний балл по всем курсам: {average_score:.2f}")
    print(f"Минимальная оценка: {min_score}")

    print(f"Максимальная оценка: {max_score}")
    
