numbers = []
for i in range(10):
    while True:
        user_input = input(f"Введите число {i + 1} из 10: ")
        try:
            num = int(user_input)
            numbers.append(num)
            break
        except ValueError:
            print("Ошибка: введите целое число!")

if numbers:
    print(f"\nСписок чисел: {numbers}")
    print(f"Минимальное число: {min(numbers)}")
    print(f"Максимальное число: {max(numbers)}")
    print(f"Сумма всех чисел: {sum(numbers)}")
else:
    print("Список пуст")
