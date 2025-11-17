courses = ("Ботаника", "Зоология", "Математика")


def find_min(grade_list=None):
    min_grade = None
    if grade_list:
        min_grade = grade_list[0]
        for num in grade_list:
            if num < min_grade:
                min_grade = num
    return min_grade


def find_max(grade_list=None):
    max_grade = None
    if grade_list:
        max_grade = grade_list[0]
        for num in grade_list:
            if num > max_grade:
                max_grade = num
    return max_grade


if __name__ == '__main__':
    student_grades = {}
    student_names = []

    while True:
        name_input = input("Имя студента (или 'стоп'): ")
        if name_input == "стоп":
            break
        student_names.append(name_input)
        student_grades[name_input] = {}

    for student_name in student_names:
        print(f"\nОценки студента: {student_name}")
        for course in courses:
            while True:
                try:
                    user_input = input(f"Оценка по {course} (3-5): ")
                    grade_value = int(user_input)
                    if 3 <= grade_value <= 5:
                        student_grades[student_name][course] = grade_value
                        break
                    else:
                        print("Неверная оценка")
                except ValueError:
                    print("Не число")

    for course in courses:
        course_grade_list = []
        for student_name in student_names:
            if course in student_grades[student_name]:
                course_grade_list.append(student_grades[student_name][course])

        if course_grade_list:
            min_value = find_min(course_grade_list)
            max_value = find_max(course_grade_list)
            average = sum(course_grade_list) / len(course_grade_list)

            print(f"\n{course}:")
            print(f"  Минимум: {min_value}")
            print(f"  Максимум: {max_value}")
            print(f"  Средний балл: {average:.2f}")
