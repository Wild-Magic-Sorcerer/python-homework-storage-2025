import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, help="Входной файл")
parser.add_argument("--output", required=True, help="Выходной файл")

args = parser.parse_args()

try:
    with open(args.input, 'r', encoding='utf-8') as f_in:
        content = f_in.read()
    
    with open(args.output, 'w', encoding='utf-8') as f_out:
        f_out.write(content)
        
    print(f"Успешно! Файл '{args.input}' скопирован в '{args.output}'")
except FileNotFoundError:
    print("Ошибка: Входной файл не найден")