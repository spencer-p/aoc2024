from functools import cache
from util import *

s = input()
m = nums(s)

def flatten(xss):
    return [x for xs in xss for x in xs]

@cache
def blink(x):
    if x == 0:
        return [1] 
    s = str(x)
    if len(s)%2 == 0:
        m = len(s)//2
        return [int(s[:m]), int(s[m:])]
    return [x * 2024]

def solve(m, n):
    for i in range(n):
        m = flatten(map(blink, m))
    return m


printc(len(solve(m, 25)))
