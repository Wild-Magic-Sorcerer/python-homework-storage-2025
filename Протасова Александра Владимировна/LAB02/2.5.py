def process_string(text):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    text = text.lower()
    for char in punctuation:
        text = text.replace(char, '')

    return text

def get_unique_words(text1, text2):
    processed1 = process_string(text1)
    processed2 = process_string(text2)

    words1 = set(processed1.split())
    words2 = set(processed2.split())

    unique_to_first = words1 - words2
    unique_to_second = words2 - words1

    return unique_to_first, unique_to_second


def main():
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")

    unique1, unique2 = get_unique_words(str1, str2)

    if not unique1 and not unique2:
        print("Все слова присутствуют в обеих строках!")
    else:
        if unique1:
            print(f"Слова, которые есть в первой строке, но отсутствуют во второй: {', '.join(unique1)}")
        if unique2:
            print(f"Слова, которые есть во второй строке, но отсутствуют в первой: {', '.join(unique2)}")


if __name__ == "__main__":
    main()
