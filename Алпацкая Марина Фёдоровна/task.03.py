if __name__ == '__main__':
    copy_fail = ''
    with open('cat.txt', 'r') as cat:
        copy_fail = cat.read()

    with open("dog.txt", 'w') as dog:
        new_dog = copy_fail.replace('cat','dog')
        dog.write(new_dog)
