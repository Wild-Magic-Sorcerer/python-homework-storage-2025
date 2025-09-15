if __name__ == "__main__":
    a1 = input()
    a2 = a1.split(" ")
    b1 = [0]
    print(a2)

    def bigOne(a2):
        greatOne = int(a2[0])
        for i in a2:
            a3 = int(i)
            if a3 > greatOne:
                greatOne = a3
        return greatOne

    def littleOne(a2):
        smallOne = int(a2[0])
        for d in a2:
            a4 = int(d)
            if a4 < smallOne:
                smallOne = a4
        return smallOne

    for v in a2:
        a5 = int(v)
        b1 = [b1[0] + a5]

print(bigOne(a2), littleOne(a2), b1)
