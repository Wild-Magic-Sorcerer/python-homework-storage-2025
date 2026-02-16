def copy_and_replace(source, target):
    with open(source, "r", encoding="utf-8") as src:
        content = src.read()

    content = content.replace("cat", "dog")

    with open(target, "w", encoding="utf-8") as tgt:
        tgt.write(content)


def main():
    copy_and_replace("source.txt", "target.txt")
    print("Готово. Слова 'cat' заменены на 'dog'.")


if __name__ == "__main__":
    main()
    

