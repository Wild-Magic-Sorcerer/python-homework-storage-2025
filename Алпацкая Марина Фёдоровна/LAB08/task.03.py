import re
if __name__ == '__main__':
    line = input('Введите пожалуйста предложение:\n')
    list_word = re.split(r'[.,?!-]', line.replace(' ', ''))

    print(f'Список слов из предложения\n{list_word}')
