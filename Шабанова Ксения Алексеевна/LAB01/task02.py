def main():
    courses = ["Вышмат", "Философия", "Физика"]
    students = {}

    print("Введите имена студентов и оценки (3-5). Для выхода: 'стоп'")

    while True:
        name = input("Имя студента: ").strip()
        if name.lower() == 'стоп':
            break
        if not name or name in students:
            continue

        grades = {}
        for course in courses:
            while True:
            try:
                    grade = int(input(f"{course}: "))
            if 3 <= grade <= 5:
                    grades[course] = grade
            break
            except:
            pass

        students[name] = grades

        all_grades = [grade for grades in students.values() for grade in grades.values()]

    if all_grades:
        print(f"\nСредний балл: {sum(all_grades)/len(all_grades):.2f}")
        print(f"Минимальная оценка: {min(all_grades)}")
        print(f"Максимальная оценка: {max(all_grades)}")

if __name__ == "__main__":
    main()
