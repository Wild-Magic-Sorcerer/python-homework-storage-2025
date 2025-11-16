if __name__ == '__main__':
    with open("file1_for_lab05.4.txt", "r") as main_file:
        with open("file2_for_lab05.4.txt", "a") as write_file:
            animals = main_file.read().splitlines()
            print(animals)
            mammals = []
            for unidentified_animal in animals:
                if animals.count(unidentified_animal) == 1:
                    new_write_file = write_file.write(f"{unidentified_animal}\n")
                else:
                    mammals.append(unidentified_animal)
    print(set(mammals))
