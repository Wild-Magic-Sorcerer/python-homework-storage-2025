#!/usr/bin/env python3

def is_palindrome(input_text: str) -> tuple[bool, int | None]:
    text_length = len(input_text)
    half_length = text_length // 2
    
    for position in range(half_length):
        left_char = input_text[position]
        right_char = input_text[text_length - 1 - position]
        if left_char != right_char:
            return False, position
    
    return True, None


def format_result(text: str, is_pal: bool, mismatch_index: int | None) -> None:
    if is_pal:
        print(f"Строка '{text}' является палиндромом")
    else:
        if mismatch_index is not None:
            left_pos = mismatch_index
            right_pos = len(text) - 1 - mismatch_index
            left_char = text[left_pos]
            right_char = text[right_pos]
            print(f"Строка '{text}' не является палиндромом")
            print(
                f"Несовпадение на позициях {left_pos} ('{left_char}') "
                f"и {right_pos} ('{right_char}')"
            )


def main() -> None:
    user_input = input("Введите строку для проверки: ").strip()
    
    if not user_input:
        print("Пустая строка считается палиндромом")
        return
    
    palindrome_result, mismatch_pos = is_palindrome(user_input)
    format_result(user_input, palindrome_result, mismatch_pos)


if __name__ == "__main__":
    main()
