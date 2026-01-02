def parse_phone_number(text1):

    start = text1.find('+')
    if start != -1 and len(text1) >= start + 15:
        phone = text1[start:start + 15]

        if (len(phone) == 15 and
                phone[0] == '+' and phone[1].isdigit() and
                phone[2] == '(' and phone[3:6].isdigit() and
                phone[6] == ')' and phone[7].isdigit() and
                phone[8] == '-' and phone[9:11].isdigit() and
                phone[11] == '-' and phone[12:14].isdigit()):

            print("Найден номер:", phone)
            print("Код страны:", phone[1])
            print("Код города:", phone[3:6])
            print("Номер абонента:", phone[7] + phone[9:11] + phone[12:14])
            return phone
        else:
            print("Номер не найден")
            return None
    else:
        print("Номер не найден")
        return None

if __name__ == "__main__":
    text = input("Введите строку: ")
    parse_phone_number(text)
