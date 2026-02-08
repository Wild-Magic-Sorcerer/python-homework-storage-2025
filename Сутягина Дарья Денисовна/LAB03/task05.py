def recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive(n - 1)

def iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    while True:
        user_input = input("Введите целое неотрицательное число: ")

        try:
            number = int(user_input)

            if number < 0:
                print("Ошибка: число должно быть неотрицательным.\n")
                continue

            rec_result = recursive(number)
            iter_result = iterative(number)

            print(f"Факториал (рекурсивно): {rec_result}")
            print(f"Факториал (итеративно): {iter_result}")
            break

        except ValueError:
            print("Ошибка: введите целое число.\n")