def count_min(numbers):
    if not numbers:
        print("Список чисел пуст. Невозможно найти минимум.")
        return None

    print("\nРасчет минимального числа:")
    smallest = numbers[0]
    print(f"Начинаем с первого числа: {smallest}")

    for i, n in enumerate(numbers):
        if i == 0:
            continue
        print(f"Сравниваем текущее число {n} с текущим минимумом ({smallest}).")
        if n < smallest:
            smallest = n
            print(f"{n} меньше, новый минимум: {smallest}")
        else:
            print(f"{n} не меньше.")

    print(f"Итоговое минимальное число: {smallest}")
    return smallest


def count_max(numbers):
    if not numbers:
        print("Список чисел пуст. Невозможно найти максимум.")
        return None

    print("\nРасчет максимального числа:")
    largest = numbers[0]
    print(f"Начинаем с первого числа: {largest}")

    for i, n in enumerate(numbers):
        if i == 0:
            continue
        print(f"Сравниваем текущее число {n} с текущим максимумом ({largest}).")
        if n > largest:
            largest = n
            print(f"{n} больше, новый максимум: {largest}")
        else:
            print(f"{n} не больше.")

    print(f"Итоговое максимальное число: {largest}")
    return largest


def count_sum(numbers):
    if not numbers:
        print("Список чисел пуст. Сумма равна 0.")
        return 0

    print("\nРасчет суммы всех чисел:")
    total_sum = 0
    print(f"Начинаем с суммы: {total_sum}")

    for n in numbers:
        print(f"Добавляем число {n} к текущей сумме ({total_sum}).")
        total_sum += n
        print(f"Новая сумма: {total_sum}")

    print(f"Итоговая сумма всех чисел: {total_sum}")
    return total_sum


if __name__ == "__main__":
    print("Введите 10 целых чисел")
    numbers_list = []
    while len(numbers_list) < 10:
        try:
            value_from_user = input(f"Введите число {len(numbers_list) + 1}: ")
            num = int(value_from_user)
            numbers_list.append(num)
        except ValueError:
            print("Неправильный ввод. Введите целое число.")

    if numbers_list:
        print(f"Ваш список чисел: {numbers_list}")
        min_value = count_min(numbers_list)
        max_value = count_max(numbers_list)
        sum_value = count_sum(numbers_list)

        if min_value is not None:
            print(f"Минимальное число: {min_value}")
        if max_value is not None:
            print(f"Максимальное число: {max_value}")
        print(f"Сумма всех чисел: {sum_value}")
    else:
        print("Список чисел пуст.")
