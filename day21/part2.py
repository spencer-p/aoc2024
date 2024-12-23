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

def score(seq):
    # returns repetitiveness
    score = 0
    for a,b in pairwise(seq):
        if a==b:
            score += 1
    return score

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

@cache
def minseq(wantseq, depth):
    if len(wantseq) == 0: return 0
    if wantseq == 'A': return 1
    if depth==0: return len(wantseq)
    seqs = findsequence(wantseq, robot=True)
    sol = None
    for seq in seqs:
        total = 0
        parts = seq.split('A')
        for part in parts:
            total += minseq(part+'A', depth-1)
        if sol is None or total < sol:
            sol = total
    return sol-1

def solve1(code):
    l1 = findsequence(code, robot=False)
    return min([minseq(code,25) for code in l1])

def solve2(code):
    l = solve1(code)
    num = nums(code)[0]
    return l*num

# 168850012939159 too low
# 232389969568832 ? yes
# 578099211876318 not it
# 633368662333590 too high
printc(sum([ solve2(code) for code in codes ]))
