import re

def split_string(input_string):
    words = re.split(r'[;:.,!?-]', input_string)

    words = [word.strip() for word in words if word.strip()]

    return words

user_input = input("Введите строку: ")
result = split_string(user_input)

print(result)