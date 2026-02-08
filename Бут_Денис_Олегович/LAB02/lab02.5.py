def prepare_text(text):

    signs = ".,!?;:-()\"'"
    for sign in signs:
        text = text.replace(sign, ' ')

    words = text.lower().split()
    return [word for word in words if word]


def compare_strings(first_string, second_string):
    if not first_string or not second_string:
        return None

    words1 = prepare_text(first_string)
    words2 = prepare_text(second_string)

    first_set = set(words1)
    second_set = set(words2)

    only_in_first = first_set - second_set
    only_in_second = second_set - first_set

    if not only_in_first and not only_in_second:
        print("Все слова присутствуют в обеих строках")
    else:
        if only_in_first:
            print(f"Слова только в первой строке: {only_in_first}")
        if only_in_second:
            print(f"Слова только во второй строке: {only_in_second}")
    return None

if __name__ == "__main__":
    str1 = input("Введите первую строку:")
    str2 = input("Введите вторую строку:")

    compare_strings(str1, str2)