from typing import Any


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def filter_strings_with_vowels(**kwargs: object) -> dict[Any, Any]:
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, str) and count_vowels(value) >= 3:
            result[key] = value
    return result

filtered_args = filter_strings_with_vowels(name="Alexander", age="30", city="New York", hobby="reading")
print(filtered_args)