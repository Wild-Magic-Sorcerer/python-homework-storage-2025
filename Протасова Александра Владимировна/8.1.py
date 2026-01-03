import re

def parse_phone_number(text1):

    pattern = r'\+\d\(\d{3}\)\d-\d{2}-\d{2}'

    match = re.search(pattern, text1)

    if match:
        phone = match.group()
        print("Найден номер:", phone)
        print("Код страны:", phone[1])
        print("Код города:", phone[3:6])
        print("Номер абонента:", phone[7] + phone[9:11] + phone[12:14])
        return phone
    else:
        print("Номер не найден")
        return None

if __name__ == "__main__":
    text = input("Введите строку: ")
    parse_phone_number(text)
