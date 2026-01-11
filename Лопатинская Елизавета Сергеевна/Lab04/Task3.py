from functools import reduce

numbers = list(range(1, 11))

product = reduce(lambda x, y: x * y, numbers)

print(f"Список чисел: {numbers}")

print(f"Произведение всех элементов (10!): {product}")
