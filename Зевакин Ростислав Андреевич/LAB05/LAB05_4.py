def filter_unique():
    with open("05_4.txt", "r", encoding="utf-8") as f:
        lines = [line.rstrip() for line in f]

    unique_lines = []
    duplicate_lines = []

    for line in lines:
        if line not in unique_lines and line not in duplicate_lines:
            unique_lines.append(line)
        elif line in unique_lines:
            unique_lines.remove(line)
            duplicate_lines.append(line)

    with open("output.txt", "w", encoding="utf-8") as f:
        for line in unique_lines:
            f.write(line + "\n")

    print("Неуникальные строки:", duplicate_lines)


filter_unique()