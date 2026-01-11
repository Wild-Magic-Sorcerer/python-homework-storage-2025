def multiply_integers(*args):
    product = 1
    found_int = False

    for item in args:
        if type(item) is int:
            product *= item
            found_int = True
            
    return product if found_int else None


def main():
    print("--- Тестирование функции умножения целых чисел ---")

    res1 = multiply_integers(2, 'текст', 3, 5.5, 4)
    res2 = multiply_integers('hello', [1, 2], True)
    res3 = multiply_integers(10, 0, 5)
    
    print(f"Результат 1 (2 * 3 * 4): {res1}")
    print(f"Результат 2 (нет целых): {res2}")
    print(f"Результат 3 (10 * 0 * 5): {res3}")

if __name__ == "__main__":
    main()
    

