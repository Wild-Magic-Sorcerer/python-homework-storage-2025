def read_numbers(filename):
    numbers = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    pass
    except FileNotFoundError:
        print("Файл не найден.")
        return []

    return numbers


def main():
    numbers = read_numbers("numbers.txt")

    if numbers:
        print("Максимальное значение:", max(numbers))
        print("Минимальное значение:", min(numbers))
        print("Среднее значение:", sum(numbers) / len(numbers))
    else:
        print("Файл не содержит чисел.")


if name == "main":
    main()
