import argparse

def format_strings(strings, count=False):

    if count:
        return len(strings)
    elif strings:
        return " ".join(strings)
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("strings", nargs="*", default=[], help="Строки для обработки")
    parser.add_argument("-c", "--count", action="store_true", help="Подсчитать количество строк")

    args = parser.parse_args()
    result = format_strings(args.strings, args.count)
    print(result)

