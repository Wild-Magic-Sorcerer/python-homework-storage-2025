def get_word_lengths(words_list):
    return list(map(lambda s: len(s), words_list))

def main():
    words = ["apple", "banana", "cherry"]
    lengths = get_word_lengths(words)

    print(f"Исходный список: {words}")
    print(f"Список длин:    {lengths}")

if __name__ == "__main__":
    main()
    

