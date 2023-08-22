"""
Docstring...
"""
from pprint import pprint
from sys import version, argv
import concurrent.futures as cf

x = 10
vlans = [1, 2, 3]


def sum_numbers(num1, num2):
    return num1 + num2

# res1 = sum_numbers(100, 200)
# print(f"{num1=} {num2=}")


if __name__ == "__main__":
    result = sum_numbers(1, 2)

    print("start".center(50, "="))
    print(version)
    print("end".center(50, "="))
