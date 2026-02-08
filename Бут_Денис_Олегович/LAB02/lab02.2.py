
def analyze_string(input_string):
    if not input_string:
        return None
    input_string = input_string.strip()

    result = {"words": 0, "letters": 0, "digits": 0, "spaces": 0, "punctuation": 0}

    if input_string:
        result["words"] = len(input_string.split())

    for symb in input_string:
        if "а" <= symb.lower() <= "я" or "a" <= symb.lower() <= "z":
            result["letters"] += 1
        elif "0" <= symb <= "9":
            result["digits"] += 1
        elif symb == " ":
            result["spaces"] += 1
        elif symb in ".,!?;:-":
            result["punctuation"] += 1

    return result

if __name__ == "__main__":

    text = "Пример строки, с 12 и знаками!!?"
    print(analyze_string(text))