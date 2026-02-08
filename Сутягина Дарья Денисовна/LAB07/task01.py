import argparse

parser = argparse.ArgumentParser(description="Приветствие пользователя")
parser.add_argument("name", help="Имя пользователя")

args = parser.parse_args()

print(f"Приветствую, {args.name}!")
