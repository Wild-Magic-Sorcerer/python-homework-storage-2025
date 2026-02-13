def get_student_name():
    while True:
        name = input("Введите имя студента (Enter для завершения): ").strip()

        if not name:
            return None

        if any(char.isdigit() for char in name):
            print("Ошибка: имя не должно содержать цифры")
            continue

        special_chars = "\\/.*=!@#$%^№&*()_+[]{}|;:'\",<>?`~"
        if any(char in special_chars for char in name):
            print("Ошибка: имя не должно содержать спецсимволы")
            continue

        if len(name) < 2:
            print("Ошибка: имя должно содержать хотя бы 2 символа")
            continue

        return name


def get_student_grades(subjects):
    grades = []

    for subject in subjects:
        try:
            grade = int(input(f"Оценка по {subject}: "))

            if grade < 3 or grade > 5:
                print(f"Ошибка: оценка должна быть от 3 до 5 (получено: {grade})")
                return None

            grades.append(grade)

        except ValueError:
            print("Ошибка: оценка должна быть целым числом")
            return None

    return grades


def calculate_averages(students_dict, subjects):
    if not students_dict:
        return {}

    all_grades = []
    subject_grades = {subject: [] for subject in subjects}

    for grades in students_dict.values():
        all_grades.extend(grades)
        for i, subject in enumerate(subjects):
            subject_grades[subject].append(grades[i])

    averages = {
        'overall': sum(all_grades) / len(all_grades) if all_grades else 0,
        'by_subject': {}
    }

    for subject in subjects:
        grades = subject_grades[subject]
        averages['by_subject'][subject] = sum(grades) / len(grades) if grades else 0

    return averages


def print_results(students_dict, subjects):
    if not students_dict:
        print("\nНет данных о студентах.")
        return

    for name, grades in students_dict.items():
        grade_strings = []
        for i, subject in enumerate(subjects):
            grade_strings.append(f"{subject}: {grades[i]}")
        print(f"{name}: {', '.join(grade_strings)}")

    averages = calculate_averages(students_dict, subjects)

    print(f"Общий средний балл: {averages['overall']:.2f}")
    print("\nПо предметам:")
    for subject, avg in averages['by_subject'].items():
        print(f"  {subject}: {avg:.2f}")


def main():
    subjects = ["Зоология", "Ботаника", "Физкультура"]
    students = {}

    print(f"\nПредметы: {', '.join(subjects)}")
    print("\nДля завершения ввода оставьте имя пустым.")

    while True:
        print(f"\n Студент №{len(students) + 1} ")

        name = get_student_name()
        if name is None:
            break

        grades = get_student_grades(subjects)
        if grades is None:
            print("Отмена")
            continue

        students[name] = grades
        print(f"Студент {name} добавлен")

    print_results(students, subjects)


if __name__ == "__main__":
    main()
