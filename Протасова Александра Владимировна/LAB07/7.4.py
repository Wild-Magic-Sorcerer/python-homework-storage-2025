import sys

if __name__ == "__main__":
    args = sys.argv

    if '--input' not in args or '--output' not in args:
        print("Использование: --input, --output ")
        sys.exit(1)

    input_index = args.index('--input')
    output_index = args.index('--output')

    input_file = args[input_index + 1]
    output_file = args[output_index + 1]

    try:
        with open(input_file, 'r') as f:
            content = f.read()

        with open(output_file, 'w') as f:
            f.write(content)

        print(f"Файл успешно скопирован из '{input_file}' в '{output_file}'")

    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден")
