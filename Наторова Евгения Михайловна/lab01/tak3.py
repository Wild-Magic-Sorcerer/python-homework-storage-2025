if __name__ == "__main__":
    user = input("введите строку слов")

    words = tuple(user.split())

    print(f"Созданный кортеж {words},"
          f"Количество уникальных слов: {len(set(words))}")
