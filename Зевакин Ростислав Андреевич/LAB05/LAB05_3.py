def replacement():

    Cat_Dog = "Cat_Dog.txt"
    output_file = "output.txt"

    try:
        with open(Cat_Dog, "r", encoding="utf-8") as f_in:
            content = f_in.read()

        new_content = content.replace("cat", "dog")

        with open(output_file, "w", encoding="utf-8") as f_out:
            f_out.write(new_content)

        print(f" Файл скопирован: {Cat_Dog} → {output_file}")
        print(f" Замена 'cat' на 'dog': {content.count('cat')}")

        print("Пример изменений:")
        lines = content.split('\n')
        for i, line in enumerate(lines[:3]):
            if 'cat' in line:
                new_line = line.replace('cat', 'dog')
                print(f" Строка {i + 1}: {line} -> {new_line}")

    except FileNotFoundError:
        print(f" Файл {Cat_Dog} не найден!")

replacement()