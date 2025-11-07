def check_for_vowels (**kwargs):
    vowels:list = ["ё","у","е","ы","а","о","э","я","и","ю"]
    result: dict[str:str] = {}
    for vowels_key in kwargs:
        if type(vowels_key) == str:
            temp = 0
            for vowel_key in vowels_key:
                if vowel_key.lower() in vowels:
                    temp += 1
            if temp >= 3:
                temp = 0
                if type(kwargs[vowels_key]) == str:
                    for vowel_valeu in kwargs[vowels_key]:
                        if vowel_valeu.lower() in vowels:
                            temp += 1
            if temp >= 3:
                result[vowels_key] = kwargs[vowels_key]
    return result

if __name__ == '__main__':
    print(check_for_vowels(апу=94, уууп='кавыпвсеу', увы='уввее', ццыыыввеее='еку'))