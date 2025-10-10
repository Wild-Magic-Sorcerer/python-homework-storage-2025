# Задание 1
numbers = []
while len(numbers) < 10:
    try:
        num = int(input(f"Введите число ({len(numbers) + 1}/10): "))
        numbers.append(num) # добавление числа в конец списка
    except ValueError:
            print("Неправильный ввод. Введите целое число.")
if numbers:
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    print(f"Минимальное число: {smallest}")

    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    print(f"Максимальное число: {largest}")

    print(f"Сумма чисел: {sum(numbers)}")
else:
    print("Список чисел пуст.")
