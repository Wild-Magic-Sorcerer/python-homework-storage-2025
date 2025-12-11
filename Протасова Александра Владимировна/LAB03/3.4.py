def find_strings(**kwargs):
    result = {}
    vowels = 'aeiou'

    for key, value in kwargs.items():
        if type(value) == str:
            vowel_count = 0
            for char in value:
                if char.lower() in vowels:
                    vowel_count += 1
            if vowel_count >= 3:
                result[key] = value

    return result

if __name__ == "__main__":
    print(find_strings(a="hello", b="world", c="amazing"))
    print(find_strings(x="hi", y="bye"))
    print(find_strings(word="education"))
