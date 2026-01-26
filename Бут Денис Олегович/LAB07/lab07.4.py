import argparse

def copy_file(source, target):
    try:
        with open(source, 'r') as inputfile:
            content = inputfile.read()
        with open(target, 'w') as outputfile:
            outputfile.write(content)
        print(f"Данные из файла: {source}, успешно загружены в: {target}")
    except FileNotFoundError:
        print(f"Файл {source} не найден")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True,metavar="SOURCE", help="файл для копирования")
    parser.add_argument("-o", "--output", required=True, metavar="TARGET", help="файл для записи")

    args = parser.parse_args()
    copy_file(args.input, args.output)

