def main():
    courses = ["Высшая математика", "Программирование python", "Зоология"]
    
    count_students = int(input("Введите количество студентов для оценки: "))
    
    all_marks = [] # Список для хранения вообще всех оценок всех студентов
    
    for i in range(count_students):
        name = input(f"\nВведите имя студента №{i+1}: ")
        
        print(f"Введите оценки студента {name} (от 3 до 5):")
        for course in courses:
            while True:
                mark_input = input(f"  {course}: ")
                
                # Проверка
                if mark_input.isdigit():
                    mark = int(mark_input)
                    if 3 <= mark <= 5:
                        all_marks.append(mark)
                        break
                    else:
                        print("    Ошибка: Оценка должна быть от 3 до 5!")
                else:
                    print("    Ошибка: Введите целое число!")
    
    # Вывод результатов
    if all_marks:
        average = sum(all_marks) / len(all_marks)
        print("\nИтоговая статистика по группе")
        print(f"Средний балл по всем студентам: {average:.2f}")
        print(f"Минимальная оценка: {min(all_marks)}")
        print(f"Максимальная оценка: {max(all_marks)}")
    else:
    
        print("\nОценки не были введены.")

if __name__ == "__main__":
    main()


