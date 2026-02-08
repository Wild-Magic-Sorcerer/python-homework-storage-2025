import argparse

parser = argparse.ArgumentParser(description="Копирование содержимого файла")

parser.add_argument(
    "--input",
    required=True,
    help="Имя входного файла"
)

parser.add_argument(
    "--output",
    required=True,
    help="Имя выходного файла"
)

args = parser.parse_args()

try:
    with open(args.input, "r", encoding="utf-8") as src:
        content = src.read()

    with open(args.output, "w", encoding="utf-8") as dst:
        dst.write(content)

    print(f"Файл успешно скопирован из '{args.input}' в '{args.output}'")

except FileNotFoundError:
    print("Ошибка: файл не найден")
except PermissionError:
    print("Ошибка: недостаточно прав для чтения или записи файла")
