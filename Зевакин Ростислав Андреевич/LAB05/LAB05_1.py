import random

random_numbers = [random.randint(1, 100) for _ in range(228)]

with open("numbers.txt", "w", encoding="utf-8") as file:
    for number in random_numbers:
        file.write(str(number) + "\n")

print(f"Записаны числа: {random_numbers}")

try:
    numbers = []

    with open("numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()  # Уборка пробелов
            if line:  # Проверка, что строка не пустая
                try:
                    numbers.append(int(line))
                except ValueError:
                    print(f"строка '{line}' не является числом")

    if not numbers:
        print("Файл пуст или не содержит чисел")
    else:
        maximum = max(numbers)
        minimum = min(numbers)
        average = sum(numbers) / len(numbers)

        print(f"Прочитано чисел: {len(numbers)}")
        print(f"Список чисел: {numbers}")
        print("Результаты анализа:")
        print(f"Максимальное число: {maximum}")
        print(f"Минимальное число: {minimum}")
        print(f"Среднее значение: {average:.2f}")

        print("Доп инфа:")
        print(f"Сумма всех чисел: {sum(numbers)}")
        print(f"Количество чисел: {len(numbers)}")

        max_index = numbers.index(maximum) + 1
        min_index = numbers.index(minimum) + 1

        print(f"Максимальное число ({maximum}) находится на строке {max_index}")
        print(f"Минимальное число ({minimum}) находится на строке {min_index}")

except FileNotFoundError:
    print("Ошибка: файл 'numbers.txt' не найден!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("Содержимое файла 'numbers.txt'")

try:
    with open("numbers.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content if content else "Файл пуст")

except FileNotFoundError:
    print("Файл не найден")