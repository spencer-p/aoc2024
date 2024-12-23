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

# largest connected component where all the nodes are connected to each other
def DFS(start, end, succ, seen=None):
    if seen is None: seen = set()
    if start == end: return [end]
    seen.add(start)
    for t in succ(start):
        if t in seen: continue

        # constraint: to visit t, succ(t) must contain all of seen.
        if len(seen - set(succ(t))) > 0: continue

        result = DFS(t, end, succ, seen=seen)
        if result is not None:
            return [start]+result
    return None

def succ(n):
    return graph[n]

seen = set()
biggest = 0
biggestgroup = None
for n in allnodes:
    if n in seen: continue
    group = set()
    DFS(n, None, succ, group)
    seen |= group
    if len(group) > biggest:
        biggest = len(group)
        biggestgroup = group


g = list(biggestgroup)
g.sort()
printc(','.join(g))
