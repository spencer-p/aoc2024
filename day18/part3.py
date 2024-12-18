from util import *

s = inputtxt()
lines = s.split('\n')
coords = [ Vec(*nums(l)) for l in lines ]

R = max( v.r for v in coords )
C = max( v.c for v in coords )
end = Vec(R,C)

def shortest(m, start, end):
    def succ(n):
        cds = rangedirs(n, Cardinals)
        return [ c for c in cds if not (c.oob(m) or c.of(m) == '#') ]
    costs = BFS(start, end, succ)
    return costs[end]

def check(i):
    global coords, end, R, C
    m = [ ['.' for i in range(C+1) ] for _ in range(R+1)]
    for i in range(i):
        v = coords[i]
        m[v.r][v.c] = '#'
    r = shortest(m, Vec(0,0), end)
    return r is not None

result = bisect(check, 0, len(coords))
printc(result)
print(check(result-1))
print(check(result))

# coords are indexed by 0!
printc(coords[result-1])
