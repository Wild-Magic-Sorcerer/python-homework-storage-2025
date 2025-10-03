def big_value(def_big):
    great_value = 0
    for i in tuple_of_name:
        student_value1 = tuple_of_name[i]
        if student_value1 <= 5:
            if student_value1 > great_value:
                great_value = student_value1
        else:
            continue
    return great_value


def little_value(def_little):
    small_value = 100
    for i in tuple_of_name:
        student_value2 = tuple_of_name[i]
        if student_value2 <= 5:
            if student_value2 < small_value:
                small_value = student_value2
        else:
            continue
    return small_value


if __name__ == "__main__":
    course_and_students = {
        "Higher mathematics": {"Миша": 5, "Савелий": 2, "Маша": 4},
        "Physics": {"Игорь": 2, "Света": 6, "Любовь": 4},
        "Zoology": {"Саша": 3, "Игнат": 2, "Мирослав": 5},
        "Botany": {"Соня": 1, "Инокентий": 4, "Тосиро": 5},
    }
    dict_in_dict = input(
        "Выберите предмет: Higher mathematics, Physics,Zoology,Botany  "
    )
    tuple_of_name = course_and_students[dict_in_dict]
    list_of_name = course_and_students[dict_in_dict].keys()
    print(tuple_of_name)

    student = input("Выберите студента:")
    value = tuple_of_name[student]
    if 3 <= value <= 5:
        print("good")
    elif value < 3:
        print("bad value")
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

    print(big_value(tuple_of_name), little_value(tuple_of_name), average_value)
