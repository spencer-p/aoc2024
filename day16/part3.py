from util import *
from heapq import heappush, heappop

s = inputtxt()
lines = s.split('\n')
m = [ c for c in lines ]
start = Vec(len(m)-2, 1)
end = Vec(1, len(m[1])-2)

def turncost(d1, d2):
    if d1 == d2: return 1
    if d1 == d2*-1: return 2001
    else: return 1001


def solve(m, start, d=East):
    succ = lambda n: [ (n[0]+d,d) for d in Cardinals if (n[0]+d).of(m) != '#' ]
    cost = lambda a, b: turncost(a[1], b[1])
    return Dijkstra((start,d), None, succ, cost)


def reversewalk(cur, facing, table):
    result = set([cur])
    curcost = table[(cur,facing)]
    for d in Cardinals:
        cost = turncost(d, facing)
        step = cur+facing*-1
        if (step,d) in table and table[(step,d)] == curcost-cost:
            result |= reversewalk(step, d, table)
    return result

table = solve(m, start)
sol = min([ table[(end,d)] for d in Cardinals if (end,d) in table])
printc(sol)
printc(len(reversewalk(end, North, table)))
