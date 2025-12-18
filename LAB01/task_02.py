#!/usr/bin/env python3
"""Учёт оценок студентов по курсам."""

COURSES = ("Программирование на Python", "Базы данных", "Операционные системы")


def read_grade(course: str) -> int:
    """Читает оценку 3-5 для курса."""
    while True:
        try:
            grade = int(input(f"  {course} (3-5): "))
            if 3 <= grade <= 5:
                return grade
            print("  Оценка должна быть 3, 4 или 5")
        except ValueError:
            print("  Введите число")


def collect_students() -> dict[str, dict[str, int]]:
    """Собирает данные студентов до ввода пустого имени."""
    students: dict[str, dict[str, int]] = {}
    print("Ввод студентов (пустое имя = конец):\n")
    
    while True:
        name = input("Студент: ").strip()
        if not name:
            break
        students[name] = {c: read_grade(c) for c in COURSES}
    
    return students


def show_results(students: dict[str, dict[str, int]]) -> None:
    """Выводит результаты и статистику."""
    if not students:
        print("Нет данных")
        return
    
    all_grades = [g for s in students.values() for g in s.values()]
    
    print("\n--- Результаты ---")
    for name, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        print(f"{name}: {avg:.1f}")
    
    print(f"\nВсего студентов: {len(students)}")
    print(f"Средний балл: {sum(all_grades) / len(all_grades):.2f}")


def main() -> None:
    print(f"Курсы: {', '.join(COURSES)}\n")
    show_results(collect_students())


if __name__ == "__main__":
    main()
