import argparse


def main():
    parser = argparse.ArgumentParser(description='Скрипт для обработки списка строк')

    parser.add_argument(
        'strings',
        nargs='+',
        help='Список строк для обработки'
    )

    parser.add_argument(
        '-c', '--count',
        action='store_true',  # флаг без значения
        help='Подсчитать количество строк вместо их вывода'
    )

    args = parser.parse_args()

    if args.count:
        print(len(args.strings))
    else:
        for s in args.strings:
            print(s)


if __name__ == '__main__':
    main()