import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        exit()

    if args[-1] == "-c":
        print(len(args) - 1)

    else:
        for s in args:
            print(s)
