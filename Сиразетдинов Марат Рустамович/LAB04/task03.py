from functools import reduce
number = range(1, 11)
product = reduce(lambda x, y: x * y, number)
print(product)
