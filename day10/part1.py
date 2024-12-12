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


    nines = set()
    seen = set([(r,c)])
    q = deque([(r,c)])
    while len(q) > 0:
        cur = q.pop()
        height = m[cur[0]][cur[1]]
        if height == 9:
            nines.add(cur)
            continue

        for r2, c2 in cardinals(*cur):
            if oob(m, r2, c2):
                continue
            if (r2, c2) in seen:
                continue
            height2 = m[r2][c2]
            if height2 == height+1:
                seen.add((r2, c2))
                q.appendleft((r2, c2))

    return nines

total = 0
for r in range(len(m)):
    for c in range(len(m[r])):
        if m[r][c] != 0:
            continue
        score = len(walk(m, r, c))
        if score > 0:
            print(r, c, "has score", score)
        total += score

printc(total)
