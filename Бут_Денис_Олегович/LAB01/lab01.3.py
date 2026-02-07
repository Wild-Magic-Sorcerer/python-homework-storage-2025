def tuple_and_set(argument):
    return f"Кортёж слов:, {tuple(argument)}, Число уникальных слов:, {len(set(argument))}"

if __name__ == "__main__":
    list_of_words = []
    while True:
        words = input()
        if words.lower() == "n" or words == "":
            break
        list_of_words.append(words)
    print(tuple_and_set(list_of_words))
