ten_random_number: list = ['6\n','8\n','1\n','-3\n','12\n','3\n','6\n','55\n','9\n','0\n']
name_faila = 'numbers.txt'

def number_chek(num: list):
    max_num = max(int(i) for i in num)
    min_num = min(int(i) for i in num)
    sum_num = sum(int(i) for i in num)/len(num)
    return min_num,max_num,sum_num

if __name__ == '__main__':
    with open(name_faila,'w+') as numbers:
        numbers.writelines(ten_random_number)

    with open(name_faila) as num_line:
        list_number = num_line.readlines()

    print(f'MAX: {number_chek(list_number)[1]}\nmin: {number_chek(list_number)[0]}\nСреднее значение: {number_chek(list_number)[2]}')
