def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
user_input = input("Введите целое неотрицательное число:")
if user_input.isdigit():
    number = int(user_input)
    res_rec = factorial_recursive(number)
    res_ite = factorial_iterative(number)
    print(f"Факториал (рекурсия): {res_rec}")
    print(f"Факториал (цикл):    {res_ite}")
else:
    print("Ошибка: нужно ввести целое положительное число.")
