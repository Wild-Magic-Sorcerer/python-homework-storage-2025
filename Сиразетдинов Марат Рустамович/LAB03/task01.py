def filter_long_strings(strings):
    if not strings:
        return []

    total_length = (sum(len(s) for s in strings))
    average_length = total_length / len(strings)
    result = [len(s) for s in strings if len(s) > average_length]
    return result
