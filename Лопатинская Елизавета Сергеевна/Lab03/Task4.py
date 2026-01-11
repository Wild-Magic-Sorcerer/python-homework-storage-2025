def filter_vowel_strings(**kwargs):
    vowels = "аеёиоуыэюяaeiouy"
    result = {}

    for key, value in kwargs.items():
        if isinstance(value, str):
            vowel_count = sum(1 for char in value.lower() if char in vowels)
            if vowel_count >= 3:
                result[key] = value
    return result

def main():
    print("--- Анализ строк на наличие гласных (минимум 3) ---")

    filtered_data = filter_vowel_strings(
        name="Алексей",      # А, е, е -> 3
        city="Уфа",          # У, а -> 2
        job="Программист",   # о, а, и -> 3
        hobby="AI",          # A, I -> 2
        status="Active"      # A, i, e -> 3 )

    if filtered_data:
        print("\nОтфильтрованные аргументы:")
        for key, val in filtered_data.items():
            print(f"  • {key}: {val}")
    else:
        print("\nСовпадений не найдено.")

if __name__ == "__main__":
    main()

