#!/usr/bin/env python3
SUBJECTS = ("Программирование на Python", "Базы данных", "Операционные системы")
MIN_GRADE = 3
MAX_GRADE = 5


def validate_grade(value: int) -> bool:
    return MIN_GRADE <= value <= MAX_GRADE


def input_grade(subject_name: str) -> int:
    while True:
        try:
            entered_grade = int(input(f"  {subject_name} ({MIN_GRADE}-{MAX_GRADE}): "))
            if validate_grade(entered_grade):
                return entered_grade
            print(f"  Ошибка: оценка должна быть от {MIN_GRADE} до {MAX_GRADE}")
        except ValueError:
            print("  Ошибка: введите целое число")


def gather_student_data() -> dict[str, dict[str, int]]:
    student_records: dict[str, dict[str, int]] = {}
    print("Введите данные студентов (пустая строка для завершения):\n")
    
    while True:
        student_name = input("Имя студента: ").strip()
        if not student_name:
            break
        
        student_grades: dict[str, int] = {}
        for subject in SUBJECTS:
            student_grades[subject] = input_grade(subject)
        
        student_records[student_name] = student_grades
    
    return student_records


def compute_average(grades: dict[str, int]) -> float:
    return sum(grades.values()) / len(grades)


def display_statistics(records: dict[str, dict[str, int]]) -> None:
    if not records:
        print("Нет данных для отображения")
        return
    
    print("\n=== Результаты ===")
    for student_name, grades in records.items():
        average = compute_average(grades)
        print(f"{student_name}: средний балл {average:.1f}")
    
    all_scores = [score for student in records.values() for score in student.values()]
    overall_average = sum(all_scores) / len(all_scores)
    
    print(f"\nВсего студентов: {len(records)}")
    print(f"Общий средний балл: {overall_average:.2f}")


def main() -> None:
    subjects_str = ", ".join(SUBJECTS)
    print(f"Дисциплины: {subjects_str}\n")
    student_data = gather_student_data()
    display_statistics(student_data)


if __name__ == "__main__":
    main()
