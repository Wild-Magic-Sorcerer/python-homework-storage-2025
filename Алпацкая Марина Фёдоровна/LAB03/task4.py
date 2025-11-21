def check_for_vowels (**kwargs):
    vowels:list = ["ё","у","е","ы","а","о","э","я","и","ю"]
    result: dict[str:str] = {}
    for vowels_key , vowels_value in kwargs.items():
        if isinstance(vowels_key, str) and isinstance(vowels_value, str):
            temp = 0
            for vowel_char_key in vowels_key:
                if vowel_char_key.lower() in vowels:
                    temp += 1
            if temp >= 3:
                for vowel_char_value in vowels_value:
                    if vowel_char_value.lower() in vowels:
                        temp += 1
            if temp >= 6:
                result[vowels_key] = kwargs[vowels_key]
    return result

if __name__ == '__main__':
    check_print = check_for_vowels(апу=94, уууп='кавыпвсеу', увы='уввее', ццыыыввеее='еку')
    print(check_print)
