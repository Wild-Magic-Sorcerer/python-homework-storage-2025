import re

if __name__ == "__main__":
    input_string = input("Строка с датой:")
    pattern = r"\d{2}\.\d{2}\.\d{4}"
    result = re.sub(pattern, "DD.MM.YYYY", input_string)
    print(f"Результат замены: {result}")



