def main():
    numbers = []
    print("Введите 10 целых чисел:")
    while len(numbers) < 10:
        user_input = input(f"Введите число №{len(numbers) + 1}: ")
        
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное целое число.")

    min_val = min(numbers)
    max_val = max(numbers)
    total_sum = sum(numbers)

    print("-" * 30)
    print(f"Ваш список: {numbers}")
    print(f"Минимальное число: {min_val}")
    print(f"Максимальное число: {max_val}")
    print(f"Сумма всех чисел: {total_sum}")

if __name__ == "__main__":
    main()
