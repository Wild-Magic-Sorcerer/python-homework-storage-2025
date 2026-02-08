def compare_strings(s1: str, s2: str):
    punctuation = ".,!?;:-()\"'"

    for p in punctuation:
        s1 = s1.replace(p, "")
        s2 = s2.replace(p, "")

    words1 = set(s1.lower().split())
    words2 = set(s2.lower().split())

    only_in_first = words1 - words2
    only_in_second = words2 - words1

    if not only_in_first and not only_in_second:
        print("Все слова присутствуют в обеих строках")
    else:
        if only_in_first:
            print("Слова, которые есть в первой строке, но нет во второй:")
            print(list(only_in_first))

        if only_in_second:
            print("Слова, которые есть во второй строке, но нет в первой:")
            print(list(only_in_second))