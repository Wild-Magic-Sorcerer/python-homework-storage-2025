import string

def normalize_text(text):
    translator = str.maketrans('', '', string.punctuation)
    nopunct = text.translate(translator)
    words = nopunct.lower().split()
    return set(words)


if __name__ == "__main__":
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")

    words1 = normalize_text(str1)
    words2 = normalize_text(str2)

    uni1 = words1 - words2
    uni2 = words2 - words1

    if uni1 == uni2:
        print("все слова совпадают")
    else:
        if uni1:
            print(f"\n cлова, которые есть только в первой строке:")
            for word in sorted(uni1):
                print(word)

        if uni2:
            print(f"\n cлова, которые есть только во второй строке:")
            for word in sorted(uni2):

                print(word)
                
