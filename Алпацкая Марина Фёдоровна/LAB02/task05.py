def checking_str(stroka: str,compare: str):
    for letter_compare in stroka.replace(" ",""):
        if not letter_compare.isalnum():
            stroka = stroka.replace(letter_compare,'')
    for letter_stroka in compare.replace(" ",""):
        if not letter_stroka.isalnum():
            compare = compare.replace(letter_stroka,'')
    stroka_set = set(stroka.lower().split())
    compate_set = set(compare.lower().split())
    if stroka_set == compate_set:
        return 'Все строки совпадают.'
    result = ''
    if stroka_set - compate_set:
        result += f"Перечень не совподающих слов относительно первой строки: {stroka_set - compate_set}.\n"
    if compate_set - stroka_set:
        result += f"Перечень не совподающих слов относительно второй строки: {compate_set - stroka_set}."
    return result

if __name__ == '__main__':

    words_strora = input("Пожалуйста введите строку на проверку:\n")
    words_compare = input("Пожалуйста введите строку с которой сравнивают:\n")
    result_check = checking_str(words_strora,words_compare)
    print(result_check)
