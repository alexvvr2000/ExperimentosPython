def counter(flag: int = 10, inclusive: bool = False, curr_number: int = 0) -> None:
    if curr_number == flag:
        return

    if inclusive:
        curr_number = 1
        inclusive = False

    print(curr_number)
    curr_number += 1
    counter(flag, inclusive, curr_number)


if __name__ == "__main__":
    counter(20, True)
