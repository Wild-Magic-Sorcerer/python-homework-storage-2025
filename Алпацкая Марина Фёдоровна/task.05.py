from datetime import datetime

def logger(login:str, time=datetime.now()):
    print(time)
    with open('log.txt', 'a') as log:
        log.write(f'{login}, {time}')
    return 'log.txt'

if __name__ == '__main__':
    user_login = input('Введите ваш логин: ')
    login_fail = logger(user_login)
    with open(login_fail,'r') as fail:
        login_read = fail.read()
        print(login_read)
