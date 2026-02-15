def filter_vowel_strings(**kwargs):
    vowels = "аеёиоуыэюяaeiouy"
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, str):
            count = 0
            for char in value.lower():
                if char in vowels:
                    count += 1
            if count >= 3:
                result[key] = value
    return result
data = (filter_vowel_strings
    (
    name="Маратата",
    city="Санкт-Петербург",
    fruit="томат",
    code=123,
    word="ритмичность"
))
print(f"Подходящие именованные аргументы:", data)
