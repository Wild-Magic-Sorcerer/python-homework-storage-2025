if __name__ == "__main__":
    words = ["apple", "banana", "cherry"]

    length = list(map(lambda x: len(x), words))
    print(f"длины строк {length}")