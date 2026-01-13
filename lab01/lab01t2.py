def is_valid_grade(grade):
    return isinstance(grade, int) and 3 <= grade <= 5


def main():
    courses = ["Зоология", "Ботаника", "Гистология"]

    students_grades = {}

    while True:
        name = input("Введите имя студента (или 'стоп' для завершения): ")
        if name.lower() == 'стоп':
            break

        grades = []
        for course in courses:
            while True:
                try:
                    grade = int(input(f"Введите оценку за курс '{course}' для {name}: "))
                    if is_valid_grade(grade):
                        grades.append(grade)
                        break
                    else:
                        print("Оценка должна быть целым числом от 3 до 5 включительно.")
                except ValueError:
                    print("Пожалуйста, введите целое число.")

        students_grades[name] = grades

    all_grades = [grade for grades in students_grades.values() for grade in grades]

    if all_grades:
        average_grade = sum(all_grades) / len(all_grades)
        min_grade = min(all_grades)
        max_grade = max(all_grades)

        print(f"\nСредний балл по всем студентам: {average_grade:.2f}")
        print(f"Минимальная оценка: {min_grade}")
        print(f"Максимальная оценка: {max_grade}")
    else:
        print("Нет оценок для анализа.")


if __name__ == "__main__":
    main()