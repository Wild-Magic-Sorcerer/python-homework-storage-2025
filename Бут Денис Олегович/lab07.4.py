import sys

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
    input_file = sys.argv[2]
    output_file = sys.argv[4]

    copy_file(input_file, output_file)