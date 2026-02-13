punctuation = ".,;:!?\"'()[]{}<>@#$%^&*_+-=~`|\\/"


def count_word_stats(text):
    original_length = len(text)

    stripped = text.strip()
    stripped_spaces = original_length - len(stripped)

    stats = {
        'words': 0,
        'letters': 0,
        'digits': 0,
        'spaces': 0,
        'punctuation': 0,
        'total_chars_original': original_length,
        'stripped_spaces': stripped_spaces
    }

    if not stripped:
        return stats

    in_word = False
    word_letters = 0

    for char in stripped:
        if 'а' <= char.lower() <= 'я' or 'a' <= char.lower() <= 'z':
            stats['letters'] += 1
            word_letters += 1
            if not in_word:
                in_word = True

        elif '0' <= char <= '9':
            stats['digits'] += 1
            word_letters += 1
            if not in_word:
                in_word = True

        elif char == ' ' or char == '\t' or char == '\n':
            stats['spaces'] += 1
            if in_word:
                stats['words'] += 1
                in_word = False
                word_letters = 0

        elif char in PUNCTUATION:
            stats['punctuation'] += 1
            if in_word:
                stats['words'] += 1
                in_word = False
                word_letters = 0

        else:
            if in_word:
                stats['words'] += 1
                in_word = False
                word_letters = 0

    if in_word:
        stats['words'] += 1

    return stats


def print_stats_report(original, stats):

    print(f"\nИсходная строка: '{original}'")
    print(f"После удаления пробелов в начале/конце: '{original.strip()}'")

    print(f"  Слов:                 {stats['words']}")
    print(f"  Букв:                 {stats['letters']}")
    print(f"  Цифр:                {stats['digits']}")
    print(f"  Пробелов:            {stats['spaces']}")
    print(f"  Знаков препинания:   {stats['punctuation']}")

    total_processed = (
            stats['letters'] +
            stats['digits'] +
            stats['spaces'] +
            stats['punctuation']
    )

    print(f"  Всего символов в исходной строке:     {stats['total_chars_original']}")
    print(f"  Удалено пробелов в начале/конце:      {stats['stripped_spaces']}")
    print(f"  Всего символов в обработанной строке: {total_processed}")

    if stats['words'] > 0:
        avg_length = stats['letters'] / stats['words']
        print(f"\n  Средняя длина слова: {avg_length:.1f} букв")

def main():
    user_input = input("Введите строку для анализа: ")
    result = count_word_stats(user_input)
    print_stats_report(user_input, result)


if __name__ == "__main__":
    main()