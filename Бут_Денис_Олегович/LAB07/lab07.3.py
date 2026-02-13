import argparse

def format_strings(strings, count=False):

    if count:
        return len(strings)
    elif strings:
        return " ".join(strings)
    return None

def output(arg):
    if not arg.strings:
        print("Ошибка: не указаны строки для обработки")
    else:
        result = format_strings(arg.strings, arg.count)
        print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("strings", nargs="*", default=[], help="Строки для обработки")
    parser.add_argument("-c", "--count", action="store_true", help="Подсчитать количество строк")

    args = parser.parse_args()
    output(args)


