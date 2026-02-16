import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("username", nargs="?")
    args = parser.parse_args()

    if args.username:
        print(f"Здравствуй {args.username}!")
    else:
        print("Please provide argument")

