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


def reversewalk(start, end, table):
    def succ(n):
        cur,facing = n[0], n[1]
        curcost = table[n]
        cds = [ (cur+facing*-1,d) for d in Cardinals ]
        cds = [ c for c in cds if c in table and table[c] ==
               curcost-turncost(c[1],facing) ]
        return cds

    return DFS_all(start, end, succ)

table = solve(m, start)
sol = min([ table[(end,d)] for d in Cardinals if (end,d) in table])
printc(sol)
paths = reversewalk((end,North), (start,East), table)
printc(len(set([n[0] for path in paths for n in path])))
