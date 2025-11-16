from tkinter.font import names


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
    courses = (
        "Higher mathematics",
        "Physics",
        "Zoology",
        "Botany",
    )
    names=[]
    while True:
        student_name = input("Введите имя студента. N/n если всё.")
        if student_name.lower() == "n" or student_name == "" :
            break
        names.append(student_name)
    print(names)
    result: dict[str: dict[str: int]]= {}
    for course in courses:
        value= input(f"Введите оценку студента {student_name} по курсу {courses}")
        result[student_name][course] = value
    print(result)
