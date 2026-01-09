def main():
    numbers = []
    while len(numbers) < 10:
        user_input = input(f"Введите целое число {len(numbers) + 1}/10: ")
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Ошибка: Введите корректное целое число.")

    min_number = min(numbers)
    max_number = max(numbers)
    total_sum = sum(numbers)

    print(f"Минимальное число: {min_number}")
    print(f"Максимальное число: {max_number}")
    print(f"Сумма всех чисел: {total_sum}")

if __name__ == "__main__":
    main()