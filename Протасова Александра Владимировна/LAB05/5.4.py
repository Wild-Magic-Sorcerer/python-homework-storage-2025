if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    unique_lines = []
    duplicates = []

    for line in lines:
        if line not in unique_lines:
            unique_lines.append(line)
        else:
            duplicates.append(line)

    with open('output.txt', 'w') as f:
        for line in unique_lines:
            f.write(line)

    print("Неуникальные строки:")
    for dup in duplicates:
        print(dup.strip())
