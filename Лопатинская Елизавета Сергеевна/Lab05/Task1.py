import random

def save_random_numbers(filename, count=10):
    numbers = [random.randint(1, 100) for _ in range(count)]
    with open(filename, "w", encoding="utf-8") as file:
        for num in numbers:
            file.write(f"{num}\n")
    print(f"Файл '{filename}' успешно создан.")
    return numbers

def analyze_numbers_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        numbers = [int(line.strip()) for line in file if line.strip()]

    if not numbers:
        print("Файл пуст.")
        return

    max_val = max(numbers)
    min_val = min(numbers)
    avg_val = sum(numbers) / len(numbers)

    print("-" * 30)
    print(f"Числа из файла: {numbers}")
    print(f"Максимальное: {max_val}")
    print(f"Минимальное: {min_val}")
    print(f"Среднее: {avg_val:.2f}")
    print("-" * 30)

def main():
    filename = "numbers.txt"
    save_random_numbers(filename)

    try:
        analyze_numbers_from_file(filename)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
    except ValueError:
        print("Ошибка: В файле содержатся некорректные данные (не числа).")

if __name__ == "__main__":
    main()
    
