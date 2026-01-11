def score(course_name, student_name):
    while True:
        try:
            score = int(input(f"Введите оценку студента {student_name} за курс '{course_name}' (3-5): "))
            if 3 <= score <= 5:
                return score
            else:
                print("ошибка: Оценка должна быть в диапазоне от 3 до 5.")
        except ValueError:
            print("ошибка: Введите целое число.")


if __name__ == "__main__":
    default = ["Вышмат", "Программирование", "Анатомия"]

    studgrades = {}

    print("ввод данных о студентах. Для завершения введите 'стоп'")
    while True:
        name = input("\nвведите имя студента: ").strip()
        if name.lower() == 'стоп':
            break

        grades = []
        for course in default:
            grade = score(course, name)
            grades.append(grade)
        studgrades[name] = grades


    total_sum = 0
    for grade in grades:
        total_sum += grade
    average = total_sum / len(grades)

    min_grade = grades[0]
    for grade in grades:
        if grade < min_grade:
            min_grade = grade

    max_grade = grades[0]
    for grade in grades:
        if grade > max_grade:
            max_grade = grade

    print(f"общее количество студентов: {len(studgrades)},"
          f" средний балл по всем студентам: {average},"
          f" минимальная оценка среди всех: {min_grade},"
          f" максимальная оценка среди всех: {max_grade}")
