numbers = []
print("Введите 10 целых чисел:")

while len(numbers) < 10:
    user_input = input(f"Введите число №{len(numbers) + 1}: ")
    # Проверяем, число ли это 
    if user_input.lstrip('-').isdigit():
        num = int(user_input)
        numbers.append(num)
    else:
        print("Это не целое число. Попробуйте еще раз!")

print("\nРезультаты:")
print(f"Минимальное число: {min(numbers)}")
print(f"Максимальное число: {max(numbers)}")
print(f"Сумма всех чисел: {sum(numbers)}")