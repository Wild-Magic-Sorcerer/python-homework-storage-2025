def main():
    subjects = ["Зоология", "Ботаника", "Физкультура"]
    NUM_SUBJECTS = len(subjects)
    NUM_FIELDS = NUM_SUBJECTS + 1

    students = {}

    print("Введите данные студентов (для завершения введите пустую строку или 'N'):")

    while True:
        user_input = input(
            f"Введите имя студента и {NUM_SUBJECTS} оценки через пробел "
            f"({', '.join(subjects)}): "
        ).strip()

        if not user_input or user_input.upper() == 'N':
            break

        data = user_input.split()

        if len(data) != NUM_FIELDS:
            print(f"Ошибка: должно быть {NUM_FIELDS} поля (имя и {NUM_SUBJECTS} оценки)")
            continue

        name = data[0]

        if any(char.isdigit() for char in name):
            print("Ошибка: имя не должно содержать цифры")
            continue

        try:
            grades = []
            valid_grades = True

            for i in range(1, NUM_FIELDS):
                grade = int(data[i])
                if grade < 3 or grade > 5:
                    print(f"Ошибка: оценка должна быть от 3 до 5 (получено: {grade})")
                    valid_grades = False
                    break
                grades.append(grade)

            if valid_grades:
                students[name] = grades
                print(f"Оценки студента {name} добавлены")

        except ValueError:
            print("Ошибка: оценки должны быть целыми числами")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

    if not students:
        print("Нет данных о студентах")
        return

    print("Оценки студентов:")

    for name, grades in students.items():
        subject_grades = []
        for i, subject in enumerate(subjects):
            subject_grades.append(f"{subject} - {grades[i]}")
        print(f"{name}: {', '.join(subject_grades)}")

    print("Средние баллы:")

    subject_totals = {subject: [] for subject in subjects}

    all_grades = []

    for grades in students.values():
        all_grades.extend(grades)
        for i, subject in enumerate(subjects):
            subject_totals[subject].append(grades[i])

    if all_grades:
        overall_avg = sum(all_grades) / len(all_grades)
        print(f"Средний балл по всем предметам: {overall_avg:.2f}")

    for subject in subjects:
        grades_list = subject_totals[subject]
        if grades_list:
            subject_avg = sum(grades_list) / len(grades_list)
            print(f"Средний балл по {subject.lower()}: {subject_avg:.2f}")


if __name__ == "__main__":
    main()

