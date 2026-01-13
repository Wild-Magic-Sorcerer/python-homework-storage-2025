def transform_string(input_string):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    transformed_string = ""

    for char in input_string:
        if char in vowels:
            transformed_string += char.upper()
        elif char.isalpha():
            transformed_string += char.lower()
        else:
            transformed_string += char

    return transformed_string

input_str = "Привет, как дела?"
result = transform_string(input_str)
print(result)