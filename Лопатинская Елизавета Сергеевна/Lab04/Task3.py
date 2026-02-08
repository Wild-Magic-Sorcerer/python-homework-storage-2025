from functools import reduce

def calculate_product(numbers_list):
    if not numbers_list:
        return 0
    return reduce(lambda x, y: x * y, numbers_list)

def main():
    numbers = list(range(1, 11))
    product = calculate_product(numbers)

    print(f"Список чисел: {numbers}")
    print(f"Произведение всех элементов (10!): {product}")

if __name__ == "__main__":
    main()

