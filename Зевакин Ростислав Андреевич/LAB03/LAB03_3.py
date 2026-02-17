def multiply_integers(*args): # умножает только целые числа
    result = 1
    found_integers = False  # целые ли числа

    for arg in args:
        if isinstance(arg, int):  # Проверка на целое число
            result *= arg
            found_integers = True

    return result if found_integers else None

def main():
    print("Работа функции multiply_integers():")

    print("\n1. Только целые числа:")
    print(f"   multiply_integers(2, 3, 4) = {multiply_integers(2, 3, 0.1, 4)}")

    print("\n2. Смешанные типы (целые и другие):")
    print(f"   multiply_integers(2, 3.5, 'строка', 4) = {multiply_integers(2, 3.5, 'строка', 4)}")

    print("\n3. Без целых чисел:")
    print(f"   multiply_integers(3.14, 'текст', [1, 2]) = {multiply_integers(3.14, 'текст', [1, 2])}")

    print("\n4. Пустой вызов:")
    print(f"   multiply_integers() = {multiply_integers()}")

    print("\n5. С отрицательными числами:")
    print(f"   multiply_integers(-2, 3, -4) = {multiply_integers(-2, 3, -4)}")

    print("\n6. С нулем:")
    print(f"   multiply_integers(5, 0, 7) = {multiply_integers(5, 0, 7)}")

    print("\n7. С логическими значениями:")
    print(f"   multiply_integers(True, False, 3) = {multiply_integers(True, False, 3)}")

    print("Доп пример:")
    numbers = [10, "не число", 2.5, 3, [1, 2], 4]
    print(f"multiply_integers(*{numbers}) = {multiply_integers(*numbers)}")


if __name__ == "__main__":
    main()