import re

ISBN10_REGEX = re.compile(r"^\d{9}[\dX]$")
ISBN13_REGEX = re.compile(r"^\d{13}$")


def normalize_isbn(isbn: str) -> str:
    return isbn.replace("-", "").replace(" ", "")


def is_valid_isbn10(isbn: str) -> bool:
    if not ISBN10_REGEX.match(isbn):
        return False

    total = 0
    for i, char in enumerate(isbn):
        value = 10 if char == "X" else int(char)
        total += value * (10 - i)

    return total % 11 == 0


def is_valid_isbn13(isbn: str) -> bool:
    if not ISBN13_REGEX.match(isbn):
        return False

    total = 0
    for i, digit in enumerate(isbn):
        factor = 1 if i % 2 == 0 else 3
        total += int(digit) * factor

    return total % 10 == 0


def is_valid_isbn(isbn: str) -> bool:
    return is_valid_isbn10(isbn) or is_valid_isbn13(isbn)
