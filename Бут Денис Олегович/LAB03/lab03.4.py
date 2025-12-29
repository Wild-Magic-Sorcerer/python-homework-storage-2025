def vowel_counter(**kwargs):
    if not kwargs:
        return None
    vowels = "aeiou"
    list_of_dicts = []
    count = 0
    for arg,word in kwargs.items():
        for vowel in word:
            if vowel in vowels:
                count += 1
        if count >= 3:
            list_of_dicts.append({arg:word})
    return list_of_dicts

if __name__ == '__main__':
    print(vowel_counter( arg1 = "value1",arg2 = "value2",arg3 = "value3" ))



