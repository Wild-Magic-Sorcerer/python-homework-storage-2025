def multiply_integers(*args):
    integers = [x for x in args if type(x) == int]

    if not integers:
        return None

    result = 1
    for num in integers:
        result *= num

    return result

if __name__ == "__main__":
    print(multiply_integers(2, 3, "hello", 4.5, 5))
    print(multiply_integers(1, 2, 3, 4, 5))
    print(multiply_integers("hello", 3.14, [1, 2]))
