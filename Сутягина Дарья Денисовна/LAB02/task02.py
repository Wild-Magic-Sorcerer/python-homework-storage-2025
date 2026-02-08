def analyze_string(text: str) -> dict:
    text = text.strip()

    result = {
        "words": 0,
        "letters": 0,
        "digits": 0,
        "spaces": 0,
        "punctuation": 0
    }

    if text:
        result["words"] = len(text.split())

    punctuation_marks = ".,!?;:-()\"'"

    for char in text:
        if char.isalpha():
            result["letters"] += 1
        elif char.isdigit():
            result["digits"] += 1
        elif char == " ":
            result["spaces"] += 1
        elif char in punctuation_marks:
            result["punctuation"] += 1

    return result
