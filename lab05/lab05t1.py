import random

with open('numbers.txt', 'w') as file:
    for _ in range(10):
        number = random.randint(1, 100)
        file.write(f"{number}\n")

def calculate_statistics(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    max_value = max(numbers)
    min_value = min(numbers)
    average_value = sum(numbers) / len(numbers)

    print(f"Максимальное значение: {max_value}")
    print(f"Минимальное значение: {min_value}")
    print(f"Среднее значение: {average_value}")

calculate_statistics('numbers.txt')