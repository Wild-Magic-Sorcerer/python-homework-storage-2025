# Реализуйте простую систему ведения лога: создайте функцию с именем logger
# которая принимает текст сообщения от пользователя и время (по умолчанию — текущее)
# и записывает лог в отдельный файл (log.txt), дописывая в конец файла каждое новое сообщение

from datetime import datetime as dt

def loger(user_str):
    with open('log.txt', 'a') as log:
        log.write(f'{user_str} | {dt.now()}\n')
user = str(input('Введи-те свой текст '))
loger(user)
print('Ваш текст сохранён в файл: log.txt')
