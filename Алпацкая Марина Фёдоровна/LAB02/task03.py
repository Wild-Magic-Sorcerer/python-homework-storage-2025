if __name__ == '__main__':
    highlight_vowels = input("Введите слово на прверку:\n")
    highlight_vowels = highlight_vowels.lower()
    original = "ёуеыаоэяию"
    new = original.upper()

    trans_high = highlight_vowels.translate(str.maketrans(original, new))
    print(trans_high)
