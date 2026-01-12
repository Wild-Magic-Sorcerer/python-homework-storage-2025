def main():
        # Сначала создадим исходный файл 
    with open("source.txt", "w") as f:
        f.write("The cat is on the mat. My cat is black.")
    
    # Копируем и заменяем
    with open("source.txt", "r") as f_src:
        content = f_src.read()
        new_content = content.replace("cat", "dog")
    
    with open("destination.txt", "w") as f_dest:
        f_dest.write(new_content)
    
    
    print("Файл скопирован, 'cat' заменено на 'dog'.")
    
if __name__ == "__main__":
    main()

