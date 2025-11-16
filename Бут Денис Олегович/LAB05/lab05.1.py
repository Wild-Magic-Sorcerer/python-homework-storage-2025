def calculate_big_one(def_for_big_num):
    biggest_num = int(def_for_big_num[0])
    for num in def_for_big_num:
        if int(num) > biggest_num:
            biggest_num= int(num)
    return biggest_num


def calculate_little_one(def_for_smallest_num):
    if not def_for_smallest_num:
        return None
    smallest_num = int(def_for_smallest_num[0])
    for num in def_for_smallest_num:
        if int(num) < smallest_num:
            smallest_num = int(num)
    return smallest_num

if __name__ == "__main__":
    list_of_sum = [0]
    list_of_numbs = []
    with open("numbers_for_lab05.1.txt.txt", "r") as file_numbers:
        for line in file_numbers:
            list_of_numbs.append(int(line))
        for number in list_of_numbs:
            list_of_sum = [list_of_sum[0] + int(number)]
        print(list_of_numbs)
        print( "Наибольшее число =",calculate_big_one(list_of_numbs),"\n"
               "Наименьшее число =",calculate_little_one(list_of_numbs),"\n"
               "Среднее чисел =",list_of_sum[0]/len(list_of_numbs))
