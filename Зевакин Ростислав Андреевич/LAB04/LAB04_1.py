is_even = lambda x: x % 2 == 0

print("Проверка четности чисел от 1 до 10:")

for number in range(1, 11):
    result = is_even(number)
    print(f"Число {number:2} -> четное: {result}")