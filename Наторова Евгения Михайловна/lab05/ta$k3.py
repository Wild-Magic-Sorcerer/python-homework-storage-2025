if __name__ == "__main__":
    with open("ottuda.txt", "r") as source_file:
        content = source_file.read()

    with open("suda.txt", "w") as dest_file:
        dest_file.write(content)
        new_content = content.replace("cat", "dog")
        
    with open("suda.txt", "w") as file:
        file.write(new_content)

    with open("suda.txt", "r") as file:
        print(file.read())


