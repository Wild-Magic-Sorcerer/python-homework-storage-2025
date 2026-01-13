def factorial_recursive(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    while True:
        user_input = input("Введите целое неотрицательное число для вычисления факториала: ")
        try:
            number = int(user_input)
            if number < 0:
                print("Пожалуйста, введите неотрицательное число.")
                continue

            factorial_rec = factorial_recursive(number)
            print(f"Факториал (рекурсивно) {number}! = {factorial_rec}")

            factorial_iter = factorial_iterative(number)
            print(f"Факториал (итеративно) {number}! = {factorial_iter}")
            break

        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")