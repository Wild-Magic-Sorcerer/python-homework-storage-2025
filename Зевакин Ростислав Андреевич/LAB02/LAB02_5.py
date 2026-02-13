punctuation = ".,;:!?\"'()[]{}-_"

def clean_text_to_words(text):
    text = text.lower()

    for p in punctuation:
        text = text.replace(p, ' ')

    words = [word for word in text.split() if word]
    return words

def find_unique_words(words1, words2):
    set1 = set(words1)
    set2 = set(words2)

    unique_to_first = set1 - set2
    unique_to_second = set2 - set1

    return unique_to_first, unique_to_second


def main():
    str1 = input("Первая строка: ")
    str2 = input("Вторая строка: ")

    words1 = clean_text_to_words(str1)
    words2 = clean_text_to_words(str2)

    unique1, unique2 = find_unique_words(words1, words2)
    all_unique = unique1.union(unique2)

    if not all_unique:
        print("Все слова присутствуют в обеих строках.")
        return

    if unique1:
        print("Слова только в первой строке:", ', '.join(sorted(unique1)))
    if unique2:
        print("Слова только во второй строке:", ', '.join(sorted(unique2)))


if __name__ == "__main__":
    main()