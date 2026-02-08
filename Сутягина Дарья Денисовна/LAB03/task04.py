def filters(**kwargs):
    vowels = "аеёиоуыэюяaeiouy"
    result = {}

    for key, value in kwargs.items():
        if type(value) is str:
            count = 0
            for char in value.lower():
                if char in vowels:
                    count += 1

            if count >= 3:
                result[key] = value

    return result
