courses = ["Высшая математика", "Зоология беспозвоночных", "Основы цитологии"]


def input_student():
    name = input("Введите имя студента (чтобы закончить - нажмите Enter): ").strip()
    if name == "":
        return None
    else:
        return name


def input_mark(course_names):
    marks = []
    for course in course_names:
        while True:
            s = input(f'Введите оценку за курс "{course}" (3-5): ').strip()
            try:
                mark = int(s)
                if 3 <= mark <= 5:
                    marks.append(mark)
                    break
                else:
                    print("Оценка должна быть в диапазоне от 3 до 5.")
            except ValueError:
                print("Это не целое число, попробуйте снова.")
    return marks


def calculate_stats(marks):
    total = 0
    minim = marks[0]
    maxim = marks[0]
    for m in marks:
        total += m
        if m < minim:
            minim = m
        if m > maxim:
            maxim = m

    average = total / len(marks)
    return average, minim, maxim


def print_results(avg, mn, mx):
    print('Средний балл по всем студентам:', f"{avg:.2f}")
    print('Минимальная оценка:', mn)
    print('Максимальная оценка:', mx)


def main():
    while True:
        all_marks = []
        students = []

        while True:
            student = input_student()
            if student is None:
                break
            students.append(student)
            all_marks.extend(input_mark(courses))

        if not students:
            print("Студенты не введены. Начинаем заново.\n")
            continue

        avg, mn, mx = calculate_stats(all_marks)
        print_results(avg, mn, mx)
        break


if __name__ == "__main__":
    main()