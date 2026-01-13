if __name__ == "__main__":
    numbers = list(range(-10, 11))
    numbers_of_3 = [n for n in numbers if n % 3 == 0]
    print("Исходные числа:", numbers)
    print("Числа, кратные 3:", numbers_of_3)
