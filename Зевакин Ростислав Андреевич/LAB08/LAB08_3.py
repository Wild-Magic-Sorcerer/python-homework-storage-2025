import re


def main():
    print("Введите строку для разбивки на слова:")
    user_input = input()

    words = re.split(r'[.,!?;:\-—\s]+', user_input)

    words = [word for word in words if word]

    print("\nСписок слов:")
    for i, word in enumerate(words, 1):
        print(f"{i}. '{word}'")



if __name__ == "__main__":
    main()