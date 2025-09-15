if __name__ == "__main__":
    a1 = input()


def d1(a1):
    a3 = a1.split(" ")
    return a3, len(set(a3))


print(d1(a1))
