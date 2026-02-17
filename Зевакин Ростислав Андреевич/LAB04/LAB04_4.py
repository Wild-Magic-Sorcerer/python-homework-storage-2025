import random

numbers = [random.randint(-20, 20) for _ in range(15)]

filtered_numbers = list(filter(lambda x: x > -5 and x % 2 == 0, numbers))

print("Исходный список:", numbers)
print("Фильтрация: числа > -5 и четные")
print("Отфильтрованный список:", filtered_numbers)

print("Подробный разбор:")

for num in numbers:
    condition1 = num > -5
    condition2 = num % 2 == 0
    conditions_met = condition1 and condition2

    if conditions_met:
        print(f" Число {num:3} Подходит (> -5: {condition1}, четное: {condition2})")
    else:
        print(f" Число {num:3} Не подходит (> -5: {condition1}, четное: {condition2})")