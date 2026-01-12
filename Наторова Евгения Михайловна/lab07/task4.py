import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="копирование файлов")
    parser.add_argument("--input", "-i", required=True, help="исходный файл")
    parser.add_argument("--output", "-o", required=True, help="целевой файл")
    args = parser.parse_args()


    with open(args.input, 'r', encoding='utf-8') as f_in:
        content = f_in.read()

    with open(args.output, 'w', encoding='utf-8') as f_out:
        f_out.write(content)


    print(f"файл '{args.input}' успешно скопирован в '{args.output}'")
    
