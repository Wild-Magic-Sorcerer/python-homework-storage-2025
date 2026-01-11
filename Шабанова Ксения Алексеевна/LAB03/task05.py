def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

def factorial_iter(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def main():
    
    # Тестирование
    user_input = input("Введите целое число для вычисления факториала: ")
    
    if user_input.isdigit():
        num = int(user_input)
        print(f"\nЧисло: {num}")
        print(f"Рекурсия: {factorial_rec(num)}")
        print(f"Итерация: {factorial_iter(num)}")
    else:
        print("Ошибка: нужно было ввести целое положительное число!")


if __name__ == "__main__":
    main()



