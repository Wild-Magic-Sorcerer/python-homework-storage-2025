len_function = lambda word: len(word)


if __name__ == "__main__":
    list_of_words = ["apple", "banana", "cherry"]
    len_of_words = map(len_function, list_of_words)
    print(list(len_of_words))


