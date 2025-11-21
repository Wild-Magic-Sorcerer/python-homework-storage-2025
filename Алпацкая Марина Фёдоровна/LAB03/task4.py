def check_for_vowels (**kwargs):
    vowels:list = ["ё","у","е","ы","а","о","э","я","и","ю"]
    result: dict[str:str] = {}
    for vowels_key, vowels_value in kwargs.items():
        if not isinstance(vowels_key, str) or not isinstance(vowels_value, str):
            continue
        flag_both_vowels: bool = True
        for argument_chars in (vowels_key, vowels_value):
            temp: int = 0
            for vowel_char in argument_chars:
                if vowel_char.lower() in vowels:
                    temp += 1
                if temp >= 3:
                    break
            if temp < 3:
                flag_both_vowels = False
                break
        if flag_both_vowels:
            result[vowels_key] = vowels_value
    return result

if __name__ == '__main__':
    check_print = check_for_vowels(апу=94, уууп='кавыпвсеу', увы='уввее', ццыыыввеее='еку')
    print(check_print)
