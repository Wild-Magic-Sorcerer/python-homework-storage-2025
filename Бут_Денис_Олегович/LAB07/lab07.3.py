import argparse

def format_strings(strings, count=False):
    if count:
        return len(strings)
    elif strings:
        return " ".join(strings)
    return None

def output(strings, count=False):
    if not strings:
        print("Не указаны строки для обработки")
    else:
        result = format_strings(strings, count)
        print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("strings", nargs="*", default=[], help="Строки для обработки")
    parser.add_argument("-c", "--count", action="store_true", help="Подсчитать количество строк")

    args = parser.parse_args()
    output(args.strings, args.count)
