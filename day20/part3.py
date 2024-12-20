from util import *

s = inputtxt()
m = [ [c for  c in line] for line in s.split('\n')]

for r in range(len(m)):
    for c in range(len(m[r])):
        match m[r][c]:
            case 'S': S = Vec(r,c)
            case 'E': E = Vec(r,c)

def cheat2(p):
    return rangedirs(p, map(lambda d: d*2, Cardinals))

def cheat20(p):
    return [ p + Vec(r,c) for r in range(-20,21) for c in range(-20, 21) if
            abs(r)+abs(c) <= 20 ]

def succ(n):
    return [c for c in rangedirs(n, Cardinals) if not c.oob(m) and c.of(m)
            != '#']
costs =  BFS(S,E,succ)
best = costs[E]
path = BFS_path(S,E,succ,costs)

# The gist of this solution is from reddit. I saw folks iterate over the
# combinations of points on the main path.
# It can run even faster if we only consider the points that can be teleported
# to. This does about 13s on my machine.
# On a high level, my DFS approach does the same thing (especially since it
# computes the cost directly when it hits the main path). But it's much slower,
# I figure because it does way more bookkeeping.

part1 = part2 = 0
for p1 in path:
    for p2 in cheat2(p1):
        if p2 not in costs: continue
        dist = (p1-p2).piecelen()
        save = costs[p2]-costs[p1]-dist
        if save >= 100: part1 += 1

    for p2 in cheat20(p1):
        if p2 not in costs: continue
        dist = (p1-p2).piecelen()
        save = costs[p2]-costs[p1]-dist
        if save >= 100: part2 += 1

print(part1)
print(part2)
