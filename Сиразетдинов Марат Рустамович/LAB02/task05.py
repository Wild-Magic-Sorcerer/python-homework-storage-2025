import string

def get_words_set(text):
    text = text.lower()

    table = str.maketrans("", "", string.punctuation)
    text = text.translate(table)
    return set(text.split())

def compare_string():
    str1 = input("Введите строку 1:")
    str2 = input("Введите строку 2:")

    words1 = get_words_set(str1)
    words2 = get_words_set(str2)
    diff = words1^words2
    if not diff:
        print("Строки одинаковые")

    else:
        print("Уникальные слова:")
        for word in diff:
            print(f"- {word}")

compare_string()
