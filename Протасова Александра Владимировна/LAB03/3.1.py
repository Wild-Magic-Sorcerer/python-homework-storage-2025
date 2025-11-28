def filter_strings(strings):
    if not strings:
        return []

    avg = sum([len(s) for s in strings]) / len(strings)
    return [s for s in strings if len(s) > avg]

if __name__ == "__main__":
    test1 = ["apple", "banana", "kiwi", "orange", "pear"]

    print(filter_strings(test1))
    print(filter_strings([]))
