import argparse
import sys

def copy_file():
    parser = argparse.ArgumentParser(description="Утилита для копирования файлов")
    parser.add_argument("--input", required=True, help="Путь к исходному файлу")
    parser.add_argument("--output", required=True, help="Путь к файлу назначения")

    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as src:
            content = src.read()

        with open(args.output, 'w', encoding='utf-8') as dst:
            dst.write(content)

        print(f"Успех! Содержимое файла '{args.input}' скопировано в '{args.output}'.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{args.input}' не найден.", file=sys.stderr)
    except PermissionError:
        print(f"Ошибка: Недостаточно прав для работы с файлами.", file=sys.stderr)
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}", file=sys.stderr)


if __name__ == "__main__":
    copy_file()