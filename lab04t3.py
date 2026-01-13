from functools import reduce

numbers = list(range(1, 11))
product = reduce(lambda x, y: x * y, numbers)
print(product)