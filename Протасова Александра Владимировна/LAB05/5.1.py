import random

def count_min(nums):
    if not nums:
        print("Список чисел пуст. Невозможно найти минимум.")
        return None

    print("\nРасчет минимального числа:")
    smallest = nums[0]
    print(f"Начинаем с первого числа: {smallest}")

    for index, num in enumerate(nums):
        if index == 0:
            continue
        print(f"Сравниваем текущее число {num} с текущим минимумом ({smallest}).")
        if num < smallest:
            smallest = num
            print(f"{num} меньше, новый минимум: {smallest}")
        else:
            print(f"{num} не меньше.")

    print(f"Итоговое минимальное число: {smallest}")
    return smallest


def count_max(nums):
    if not nums:
        print("Список чисел пуст. Невозможно найти максимум.")
        return None

    print("\nРасчет максимального числа:")
    largest = nums[0]
    print(f"Начинаем с первого числа: {largest}")

    for index, num in enumerate(nums):
        if index == 0:
            continue
        print(f"Сравниваем текущее число {num} с текущим максимумом ({largest}).")
        if num > largest:
            largest = num
            print(f"{num} больше, новый максимум: {largest}")
        else:
            print(f"{num} не больше.")

    print(f"Итоговое максимальное число: {largest}")
    return largest


def count_sum(nums):
    if not nums:
        print("Список чисел пуст. Сумма равна 0.")
        return 0

    print("\nРасчет суммы всех чисел:")
    total_sum = 0
    print(f"Начинаем с суммы: {total_sum}")

    for num in nums:
        print(f"Добавляем число {num} к текущей сумме ({total_sum}).")
        total_sum += num
        print(f"Новая сумма: {total_sum}")

    print(f"Итоговая сумма всех чисел: {total_sum}")
    return total_sum

if __name__ == "__main__":
    with open("numbers.txt", "w") as file:
        for j in range(10):
            file.write(f"{random.randint(1, 100)}\n")

            numbers_list = []
            with open("numbers.txt", "r") as file_1:
                for line in file:
                    numbers_list.append(int(line.strip()))

            print(f"Числа из файла: {numbers_list}")

    min_num = count_min(numbers_list)
    max_num = count_max(numbers_list)
    total = count_sum(numbers_list)

    avg_num = 0
    if numbers_list:
        avg_num = total / len(numbers_list)
        print(f"\nСреднее арифметическое: {avg_num:.2f}")
    else:
        print("\nНевозможно вычислить среднее арифметическое - список пуст")

        print(f"Минимальное число: {min_num}")
        print(f"Максимальное число: {max_num}")
        print(f"Среднее арифметическое: {avg_num:.2f}")
