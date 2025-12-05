from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    product = reduce(lambda x, y: x * y, numbers)
    print("Исходный список:", numbers)
    print("Произведение всех элементов:", product)
