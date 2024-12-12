from functools import cache
from util import *

s = input()
m = nums(s)


def blink(x):
    if x == 0:
        return [1] 
    s = str(x)
    if len(s)%2 == 0:
        m = len(s)//2
        return [int(s[:m]), int(s[m:])]
    return [x * 2024]


@cache
def solveone(x, n):
    if n == 0:
        return 1
    return sum([solveone(i, n-1) for i in blink(x)])


printc(sum([solveone(i, 75) for i in m]))
