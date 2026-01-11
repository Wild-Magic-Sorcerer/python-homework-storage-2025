import data
def mask_dates(text):
    date_pattern = r"\d{2}\.\d{2}\.\d{4}"
    result = re.sub(date_pattern, "DD.MM.YYYY", text)
    return result

# Пример работы
user_input = input("Введите текст, содержащий даты (например, 01.01.2024): ")
output = mask_dates(user_input)

print("\nРезультат обработки:")
print(output)