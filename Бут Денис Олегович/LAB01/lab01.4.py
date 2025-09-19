main_list = [1, 4, 8, 11, 31, 8, 32, 324, 8]
box_of_num = {}
for i in main_list:
    c = main_list.count(i)
    if i not in box_of_num:
        box_of_num.update({i: c})

    else:
        continue
if __name__ == "__main__":
    print(box_of_num)
