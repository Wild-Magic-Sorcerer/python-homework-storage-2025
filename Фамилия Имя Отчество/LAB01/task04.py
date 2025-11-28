lin = [52, 2, 5, 52, 43, 67, 45344, 228, 25552, 252525, 5, 2, 52]
if __name__ == '__main__':
    diznuts = {}
    for i in lin:
        if i not in diznuts:
            diznuts[i] = 1
        else:
            diznuts[i] += 1
    for su in diznuts:
        print(f"chislo '{su}' vstrechaetsa: {diznuts.get(su)} raz")
