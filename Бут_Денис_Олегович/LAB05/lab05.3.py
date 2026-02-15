if __name__ == "__main__":
    with (open("first_file_for_lab05.3.txt", "r") as file1,
          open("second_file_for_lab05.3.txt", "w") as file2):
            cat_in_file2 = file1.read()
            file2.write(cat_in_file2)
    dog_in_file2 = cat_in_file2.replace("cat", "dog")
    with open("second_file_for_lab05.3.txt", "w") as file:
        file.write(dog_in_file2)

