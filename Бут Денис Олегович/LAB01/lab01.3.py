words = input()


def tuple_and_set(words):
    split_w = words.split(" ")
    return print("Кортёж слов:", split_w, "Число уникальных слов:", len(set(split_w)))


if __name__ == "__main__":
    words = input() 
    print(tuple_and_set(words))
