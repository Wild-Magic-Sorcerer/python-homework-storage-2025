import argparse
if __name__ == '__main__':
    fail = argparse.ArgumentParser(description='Копирует данные из одного файла в другой')
    fail.add_argument('--input', required=True)
    fail.add_argument('--output', default='new.txt')
    copy_fail = fail.parse_args()

    copy = ''

    with open(copy_fail.input, 'r') as old:
        copy = old.readlines()

    with open(copy_fail.output, 'w') as new:
        new.write(copy)
        print('Фаил успешно скопирован')
