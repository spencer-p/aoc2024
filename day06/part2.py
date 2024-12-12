from util import *

s = input()
m = s.split()

startr, startc = None, None
for r, row in enumerate(m):
    if '^' in row:
        startr = r
        for c, t in enumerate(row):
            if t == '^':
                startc = c
                break
        break


dirs = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1],
        ]
di = 0

def splice(s, x, c):
    return s[:x]+c+s[x+1:]

def debug(rt, ct):
    global m
    for r, row in enumerate(m):
        if r == rt:
            print(splice(row, ct, 'O'))
        else:
            print(row)

def withnew(old, rt, ct):
    m = old.copy()
    m[rt] = splice(m[rt], ct, '#')
    return m

def ingrid(r, c):
    return r >= 0 and r < len(m) and c >= 0 and c < len(m[0])

print("=======================================================")

r, c = startr, startc

def enum_positions(startr, startc, m):
    p = set()
    r, c = startr, startc
    di = 0
    while True:
        p.add((r,c))

        rn, cn = r+dirs[di][0], c+dirs[di][1]
        if not ingrid(rn, cn):
            break
        t = m[rn][cn]
        if t == '#':
            di = (di+1)%4
        else:
            r, c = rn, cn
    return p

def detect_cycle(startr, startc, m):
    p = set()
    r, c = startr, startc
    di = 0

    while True:
        if (r,c,di) in p:
            return True
        p.add((r,c,di))

        rn, cn = r+dirs[di][0], c+dirs[di][1]
        if not ingrid(rn, cn):
            break
        t = m[rn][cn]
        if t == '#':
            di = (di+1)%4
        else:
            r, c = rn, cn
    return False


positions = enum_positions(startr, startc, m)
printc(len(positions))
total = ctrue([detect_cycle(startr, startc, withnew(m, p[0], p[1])) for p in
               positions])
printc(total)

# Key observation: the new obstacle had to be on the old path.
