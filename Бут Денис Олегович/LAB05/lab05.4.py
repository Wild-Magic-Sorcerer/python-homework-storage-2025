if __name__ == '__main__':
    with open("file1_for_lab05.4.txt", "r") as main_file:
        animals = main_file.readlines()
    not_unique = []
    unique = []
    with open("file2_for_lab05.4.txt", "a") as write_file:
        for unidentified_animal in animals:
            if unidentified_animal not in unique:
                write_file.write(unidentified_animal)
                unique.append(unidentified_animal)
            elif unidentified_animal in unique:
                not_unique.append(unidentified_animal)

    print(f"Не уникальные строки из файла: {not_unique}")

