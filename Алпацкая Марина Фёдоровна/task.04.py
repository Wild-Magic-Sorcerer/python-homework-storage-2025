if __name__ == '__main__':
    unekum:list = []
    not_unekum:list = []
    with open('lins_text.txt','r') as text:
        list_text = text.readlines()

    for line in list_text:
        if not line in unekum:
                unekum.append(line)
        else:
                not_unekum.append(line)

    print(f'Повторы в файле: {set(not_unekum)}')
