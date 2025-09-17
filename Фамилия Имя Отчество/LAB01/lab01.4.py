Main_list = [1, 4, 8, 11, 31, 8, 32, 324, 8]
box_of_num = {}
for i in Main_list:
    c = Main_list.count(i)
    if i not in box_of_num:
        Main_dict = {i: c}
        box_of_num.update(dict(Main_dict))

    else:
        continue
print(box_of_num)
if __name__ == "__main__":
    ...
