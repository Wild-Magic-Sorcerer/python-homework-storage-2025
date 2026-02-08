def filter(**kwargs):
    sets = set('аеёиоуыэюяaeiou')
    result = {}

    for key, value in kwargs.items():
        if isinstance(value, str):
            count = sum(1 for char in value.lower() if char in sets)
            if count >= 3:
                result[key] = value

    return result

if __name__ == "__main__":
    res = filter(str1 = "комната",
                    str2 = "дом",
                    str3 = "стул",
                    str4 = "камешки")
    print(f"результат: {res}")


