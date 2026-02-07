def calculate_big_one(dict_of_values):
    if not dict_of_values:
        return None

    greatest_value = None
    for some_value in dict_of_values.values():
        if greatest_value is None or some_value > greatest_value:
            greatest_value = some_value
    return greatest_value


def calculate_little_one(dict_of_values):
    if not dict_of_values:
        return None

    smallest_value = None
    for some_value in dict_of_values.values():
        if smallest_value is None or some_value < smallest_value:
            smallest_value = some_value
    return smallest_value


def calculate_average_value(grades_list):
    if not grades_list:
        return 0

    return sum(grades_list) / len(grades_list)

if __name__ == "__main__":
    students = {"Иван": [5, 4, 5], "Мария": [4, 3, 4], "Петр": [3, 4, 5]}

    print("Средние баллы:")
    all_grades = []

    for name, grades in students.items():
        avg = calculate_average_value(grades)
        print(f"{name}: {avg}")
        all_grades.extend(grades)

    if all_grades:
        total_avg = calculate_average_value(all_grades)
        print(f"Общий средний балл: {total_avg}")

    min_dict = {}
    for name, grades in students.items():
        min_dict[name] = min(grades)

    max_dict = {}
    for name, grades in students.items():
        max_dict[name] = max(grades)

    min_grade = calculate_little_one(min_dict)
    max_grade = calculate_big_one(max_dict)

    print(f"Минимальная оценка в группе: {min_grade}")
    print(f"Максимальная оценка в группе: {max_grade}")


