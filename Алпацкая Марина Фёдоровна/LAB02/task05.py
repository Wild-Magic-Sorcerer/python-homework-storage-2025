def checking_str(stroka: str,compare: str):
    match = []
    stroka_lower = stroka.lower()
    compare_lower = compare.lower()
    for letter_compare in compare_lower.replace(" ",""):
         if not letter_compare.isalnum():
            compare_lower = compare_lower.replace(letter_compare,'')
    for letter_stroka in stroka_lower.replace(" ",""):
        if not letter_stroka.isalnum():
            stroka_lower = stroka_lower.replace(letter_stroka,'')
    for com in compare_lower.split():
        for strok in stroka_lower.split():
            if com == strok:
                match.append(com)
    if len(set(match)) == len(set(stroka_lower.split())):
        return print(f'Все слова присутствуют')
    else:
        return print(f"Перечень не совподающих слов: {set(match)}")

if __name__ == '__main__':

    words_strora = input("Пожалуйста введите строку на проверку:\n")
    words_compare = input("Пожалуйста введите строку с которой сравнивают:\n")
    checking_str(words_strora,words_compare)
