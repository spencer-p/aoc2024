from util import *

s = inputtxt()
lines = s.split('\n')
coords = [ Vec(*nums(l)) for l in lines ]

R = max( v.r for v in coords )
C = max( v.c for v in coords )
end = Vec(R,C)

m = [ ['.' for i in range(C+1) ] for _ in range(R+1)]
for i in range(1024):
    v = coords[i]
    m[v.r][v.c] = '#'

def bfs(m, start, end):
    seen = set()
    costs = defaultdict(lambda: 0)
    q = deque([start])
    while len(q) > 0:
        cur = q.pop()
        if cur in seen: continue
        seen.add(cur)
        
        if cur == end:
            return costs[cur]

        for t in rangedirs(cur, Cardinals):
            if t.oob(m): continue
            if t.of(m) == '#': continue

            costs[t] = 1 + costs[cur]
            q.appendleft(t)

    return None

def bisect(f, l, h):
    while l <= h:
        m = (l+h)//2
        t = f(m)
        if t:
            l = m + 1
        else:
            h = m - 1
    return l

def check(i):
    global coords, end, R, C
    m = [ ['.' for i in range(C+1) ] for _ in range(R+1)]
    for i in range(i):
        v = coords[i]
        m[v.r][v.c] = '#'
    r = bfs(m, Vec(0,0), end)
    return r is not None

result = bisect(check, 0, len(coords))
printc(result)
print(check(result-1))
print(check(result))

# coords are indexed by 0!
printc(coords[result-1])
