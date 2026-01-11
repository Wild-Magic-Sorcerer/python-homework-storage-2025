def filter_vowel_strings(**kwargs):
    vowels = "аеёиоуыэюяaeiouy"
    result = {}

    for key, value in kwargs.items():
        if isinstance(value, str):
            vowel_count = sum(1 for char in value.lower() if char in vowels)
            if vowel_count >= 3:
                result[key] = value
    return result


filtered_data = filter_vowel_strings(
    name="Алексей",
    city="Уфа",
    job="Программист",
    hobby="AI",
    status="Active"
)

print("Отфильтрованные аргументы:")
print(filtered_data)