def clean_text_for_palindrome(text):
    return text.lower().replace(" ", "")


def print_palindrome_result(original, cleaned):
    if cleaned == cleaned[::-1]:
        print(f"Строка '{original}' — палиндром.")
        return

    print(f"Строка '{original}' — не палиндром.")

    length = len(cleaned)
    for i in range(length // 2):
        if cleaned[i] != cleaned[length - 1 - i]:
            print(
                f"Несовпадение: позиция {i} ('{cleaned[i]}') != "
                f"позиция {length - 1 - i} ('{cleaned[length - 1 - i]}')"
            )
            return


def main():
    user_input = input("Введите строку для проверки на палиндром: ")
    cleaned = clean_text_for_palindrome(user_input)
    print_palindrome_result(user_input, cleaned)


if __name__ == "__main__":
    main()