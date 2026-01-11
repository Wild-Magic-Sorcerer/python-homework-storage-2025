import string

def get_clean_words(text):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    return set(clean_text.split())

def compare_strings():
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")

    words1 = get_clean_words(str1)
    words2 = get_clean_words(str2)

    diff = words1.symmetric_difference(words2)

    if not diff:
        print("\nВсе слова присутствуют в обеих строках.")
    else:
        print("\nСлова, которые есть только в одной из строк:")
        print(", ".join(diff))

compare_strings()

