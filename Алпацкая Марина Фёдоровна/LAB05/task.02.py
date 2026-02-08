if __name__ == '__main__':
    text_user = input(f'Введити строку в фаил:\n')
    with open("input_fail",'a') as fail:
        fail.write(text_user + '\n')
    with open("input_fail",'r') as fail:
        print(fail.read())
