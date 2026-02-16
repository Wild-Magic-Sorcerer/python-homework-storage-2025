def process_file(source_file, unique_file):
    seen = set()
    duplicates = []

    with open(source_file, "r", encoding="utf-8") as file:
        for line in file:
            clean = line.rstrip()
            if clean in seen:
                duplicates.append(clean)
            else:
                seen.add(clean)

    with open(unique_file, "w", encoding="utf-8") as file:
        for line in seen:
            file.write(line + "\n")

    return duplicates


def main():
    duplicates = process_file("input.txt", "unique.txt")

    if duplicates:
        print("Неуникальные строки:")
        for line in duplicates:
            print(line)
    else:
        print("Неуникальных строк нет.")


if __name__ == "__main__":
    main()

