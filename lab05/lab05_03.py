# Напишите скрипт, который копирует содержимое одного текстового файла в другой
# а затем заменяет во втором файле все вхождения слова "cat" на слово "dog"

list_cnd = []
with open('lab05_03_file_f.txt', 'r+') as file_with_cat:
    while True:
        list_cnd = file_with_cat.readline().replace('cat\n', 'dog\n')
        if not list_cnd:
            continue
        with open('lab05_03_file_s.txt', 'a') as file_with_dog:
            file_with_dog.write(list_cnd)
