def recursive(n):
    if n <= 1:
        return 1
    return n * recursive(n - 1)

def iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    while True:
        try:
            number = int(input("Введите целое неотрицательное число: "))
            if number < 0:
                print("Число должно быть неотрицательным.\n")
                continue

            print("Факториал рекурсивно:", recursive(number))
            print("Факториал итеративно:", iterative(number))
            break

        except ValueError:
            print("Введите целое число.\n")

if __name__ == "__main__":
    main()
