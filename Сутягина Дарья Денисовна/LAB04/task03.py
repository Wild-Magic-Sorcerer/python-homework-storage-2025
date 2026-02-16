from functools import reduce

if __name__ == "__main__":
    numbers = list(range(1, 11))
    product = reduce(lambda x, y: x * y, numbers)

    print(product)
