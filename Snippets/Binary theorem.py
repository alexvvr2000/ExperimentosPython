import re


def bin_theorem(val1, val2, exp):
    pass


if __name__ == "__main__":
    formulas = [
        ("2x", "-6", "2"),
        ("x", "3y", "2"),
        ("3x", "1", "3"),
        ("a", "2b", "6"),
        ("2a", "-3b", "4"),
        ("s", "-7", "7"),
        ("1", "y", "3"),
        ("4p", "-q", "5"),
        ("r", "-6", "8"),
        ("x", "1", "4")
    ]

    for val_set in formulas:
        print(re.split(r"(\d)|([-+])|([a-zA-Z])", val_set[0]))
