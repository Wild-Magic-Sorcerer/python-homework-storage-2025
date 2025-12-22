if __name__ == '__main__':
    copy_fail = ''
    with open('cat.txt', 'r') as cat:
        copy_fail = cat.readlines()

    with open("dog.txt", 'w') as dog:
        for line in copy_fail:
            new_dog = line.replace('cat', 'dog')
            dog.write(new_dog)
