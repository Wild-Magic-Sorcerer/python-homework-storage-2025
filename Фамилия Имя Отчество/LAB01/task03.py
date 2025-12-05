if __name__ == '__main__':
    word = input("vvidite slova:")
    wordtup = tuple(word.split(" "))
    wordset = set(word.split(" "))

    print(f"unikalny slova: {len(wordset)}")
