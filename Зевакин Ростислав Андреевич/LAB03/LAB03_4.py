def filter_strings_with_vowels(**kwargs):
    result = {}

    vowels = "аеёиоуыэюяaeiou"

    for key, value in kwargs.items():
        if isinstance(value, str):
            vowel_count = 0
            for char in value.lower():
                if char in vowels:
                    vowel_count += 1
            if vowel_count >= 3:
                result[key] = value

    return result

def main():
    print("Фильтрация строк")

    print("\n1. Пример с разными типами данных:")
    result1 = filter_strings_with_vowels(
        name="Сергей",
        age=25,
        city="Санкт-Петербург",
        hobby="Плавать",
        score=19.84,
        note="Сложно",
        empty=""
    )
    print(f"   Результат: {result1}")

    print("\n2. Строки с разным количеством гласных:")
    result2 = filter_strings_with_vowels(
        text1="Рот",  # 1 гласная
        text2="Дом",  # 1 гласная
        text3="Ага",  # 2 гласные
        text4="Апельсин",  # 4 гласные
        text5="Warrum",  # 2 гласные
        text6="Puff",  # 1 гласная
        text7="Радионуклеид"  # 6 гласных
    )
    print(f"   Результат: {result2}")

    print("\n3. Смесь английских и русских слов:")
    result3 = filter_strings_with_vowels(
        eng1="Beautiful",  # 5 гласных
        eng2="Programming",  # 3 гласные
        rus1="Эрудированная",  # 6 гласных
        rus2="Компьютер",  # 3 гласные
        mix="Hello мир!"  # 3 гласные
    )
    print(f" Результат: {result3}")

    print("\n4. Без подходящих строк:")
    result4 = filter_strings_with_vowels(
        a="кот",
        b="рот",
        c="сон",
        d="123",
        e="!!!"
    )
    print(f"   Результат: {result4} (пустой словарь)")

    print("\n5. Пустой вызов:")
    result5 = filter_strings_with_vowels()
    print(f"   Результат: {result5}")

if __name__ == "__main__":
    main()