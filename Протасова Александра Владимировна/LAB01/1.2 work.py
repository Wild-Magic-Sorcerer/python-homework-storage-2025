courses = ("Ботаника", "Зоология", "Математика")

def count_min(grades=None):
    smallest = None
    if grades:
        smallest = grades[0]
        for n in grades:
            if n < smallest:
                smallest = n
    return smallest

def count_max(grades=None):
    largest = None
    if grades:
         largest = grades[0]
        for n in grades:
            if n > largest:
                largest = n
    return largest

    avg = sum(all_grades) / len(all_grades)

    print(f"Минимум: {smallest}")
    print(f"Максимум: {largest}")
    print(f"Средний балл: {avg:.2f}")

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
