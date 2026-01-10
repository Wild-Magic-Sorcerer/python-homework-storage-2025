if __name__ == "__main__":
    with open("ottuda.txt", "r") as source_file:
        content = source_file.read()

    with open("suda.txt", "w") as dest_file:
        dest_file.write(content)

    with open("suda.txt", "r+") as file:
        content = file.read()
        new_content = content.replace("cat", "dog")
        file.seek(0)
        file.write(new_content)
        file.truncate()

    with open("suda.txt", "r") as file:
        print(file.read())
