import argparse
import shutil
import os

def copy_file(input_file, output_file):
    try:
        shutil.copy(input_file, output_file)
        print(f"Файл '{input_file}' успешно скопирован в '{output_file}'.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    parser = argparse.ArgumentParser(description='Копирует содержимое одного файла в другой.')
    parser.add_argument('--input', required=True, help='Имя входного файла')
    parser.add_argument('--output', required=True, help='Имя выходного файла')
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Ошибка: Файл '{args.input}' не существует.")
        return

    copy_file(args.input, args.output)

if __name__ == '__main__':
    main()