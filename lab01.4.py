if __name__ == "__main__":
    a = [1, 4, 8, 11, 31, 8, 32, 324, 8]
box_of_num = {}
for i in a:
    c = a.count(i)
    if i not in box_of_num:
        box_of_num.update(dict([(i, c)]))

    else:
        continue
print(box_of_num)
