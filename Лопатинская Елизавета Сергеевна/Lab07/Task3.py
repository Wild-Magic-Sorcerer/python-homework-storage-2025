import argparse

def main():
    parser = argparse.ArgumentParser(description="Обработка списка строк")
    parser.add_argument("strings", nargs="+", help="Список строк для обработки")
    parser.add_argument("-c", "--count", action="store_true",
                        help="Вывести количество строк вместо самих строк")

    args = parser.parse_args()

    if args.count:
        print(f"Количество введенных строк: {len(args.strings)}")
    else:
        print("Введенные строки:")
        for s in args.strings:
            print(f"- {s}")

if __name__ == "__main__":

    main()

