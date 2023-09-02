from __future__ import annotations
from typing import List

"""
    CONCLUSION: The function is executed for the returned value
    either making the binary threes make sense now.
"""

# Leaves where the function left if off
def test_if(val: int = 0) -> None:
    print("\t", val)
    if val != 10:
        test_if(val + 1)

    print("\t", val)

# Leaves where the function left if off
def test_if_else(val: int = 0) -> None:
    if val == 10:
        return
    else:
        print("\t",val)
        test_if_else(val + 1)
        print("\t", val)


def test_return(id_: str = "str", val: int = 3, counter: List[int] = []) -> int:
    print(f"\tOngoing {id_}: ", val,)
    print(len(counter))
    if val == 6:
        return val
    else:
        counter.append(1 if val is 9 else 0)
        return test_return("str 1", val + 1, counter) + test_return("str 2", val + 1, counter)


if __name__ == "__main__":
    print("Back and forth with only if: \n")
    test_if()

    print("The same but with if else: \n")
    test_if_else()

    print("Now using a return value: \n")
    print(test_return())
