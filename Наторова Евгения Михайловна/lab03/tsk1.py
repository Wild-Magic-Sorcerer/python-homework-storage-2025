def filter_by_len(strings):
    if not strings:
        return []

    length = sum(len(s) for s in strings) / len(strings)
    return [s for s in strings if len(s) > length]

if __name__ == "__main__":
    stroka = ["abcd", "def", "gh", "dhdjh", "lsdfjddd"]
    filtered = filter_by_len(stroka)
    print(filtered)