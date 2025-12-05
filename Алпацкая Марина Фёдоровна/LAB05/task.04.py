if __name__ == '__main__':
    unekum:list = []
    not_unekum:list = []
    with open('lins_text.txt','r') as text:
        list_text = text.readlines()

    for line in list_text:
        if line not in unekum:
            unekum.append(line)
        elif line not in not_unekum:
            not_unekum.append(line)

    print(f'Повторы в файле: {not_unekum}')
