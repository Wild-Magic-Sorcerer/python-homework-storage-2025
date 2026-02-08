def long_strings(strings: list) -> list:
    if not strings:
        return []

    total = 0
    for s in strings:
        total += len(s)

    avg_len = total / len(strings)

    result = []
    for s in strings:
        if len(s) > avg_len:
            result.append(s)

    return result
