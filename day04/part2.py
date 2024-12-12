from itertools import pairwise

f = open("input.txt", "r")
lines = f.read().strip().split()
m = [ [c for c in lines[i]] for i in range(len(lines)) ]

def read(x, y):
    if x < 0 or y < 0:
        return '\0'
    try:
        return m[x][y]
    except:
        return '\0'

def solve():
    total = 0
    diffs = [
            [-1,-1], # nw
            [-1,1], # sw
            [1,-1], # ne
            [1,1], # se
            ]
    for x in range(len(m)):
        for y in range(len(m[x])):
            if read(x, y) != 'A':
                continue
            t = ''.join([ read(x+c[0], y+c[1]) for c in diffs ])
            if t in ["MMSS", "SSMM", "SMSM", "MSMS"]:
                total += 1
    return total

#m = [['X', 'M', 'A', 'S']]
print(solve())
