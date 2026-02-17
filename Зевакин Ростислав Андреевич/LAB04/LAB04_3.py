from functools import reduce

numbers = list(range(1, 11))

product = reduce(lambda x, y: x * y, numbers)

print("Список чисел:", numbers)
print("Произведение всех чисел от 1 до 10:", product)
print("Подробный расчет:")
print("10! =", product)