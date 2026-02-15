def transform_string(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY"
    result = ""
    for char in text:
        if char in vowels:
            result += char.upper()
        else:
            result += char.lower()

    return result
input_string = "i love sushi"
print(transform_string(input_string))
