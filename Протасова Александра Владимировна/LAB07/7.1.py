import sys

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Ошибка: необходимо указать имя пользователя")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Привет, {username}!")
