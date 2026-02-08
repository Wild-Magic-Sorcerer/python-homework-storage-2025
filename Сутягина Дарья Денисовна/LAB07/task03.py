import argparse

parser = argparse.ArgumentParser(description="Обработка списка строк")

parser.add_argument(
    "strings",
    nargs="+",
    help="Список строк"
)

# Необязательный флаг подсчёта
parser.add_argument(
    "--count",
    action="store_true",
    help="Вывести количество строк"
)

args = parser.parse_args()

if args.count:
    print("Количество строк:", len(args.strings))
else:
    print("Введённые строки:")
    for s in args.strings:
        print(s)
