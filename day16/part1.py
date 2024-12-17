from util import *
from heapq import heappush, heappop

s = inputtxt()
lines = s.split('\n')
m = [ c for c in lines ]
start = Vec(len(m)-2, 1)
end = Vec(1, len(m[1])-2)

def turncost(d1, d2):
    if d1 == d2: return 0
    if d1 == d2*-1: return 2000
    else: return 1000

def solve(m, start, d=East):
    table = defaultdict(lambda: 1e12)
    table[(start, East)] = 0

    q = [(0, start,d)]
    seen = set()
    while len(q) > 0:
        _, cur, facing = heappop(q)
        if cur.of(m) == '#' or (cur,facing) in seen:
            continue
        seen.add((cur,facing))

        for d in Cardinals:
            step = cur+d
            if step.of(m) == '#':
                continue
            table[(step,d)] = min(table[(step,d)],
                                  table[(cur,facing)]+1+turncost(d, facing))
            heappush(q, (table[(step,d)], step, d))

    return table

def debug(table, m):
    for r in range(1, len(m)-1):
        for c in range(1, len(m[r])-1):
            n = min([ table[(Vec(r,c),d)] for d in Cardinals ])
            if m[r][c] == '#':
                print('##### ', end='')
            elif n == 1e12:
                print('      ', end='')
            else:
                print(format(n, '05d'), end=' ')
        print()

table = solve(m, start)
debug(table, m)
printc(min([ table[(end,d)] for d in Cardinals ]))
