#!/usr/bin/env python3

import re
regular = re.compile("[a-zA-Z]")


def is_special(char: str) -> bool:
    return regular.match(char) == None


def is_palindrome(input: str) -> bool:
    str_len = len(input)
    start_pos = 0
    end_pos = str_len - 1
    while start_pos < end_pos:
        while is_special(input[end_pos]):
            end_pos -= 1
        if input[start_pos].lower() != input[end_pos]:
            return False
        start_pos += 1
        end_pos -= 1
        while is_special(input[start_pos]):
            start_pos += 1
    return True


if __name__ == "__main__":
    print(f"racecar {is_palindrome('racecar')}")

    odd = "Never odd or even"
    print(f"{odd}: {is_palindrome(odd)}")