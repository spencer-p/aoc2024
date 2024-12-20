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
    return BFS(start,end,succ)

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
        if t.of(m) != '#':
            r.extend(DFS(m, t, end, depth+1, cheatstart=cheatstart, seen=seen))
    if cheatstart is None:
        for t in cheatspots(m, start):
            r.extend(DFS(m, t, end, depth+(start-t).piecelen(), cheatstart=start, seen=seen))
    return r

def cheatspots(m, v):
    result = []
    for r in range(-20, 21):
        for c in range(-20, 21):
            if abs(r)+abs(c) > 20:
                continue
            cd = v+Vec(r,c)
            if not cd.oob(m) and cd.of(m) != '#':
                result.append(cd)
    return result

costs = bestnocheat(m,S,E)
best = costs[E]
paths = DFS(m, S, E)
printc(ctrue(list(map(lambda x: best-x >= 100, paths))))
