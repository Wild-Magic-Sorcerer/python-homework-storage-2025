if __name__ == "__main__":
    dups = []
    uni = []
    with open("pupa.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line not in uni:
                uni.append(line)
            else:
                dups.append(line)
    with open("pupa2_0.txt", "w") as file:
        for line in uni:
            file.write(line + "\n")
print(dups)