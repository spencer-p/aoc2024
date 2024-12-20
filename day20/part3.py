from util import *

s = inputtxt()
m = [ [c for  c in line] for line in s.split('\n')]

for r in range(len(m)):
    for c in range(len(m[r])):
        match m[r][c]:
            case 'S': S = Vec(r,c)
            case 'E': E = Vec(r,c)

def bestnocheat(m,start,end):
    def succ(n):
        return [c for c in rangedirs(n, Cardinals) if not c.oob(m) and c.of(m)
                != '#']
    costs = BFS(start,end,succ)
    return costs

def DFS(m, start, end, depth=0, cheatstart=None, seen=None):
    global costs, best
    if cheatstart is not None and start in costs:
        # then the solution is directly computable
        return [best-(costs[start]-depth)]

    if seen is None: seen = set()
    if start == end: return [depth]
    if (start,cheatstart) in seen:
        return []
    seen.add(( start, cheatstart ))
    r = []
    for t in rangedirs(start, Cardinals):
        if t.oob(m): continue
        if (t,cheatstart) in seen: continue

        if t.of(m) == '#':
            if cheatstart is None:
                r.extend(DFS(m, t, end, depth+1, cheatstart=start, seen=seen))
        else:
            r.extend(DFS(m, t, end, depth+1, cheatstart=cheatstart, seen=seen))
    return r

def cheatspots(m, v):
    result = []
    for r in range(-21, 21):
        for c in range(-21+r, 21-r):
            diff = Vec(r,c)
            cd = v+diff
            if not cd.oob(m) and cd.of(m) != '#':
                result.append(cd)
    return result

print(cheatspots(m, Vec(0,0)))

costs = bestnocheat(m,S,E)
best = costs[E]
print("best is", best)
paths = DFS(m, S, E)
#print(list(map(lambda x: best-x > 0, paths)))
printc(ctrue(list(map(lambda x: best-x >= 100, paths))))
