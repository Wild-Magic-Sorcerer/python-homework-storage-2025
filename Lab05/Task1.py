import random
numbers_to_write = [random.randint(1, 100) for _ in range(10)]

with open("numbers.txt", "w", encoding="utf-8") as file:
    for num in numbers_to_write:
        file.write(f"{num}\n")

print("Файл 'numbers.txt' успешно создан.")

try:
    with open("numbers.txt", "r", encoding="utf-8") as file:
        numbers = [int(line.strip()) for line in file if line.strip()]

    if numbers:
        max_val = max(numbers)
        min_val = min(numbers)
        avg_val = sum(numbers) / len(numbers)

        print("-" * 30)
        print(f"Числа из файла: {numbers}")
        print(f"Максимальное: {max_val}")
        print(f"Минимальное: {min_val}")
        print(f"Среднее: {avg_val:.2f}")
        print("-" * 30)
    else:
        print("Файл пуст.")

except FileNotFoundError:
    print("Ошибка: Файл не найден.")
except ValueError:
    print("Ошибка: В файле содержатся некорректные данные (не числа).")