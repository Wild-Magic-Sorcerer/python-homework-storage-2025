import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    try:
        with open(args.input, 'r') as f_in:
            content = f_in.read()

        with open(args.output, 'w') as f_out:
            f_out.write(content)

        print(f"Файл скопирован из '{args.input}' в '{args.output}'")
    except FileNotFoundError:
        print(f"Файл '{args.input}' не найден")
