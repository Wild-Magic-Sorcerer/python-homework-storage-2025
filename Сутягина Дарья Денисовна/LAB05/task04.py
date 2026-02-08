source_file = "input.txt"
unique_file = "unique.txt"

seen = set()
dubls = []

with open(source_file, "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.rstrip()

        if clean_line in seen:
            dubls.append(clean_line)
        else:
            seen.add(clean_line)

with open(unique_file, "w", encoding="utf-8") as file:
    for line in seen:
        file.write(line + "\n")

if dubls:
    print("Неуникальные строки:")
    for line in dubls:
        print(line)
else:
    print("Неуникальных строк нет")
