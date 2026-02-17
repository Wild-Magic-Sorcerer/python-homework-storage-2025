def filter_long_strings(strings):
    if not strings:
        return []

    avg_length = sum(len(s) for s in strings) / len(strings)
    return [s for s in strings if len(s) > avg_length]

test1 = ["cat", "elephant", "dog", "giraffe", "mouse"]
print(filter_long_strings(test1))

test2 = ["a", "bb", "ccc", "dddd"]
print(filter_long_strings(test2))

test3 = []
print(filter_long_strings(test3))

test4 = ["один", "два", "три"]
print(filter_long_strings(test4))