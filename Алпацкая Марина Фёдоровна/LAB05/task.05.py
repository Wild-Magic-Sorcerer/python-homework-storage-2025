from datetime import datetime

name_fail = 'log.txt'

def logger(login:str, time=None):
    if not time:
        time = datetime.now()
    with open('log.txt', 'a') as log:
        log.write(f'{login}, {time}\n')
    return None

if __name__ == '__main__':
    user_login = input('Введите ваш логин: ')
    logger(user_login)
    with open(name_fail,'r') as fail:
        login_read = fail.read()
        print(login_read)
