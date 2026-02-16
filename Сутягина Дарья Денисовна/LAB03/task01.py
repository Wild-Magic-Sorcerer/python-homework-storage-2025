def long_strings(strings: list) -> list:
    if not strings:
        return []

    total = 0
    for s in strings:
        total += len(s)

    avg_len = total / len(strings)

    result = []
    for s in strings:
        if len(s) > avg_len:
            result.append(s)

    return result

def main():
    user_input = input("Введите строки через пробел: ")
    strings = user_input.split()
    print("Результат:", long_strings(strings))

if __name__ == "__main__":
    main()
