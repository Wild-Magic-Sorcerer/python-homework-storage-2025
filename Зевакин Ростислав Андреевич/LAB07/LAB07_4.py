import argparse


def main():
    parser = argparse.ArgumentParser(description='Копирование содержимого файла')

    parser.add_argument('--input', required=True, help='Имя входного файла')
    parser.add_argument('--output', required=True, help='Имя выходного файла')

    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as infile:
            content = infile.read()

        with open(args.output, 'w', encoding='utf-8') as outfile:
            outfile.write(content)

        print(f'Файл успешно скопирован из {args.input} в {args.output}')

    except FileNotFoundError:
        print(f'Ошибка: файл {args.input} не найден')
    except IOError as e:
        print(f'Ошибка ввода-вывода: {e}')


if __name__ == '__main__':
    main()