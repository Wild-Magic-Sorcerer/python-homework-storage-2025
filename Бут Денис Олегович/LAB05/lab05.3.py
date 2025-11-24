if __name__ == "__main__":
    with open("second_file_for_lab05.3.txt.txt", "w") as file2:
        with open("first_file_for_lab05.3.txt.txt", "r") as file1:
            cat_in_file2 = file2.write(file1.read())
    with open("second_file_for_lab05.3.txt.txt", "r") as file2:
        cat_in_file2 = file2.read()
        dog_in_file2 = cat_in_file2.replace("cat", "dog")
    with open("second_file_for_lab05.3.txt.txt", "w") as file2:
        file2.write(dog_in_file2)


