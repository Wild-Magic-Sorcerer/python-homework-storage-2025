def filter_long_strings(strings):
    lengths = [len(s) for s in strings]

    average_length = sum(lengths) / len(strings) if strings else 0

    long_strings = [s for s in strings if len(s) > average_length]

    return long_strings

input_strings = ["яблоко", "банан", "черешня", "вишня", "арбуз", "виноград"]
result = filter_long_strings(input_strings)
print(result)