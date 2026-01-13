if __name__ == "__main__":
    numbers = []
    for i in range(10):
        while True:
            user_input = input(f"введите целое число ")
            try:
                num = int(user_input)
                numbers.append(num)
                break
            except ValueError:
                print("неорректное число")
    
    if numbers:
        min_num = numbers[0]
        for num in numbers:
            if num < min_num:
                min_num = num
        print(f"минимальное число: {min_num}")

        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        print(f"максимальное число: {max_num}")

        total = 0
        for num in numbers:
            total += num
        print(f"сумма всех чисел: {total}")
    else:
        print("пусто")

