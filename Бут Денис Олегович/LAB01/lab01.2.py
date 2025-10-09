def calculate_biggest_value(dict_of_values):
    if not dict_of_values:
        return None
    greatest_value = None
    for value in dict_of_values.values():
        if not greatest_value:
            greatest_value = value
        else:
            if greatest_value < value:
                greatest_value = value
    return greatest_value


def calculate_smallest_value(dict_of_values):
    if not dict_of_values:
        return None
    smallest_value = None
    for value in dict_of_values.values():
        if not smallest_value:
            smallest_value = value
    else:
        if smallest_value > value:
            smallest_value = value
    return smallest_value


if __name__ == "__main__":
    course_and_students = {
        "Higher mathematics": {"Миша": 5, "Савелий": 2, "Маша": 4},
        "Physics": {"Игорь": 2, "Света": 6, "Любовь": 4},
        "Zoology": {"Саша": 3, "Игнат": 2, "Мирослав": 5},
        "Botany": {"Соня": 1, "Инокентий": 4, "Тосиро": 5},
    }
    dict_in_dict = input(
        "Выберите предмет: Higher mathematics, Physics,Zoology,Botany "
    )
    tuple_of_name = course_and_students[dict_in_dict]
    list_of_name = course_and_students[dict_in_dict].keys()
    print(list_of_name)

    name_of_student = input("Выберите студента:")
    value = tuple_of_name[name_of_student]
    if 3 <= value <= 5:
        print("good")
    else:
        print("wrong value")

    sum_of_value = 0
    list_of_value = []
    for i in tuple_of_name:
        student_value3 = tuple_of_name[i]
        if student_value3 <= 5:
            list_of_value.append(student_value3)
            sum_of_value = student_value3 + sum_of_value
        else:
            continue
        average_value: float = sum_of_value / len(list_of_value)

    print(
        calculate_biggest_value(tuple_of_name),
        calculate_smallest_value(tuple_of_name),
        average_value,
    )
