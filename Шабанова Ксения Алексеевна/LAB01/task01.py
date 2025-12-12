def main():
    numbers = []

    print("Введите 10 целых чисел:")

    while len(numbers) < 10:
        try:
            user_input = input(f"Число {len(numbers) + 1}: ")
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Что-то не так, введите целое число.")

    min_number = min(numbers)
    max_number = max(numbers)
    total_sum = sum(numbers)

    print("\nРезультаты:")
    print(f"Список чисел: {numbers}")
    print(f"Минимальное число: {min_number}")
    print(f"Максимальное число: {max_number}")
    print(f"Сумма всех чисел: {total_sum}")

if __name__ == "__main__":
    main()
