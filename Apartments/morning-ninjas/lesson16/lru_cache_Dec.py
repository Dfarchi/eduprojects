import math
from functools import lru_cache


@lru_cache
def get_factorial(num: int):
    return math.factorial(num)