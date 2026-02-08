def vowel_counter(**kwargs):
    if not kwargs:
        return None

    vowels = "aeiou"
    result = {}

    for key, word in kwargs.items():
        count = 0
        for letter in word:
            if letter in vowels:
                count += 1
        if count >= 3:
            result[key] = word

    return result

if __name__ == '__main__':
    print(vowel_counter(arg1="value1", arg2="value2", arg3="value3"))



