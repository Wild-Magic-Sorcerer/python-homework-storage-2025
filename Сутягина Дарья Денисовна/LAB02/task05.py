def compare_strings(s1: str, s2: str):
    punct = ".,!?;:-()\"'"

    for symb in punct:
        s1 = s1.replace(symb, "")
        s2 = s2.replace(symb, "")

    words1 = set(s1.lower().split())
    words2 = set(s2.lower().split())

    only_in_1 = words1 - words2
    only_in_2 = words2 - words1

    if not only_in_1 and not only_in_2:
        print("Все слова присутствуют в обеих строках")
    else:
        if only_in_1:
            print("Слова только в первой строке:")
            print(*only_in_1)

        if only_in_2:
            print("Слова только во второй строке:")
            print(*only_in_2)


def main():
    first = input("Введите первую строку: ")
    second = input("Введите вторую строку: ")
    compare_strings(first, second)


if __name__ == "__main__":
    main()
