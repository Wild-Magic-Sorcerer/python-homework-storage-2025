def multiply_integers(*args):
    product = 1
    has_integers = False

    for arg in args:
        if isinstance(arg, int):
            product *= arg
            has_integers = True

    return product if has_integers else None

print(multiply_integers(1, 2, 3))
print(multiply_integers(1, 2.5, 'a'))
print(multiply_integers('a', 2.5))
print(multiply_integers())