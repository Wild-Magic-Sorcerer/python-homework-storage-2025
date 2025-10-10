def checking_str(stroka=str,compare=str):
    match = []
    stroka_list = stroka.split()
    compare = compare.lower()
    compare_list = compare.split()
    for num_word in range(len(compare_list)):
        if compare_list[num_word].isalpha() == False:
            for i in compare_list[num_word]:
                if i.isalpha() == False:
                    compare_list[num_word] = compare_list[num_word].replace(i,'')
    for word in stroka_list:
        word = word.lower()
        if word.isalpha() == False:
            for i in word:
                if i.isalpha() == False:
                    word = word.replace(i,'')
        for com in compare_list:
            if com == word:
                match.append(com)
    if len(set(match)) == len(set(stroka_list)):
        return print(f'Все слова присутствуют')
    else:
        return print(f"Перечень совподающих слов: {set(match)}")
if __name__ == '__main__':
    checking_str(input("Пожалуйста введите строку на проверку:\n"),input("Пожалуйста введите строку с которой сравнивают:\n"))