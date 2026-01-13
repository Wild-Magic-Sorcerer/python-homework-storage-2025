import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="приветствие")
    parser.add_argument("username", help="имя пользователя для обработки")
    args = parser.parse_args()
    print(f"привет, {args.username}")
