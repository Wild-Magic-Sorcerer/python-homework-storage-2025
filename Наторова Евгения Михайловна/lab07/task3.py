import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="обработка списка строк")
    parser.add_argument("strings", nargs='+', help="список строк")
    parser.add_argument("--count", '-c', action="store_true", help="подсчитать количество строк")
    args = parser.parse_args()

    if args.count:
        print(len(args.strings))
    else:
        print("Строки:")
        for s in args.strings:
            print(s)

