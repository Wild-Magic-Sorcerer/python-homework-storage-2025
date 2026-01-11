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
    user = input("введите целое неотрицательное число: ")
    number = int(user)
    if number < 0:
        print("ошибка: факториал определен только для неотрицательных чисел!")

    print("рекурсивный метод:")
    result_rec = recursive(number)
    print(f"{number}! = {result_rec}")

    print("итеративный метод:")
    result_iter = iterative(number)
    print(f"{number}! = {result_iter}")
