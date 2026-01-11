import argparse

def main():
    parser = argparse.ArgumentParser(description="Простой приветственный скрипт")
    parser.add_argument("name", help="Имя пользователя для приветствия")
    args = parser.parse_args()

    print(f"Привет, {args.name}! Добро пожаловать.")

if __name__ == "__main__":
    main()

