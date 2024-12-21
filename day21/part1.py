from util import *

nkeypad = [
        ['7','8','9'],
        ['4','5','6'],
        ['1','2','3'],
        [None,'0','A'],
        ]
rkeypad = [
        [None, '^', 'A'],
        ['<','v','>'],
        ]


s = inputtxt()
codes = s.split('\n')

def flatten(xss):
    return [x for xs in xss for x in xs]

def dtoa(d):
    if d == Left: return '<'
    elif d == Right: return '>'
    elif d == Up: return '^'
    elif d == Down: return 'v'

@cache
def keytov(key, robot=False):
    if robot:
        pad = rkeypad
    else:
        pad = nkeypad
    for r in range(len(pad)):
        for c in range(len(pad[r])):
            if pad[r][c] == key:
                return Vec(r,c)

def manhattanpaths(start, end, pad) -> dict:
    seen = set()
    costs = defaultdict(lambda: None)
    costs[''] = 0
    q = deque([('', start)])
    mincost = None
    paths = []
    while len(q) > 0:
        path, v = q.pop()
        if v == end:
            paths.append(path)
            if mincost is None: mincost = costs[path]
            continue
        if mincost is not None and costs[path] > mincost:
            break

        seen.add(v)
        for d in Cardinals:
            t = v+d
            if t.oob(pad) or t.of(pad) is None: continue
            if t in seen: continue
            tpath = path + dtoa(d)
            costs[tpath] = 1 + costs[path]
            q.appendleft((tpath, t))
    return paths

@cache
def findsequence(wantseq, start=None, robot=False):
    if robot:
        pad = rkeypad
        if start is None: start = Vec(0,2)
    else:
        pad = nkeypad
        if start is None: start = Vec(3,2)

    n = keytov(wantseq[0], robot=robot)
    paths = manhattanpaths(start, n, pad)
    if len(wantseq) == 1:
        return [p1+'A' for p1 in paths]
    recpaths = findsequence(wantseq[1:], n, robot=robot)
    return [ p1+'A'+p2 for p1 in paths for p2 in recpaths]

def solve(startcode):
    l1 = findsequence(startcode, robot=False)
    l2 = flatten([findsequence(code, robot=True) for code in l1])
    l3 = flatten([findsequence(code, robot=True) for code in l2])
    sol = min(map(len, l3))
    return sol

total = 0
for code in codes:
    l = solve(code)
    num = nums(code)[0]
    total += l*num
printc(total)
