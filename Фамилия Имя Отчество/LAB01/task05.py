li = [-1, -2, -3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 14, 15]
print(li)
if __name__ == '__main__':
    lis = [i for i in li if i % 3 == 0]
    print(lis)
