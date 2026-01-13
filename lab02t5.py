import string

def compare_strings():

    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")

    translator = str.maketrans('', '', string.punctuation)
    words1 = set(str1.translate(translator).lower().split())
    words2 = set(str2.translate(translator).lower().split())

    only_in_str1 = words1 - words2
    only_in_str2 = words2 - words1

    if not only_in_str1 and not only_in_str2:
        print("Все слова присутствуют в обеих строках.")
    else:
        if only_in_str1:
            print("Слова, присутствующие только в первой строке:", only_in_str1)
        if only_in_str2:
            print("Слова, присутствующие только во второй строке:", only_in_str2)

compare_strings()