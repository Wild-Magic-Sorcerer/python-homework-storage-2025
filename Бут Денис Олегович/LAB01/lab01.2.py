def calculate_biggest_value(dict_of_values):
    if not dict_of_values:
        return None
    greatest_value = None
    for some_value in dict_of_values.values():
        if greatest_value is None:
            greatest_value = some_value
        elif greatest_value < some_value:
                greatest_value = some_value
    return greatest_value

def calculate_smallest_value(dict_of_values):
    if not dict_of_values:
        return None
    smallest_value = None
    for some_value in dict_of_values.values():
        if smallest_value is None:
            smallest_value = some_value
        elif some_value < smallest_value:
            smallest_value = some_value
    return smallest_value

if __name__ == "__main__":
    students = {
        "Иван": [5, 4, 5],
        "Мария": [4, 3, 4],
        "Петр": [3, 4, 5] }

    print("Средние баллы:")
    
    all_grades = []
    
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        print(f"{name}: {round(avg, 2)}")
        all_grades.extend(grades)
        
    if all_grades:
        total_avg = sum(all_grades) / len(all_grades)
        print(f"Общий средний:, {round(total_avg, 2)}")

    min_dict = {}
    for name, grades in students.items():
        min_dict[name] = min(grades)
    max_dict = {}
    for name, grades in students.items():
        max_dict[name] = max(grades)
        
    min_grade = calculate_smallest_value(min_dict)
    max_grade = calculate_biggest_value(max_dict)

    print(f"Минимальная оценка в группе: {min_grade}")
    print(f"Максимальная оценка в группе: {max_grade}")
    
    
