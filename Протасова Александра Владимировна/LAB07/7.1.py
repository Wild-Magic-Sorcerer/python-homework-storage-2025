import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    args = parser.parse_args()

    print(f"Привет, {args.username}!")
