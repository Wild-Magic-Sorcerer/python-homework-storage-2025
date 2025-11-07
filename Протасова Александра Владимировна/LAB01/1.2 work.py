# задание 2
courses = ("Ботаника", "Зоология", "Математика")

def count_min():
 if __name__ == '__main__':
    grades = {}
    names = []
    while True:
        name = input("Имя студента (или 'стоп'): ")
        if name == "стоп":
            break
        names.append(name)
        grades[name] = {}

    for course in courses:
        print(f"\nОценки студента: {name}")
        for name in names:
            while True:
                try:
                    input_from_usr = input(f"Оценка по {course} (3-5): ")
                    grade = int(input_from_usr)
                    if 3 <= grade <= 5:
                        grades[name][course] = grade
                        break
                    else:
                        print("Неверная оценка")
                except ValueError:
                    print("Не число")

    all_grades = [grade for student in grades.values() for grade in student.values()]

    if grades:
        smallest = grades[0]
        for n in grades:
            if n < smallest:
                smallest = n
        print(f"Мин: {smallest}")

        largest = grades[0]
        for n in grades:
            if n > largest:
                largest = n
        print(f"Макс: {largest}")

    avg = sum(all_grades) / len(all_grades)
    print(f"Средний балл: {avg:.2f}")




