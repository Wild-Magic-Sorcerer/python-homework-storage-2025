def find_maximum(numbers):
    if not numbers:
        return None

    maximum = int(numbers[0])
    for number in numbers:
        current = int(number)
        if current > maximum:
            maximum = current
    return maximum


def find_minimum(numbers):
    if not numbers:
        return None

    minimum = int(numbers[0])
    for number in numbers:
        current = int(number)
        if current < minimum:
            minimum = current
    return minimum


if __name__ == "__main__":
    list_of_num = []

    print("Введите 10 целых чисел:")

    while len(list_of_num) < 10:
        user_input = input(f"Число {len(list_of_num) + 1}: ").strip()

        try:
            num = int(user_input)
            list_of_num.append(num)
        except ValueError:
            print("Пожалуйста, введите целое число.")

    print(f"\nВведенные числа: {list_of_num}")

    summarise = sum(list_of_num)

    print(f"Наибольшее число: {find_maximum(list_of_num)}")
    print(f"Наименьшее число: {find_minimum(list_of_num)}")
    print(f"Сумма чисел: {summarise}")
