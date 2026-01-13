import re

def replace_dates(input_string):
    date_pattern = r'\b(\d{2})\.(\d{2})\.(\d{4})\b'

    def replace_with_letters(match):
        return 'DD.MM.YYYY'

    result = re.sub(date_pattern, replace_with_letters, input_string)

    return result

input_string = "Сегодня 16.05.2004, а завтра 17.05.2004."
output_string = replace_dates(input_string)
print(output_string)