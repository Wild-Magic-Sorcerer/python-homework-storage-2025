numbers = [15, -8, 3, -12, 7, 0, -3, 10, -20, 18, 5, -15, 2, 20, -1, 14, -6, 9, -10, 4]

if __name__ == "__main__":
    filtered_numbers = list(filter(lambda x: x > -5 and x % 2 == 0, numbers))
    print("Исходный список:", numbers)
    print("Отфильтрованные числа (больше -5 и чётные):", filtered_numbers)
