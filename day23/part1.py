from util import *

s = inputtxt()
lines = s.split('\n')
graph = defaultdict(lambda: set())
allnodes = set()
for line in lines:
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)
    allnodes.add(a)
    allnodes.add(b)

# the problem is to identify connected components of 3
def DFS(start, end, succ, seen=None, depth=0):
    if seen is None: seen = set()
    if depth == 3 and start == end: return [[]]
    if depth == 3: return []
    seen.add(start)
    paths = []
    for t in succ(start):
        if t != end and t in seen: continue
        results = DFS(t, end, succ, seen=seen.copy(), depth=depth+1)
        if len(results) > 0:
            paths.extend([ [start] + r for r in results ])
    return paths

def succ(n):
    return graph[n]

allgroups = set()
for n in allnodes:
    if not n.startswith('t'): continue
    paths = DFS(n, n, succ, set())
    for p in paths: p.sort()
    groups = set([ ','.join(p) for p in paths ])
    allgroups |= groups
printc(len(allgroups))
