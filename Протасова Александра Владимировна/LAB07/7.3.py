import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("strings", nargs="*")
    parser.add_argument("-c", "--count", action="store_true")

    args = parser.parse_args()

    if args.count:
        print(len(args.strings))
    else:
        for s in args.strings:
            print(s)
