import argparse

def main():
    parser = argparse.ArgumentParser(description="Скрипт для обработки списка строк.")
    parser.add_argument('lines', nargs='+', help='Список строк для обработки')
    parser.add_argument('--count', action='store_true', help='Вывести количество строк')
    args = parser.parse_args()

    if args.count:
        print(f'Количество введённых строк: {len(args.lines)}')
    else:
        for line in args.lines:
            print(line)

if __name__ == '__main__':
    main()