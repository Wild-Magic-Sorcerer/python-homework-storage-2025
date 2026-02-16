def multiply_int(*args):
    result = 1
    found = False

    for arg in args:
        if isinstance(arg, int):
            result *= arg
            found = True

    return result if found else None

def main():
    values = [1, 2, "a", 3]
    print("Результат:", multiply_int(*values))

if __name__ == "__main__":
    main()
