import argparse

def counter_of_str(args_object):
    if args_object.count:
        return len(args_object.strings)
    elif args_object.strings:
        return " ".join(args_object.strings)
    else:
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("strings", nargs="*", default=[])
    parser.add_argument("-c", "--count", action="store_true")

    args = parser.parse_args()
    result = counter_of_str(args)

