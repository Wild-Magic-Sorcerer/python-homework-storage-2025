import sys

def factorial(some_list):
    if not some_list:
        return None

    try:
        n = int(some_list[1])
    except ValueError:
        return "Ошибка: первый аргумент должен быть числом"

    result = 1
    process = []

    for num in range(1, n + 1):
        result *= num
        process.append(result)

    if some_list[-1] in ["-v","--verbose"]:
        return f"Результат вычисления: {result}\nПодробное вычисление: {process}"
    else:
        return f"Результат вычисления: {result}"

if __name__ == "__main__":
    print(factorial(sys.argv))