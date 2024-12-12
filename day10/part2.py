from util import *

s = input()
lines = s.split('\n')
m = [ list(map(int, l)) for l in lines ]

def oob(m, r, c):
    return r < 0 or c < 0 or r >= len(m) or c >= len(m[r])

dirs = [ ( 0, 1 ), ( 1, 0 ), ( -1, 0 ), ( 0, -1 ) ]

def cardinals(r, c):
    return [ (r+i, c+j) for (i, j) in dirs]

def walk(m, r, c, seen=None):
    if oob(m, r, c):
        return 0
    if seen is None:
        seen = set((r,c))

    seen.add((r,c))
    if m[r][c] == 9:
        return 1

    total = 0
    q = cardinals(r,c)
    height = m[r][c]
    for r, c in q:
        if (r,c) in seen or oob(m,r,c):
            continue
        if m[r][c] != height+1:
            continue
        newseen = seen.copy()
        total += walk(m, r, c, seen=newseen)

    return total

print(walk(m, 0, 2))


total = 0
for r in range(len(m)):
    for c in range(len(m[r])):
        if m[r][c] != 0:
            continue
        score = walk(m, r, c)
        if score > 0:
            print(r, c, "has score", score)
        total += score

printc(total)
