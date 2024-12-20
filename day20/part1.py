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
    return costs[end]

def debug(m, costs):
    for r in range(len(m)):
        for c in range(len(m[r])):
            opts = [ costs[(Vec(r,c),n,b)] for n in range(3) for b in [True,False] ]
            opts = [ o for o in opts if o is not None ]
            print(m[r][c], end = ' ')
            if len(opts) == 0:
                print('    ', end='')
            else:
                print('{}{:02d}'.format(len(opts), min(opts)), end=' ')
        print()

def solve(m,start, end):
    start = (start,2,False)
    def succ(n):
        cur, ncheat, cheating = n
        if cheating and ncheat == 0:
            cheating = False
        cancheat = ncheat == 2

        cds = rangedirs(cur, Cardinals)
        cds = [c for c in cds if not c.oob(m)]

        if cheating:
            cds = [ (c,ncheat-1,True) for c in cds ]
        else:
            cds = [
                    (c,ncheat,False) if c.of(m) != '#'
                    else ((c,ncheat-1,True) if cancheat
                    else None)
                    for c in cds
                    ]
        return [c for c in cds if c is not None]

    costs = BFS(start, None, succ)
    debug(m, costs)

    path = BFS_path(start, end, succ, costs, lambda n: n[0])
    print(path)
    for p in path:
        print(p)
    print(k)
    return cost

best = bestnocheat(m,S,E)
total = 0
for r in range(len(m)):
    for c in range(len(m[r])):
        if m[r][c] == '#':
            m[r][c] = '.'
            t = bestnocheat(m,S,E)
            m[r][c] = '#'
            if best-t >= 100:
                print(best-t)
                total += 1
printc(total)
