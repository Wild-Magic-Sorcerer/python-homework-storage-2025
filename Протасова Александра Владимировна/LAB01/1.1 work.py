# Задание 1
def count_min():
    print("\nРасчет минимального числа:")
    smallest = numbers[0]
    print(f"Начинаем с первого числа: {smallest}")
    for i, n in enumerate(numbers):
        if i == 0:
            continue
        print(f"  Сравниваем текущее число {n} с текущим минимумом ({smallest}).")
        if n < smallest:
            smallest = n
            print(f"    {n} меньше, новый минимум: {smallest}")
        else:
            print(f"    {n} не меньше.")
    print(f"Итоговое минимальное число: {smallest}")
    return smallest


def count_max():
    print("\nРасчет максимального числа:")
    largest = numbers[0]
    print(f"  Начинаем с первого числа: {largest}")
    for i, n in enumerate(numbers):
        if i == 0:
            continue
        print(f"  Сравниваем текущее число {n} с текущим максимумом ({largest}).")
        if n > largest:
            largest = n
            print(f"    {n} больше, новый максимум: {largest}")
        else:
            print(f"    {n} не больше.")
    print(f"Итоговое максимальное число: {largest}")
    return largest


def count_sum():
    print("\nРасчет суммы всех чисел:")
    total_sum = 0
    print(f"  Начинаем с суммы: {total_sum}")
    for n in numbers:
        print(f"  Добавляем число {n} к текущей сумме ({total_sum}).")
        total_sum += n
        print(f"    Новая сумма: {total_sum}")
    print(f"Итоговая сумма всех чисел: {total_sum}")
    return total_sum


if __name__ == "__main__":
    print("Введите 10 целых чисел")
    numbers = []
    while len(numbers) < 10:
        try:
            value_from_user = input(f"Введите число: ")
            num = int(value_from_user)
            numbers.append(num) # добавление числа в конец списка
        except ValueError:
                print("Неправильный ввод. Введите целое число.")
    if numbers:
        print(f"Ваш список чисел: {numbers}")
    else:
        print("Список чисел пуст.")
