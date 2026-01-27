import re
if __name__ == '__main__':
    line = input('Введите пожалуйста дату:\n')
    data = re.sub(r'\d\d\.\d\d\.\d{4}',"DD.MM.YYYY", line)
    print(f'Отредактированное предложение:\n{data}')
