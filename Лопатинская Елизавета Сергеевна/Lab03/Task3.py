def multiply_integers(args):
    product = 1
    found_int = False

    for item in args:
        if type(item) is int:
            product *= item
            found_int = True
    return product if found_int else None

print(f"Результат 1: {multiply_integers(2, 'текст', 3, 5.5, 4)}")
print(f"Результат 2: {multiply_integers('hello', [1, 2], True)}")

print(f"Результат 3: {multiply_integers(10, 0, 5)}")
