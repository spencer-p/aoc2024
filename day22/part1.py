from util import *

s = inputtxt()
lines = s.split('\n')
nums = list(map(int, lines))

def mixprune(a, b):
    a ^= b
    a = a % 16777216 # this is 2 to the 24
    return a

def secretn(s, n):
    for i in range(n):
        s = mixprune(s, s*64)
        s = mixprune(s, s//32)
        s = mixprune(s, s*2048)
    return s

secretn(123, 10)
printc(sum(map(lambda seed: secretn(seed, 2000), nums)))
