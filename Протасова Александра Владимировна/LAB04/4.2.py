strings = ["apple", "banana", "cherry"]

if __name__ == "__main__":
    lengths = list(map(lambda x: len(x), strings))
    print("Исходный список:", strings)
    print("Длины строк:", lengths)
