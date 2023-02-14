import math
from typing import Any


def anagram(number: int) -> Any:
    int(math.pow(number, 2))
    string_number = str(number)
    string_number_squared = str(int(math.pow(number, 2)))

    if string_number_squared.endswith(string_number):

        print("The number is an Anagram")
    else:
        print("The number is not an Anagram")


anagram(25)
