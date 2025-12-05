numbers = [2, 1, 2, 2, 3, 4, 1, 7, 3]


def main(numb):
    count = {}
    for x in numb:
        count[x] = count.get(x, 0) + 1

    for number, cnt in count.items():
        print(number, "—", cnt)


if __name__ == "__main__":
    main(numbers)