import sys
import re
from itertools import pairwise, combinations
from collections import Counter, defaultdict, deque
import subprocess
from functools import cache, reduce
import operator
from dataclasses import dataclass
from heapq import heappush, heappop

sys.setrecursionlimit(1000000)

# sim. to sum, but for mult.
mul = lambda ls: reduce(operator.mul, ls, 1)

def dd():
    return defaultdict(lambda: None)

def nums(s):
    return list(map(int, re.findall(r'\d+', s)))

def printc(x):
    s = '{}'.format(x)
    print(s)
    subprocess.run(["xclip", "-i", "-sel", "c"], input=str.encode(s))

def inputtxt():
    fname = "input.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    f = open(fname, "r")
    return f.read().strip()

def ctrue(l):
    total = 0
    for i in l:
        if i:
            total += 1
    return total

def bisect(f, l, h):
    while l <= h:
        m = (l+h)//2
        t = f(m)
        if t:
            l = m + 1
        else:
            h = m - 1
    return l

@dataclass(eq=True, frozen=True, order=True)
class Vec:
    r: int
    c: int

    # x and y alias to r and c
    @property
    def x(self):
        return self.r
    @property
    def y(self):
        return self.c

    def __add__(self, other):
        return Vec(self.r+other.r, self.c+other.c)

    def __sub__(self, other):
        return Vec(self.r-other.r, self.c-other.c)

    def __mul__(self, n):
        return Vec(self.r*n, self.c*n)

    def of(self, m):
        return m[self.r][self.c]

    def oob(self, m):
        return not (self.r >= 0 and
                    self.c >= 0 and
                    self.r < len(m) and
                    self.c < len(m[self.r]))

    def piecelen(self):
        return abs(self.r)+abs(self.c)

# Cardinal directions as up/down left/right and NSEW.
East  = Right = Vec(0,1)
South = Down  = Vec(1,0)
North = Up    = Vec(-1,0)
West  = Left  = Vec(0,-1)
Cardinals = [Right, Down, Left, Up]

# The four intercardinal directions.
Southeast = South+East
Southwest = South+West
Northwest = North+West
Northeast = North+East
Intercardinals = [Southeast, Southwest, Northwest, Northeast]

# The full eight point compass.
Compass8 = [East,  Southeast,
            South, Southwest,
            West,  Northwest,
            North, Northeast]

def rangedirs(v: Vec, dirs: list[Vec]):
    return [v+d for d in dirs]

# BFS finds the cost to get from start to end (or all nodes if end is None) and
# returns a dictionary of coordinates to the cost to get there.
# succ should return the "successors" of a given node, or an empty list if none.
def BFS(start, end, succ) -> dict:
    seen = set()
    costs = defaultdict(lambda: None)
    costs[start] = 0
    q = deque([start])
    while len(q) > 0:
        cur = q.pop()
        if cur in seen: continue
        seen.add(cur)
        if end is not None and cur == end:
            return costs
        for t in succ(cur):
            if t in costs:
                costs[t] = min(costs[t], 1+costs[cur])
            else:
                costs[t] = 1 + costs[cur]
            q.appendleft(t)
    return costs

# BFS_path returns a path from the result of BFS.
def BFS_path(start, end, succ, costs, ntoend=lambda x: x):
    def newsucc(n):
        candidates = succ(n)
        cost = costs[n]
        candidates = [ c for c in candidates if costs[c] == cost+1 ]
        return candidates
    return DFS(start, end, newsucc, ntoend=ntoend)

# Dijkstra is like BFS with the addition of the cost oracle.
def Dijkstra(start, end, succ, cost) -> dict:
    seen = set()
    costs = {start: 0}
    q = [(0,start)]
    while len(q) > 0:
        _, cur = heappop(q)
        if cur in seen: continue
        seen.add(cur)
        if end is not None and cur == end:
            return costs
        for t in succ(cur):
            edge = cost(cur, t)
            if t in costs:
                costs[t] = min(costs[t], costs[cur] + edge)
            else:
                costs[t] = costs[cur] + edge
            heappush(q, (costs[t], t))
    return costs

# DFS finds a path from start to end.
def DFS(start, end, succ, seen=None, ntoend=lambda x: x):
    if seen is None: seen = set()
    if ntoend(start) == end: return [end]
    seen.add(start)
    for t in succ(start):
        result = DFS(t, end, succ, seen=seen)
        if result is not None:
            return [start]+result
    return None

# DFS_all finds all possible paths from start to end.
def DFS_all(start, end, succ, seen=None):
    if seen is None: seen = set()
    if start[0] == end: return [[end]]
    seen.add(start)
    paths = []
    for t in succ(start):
        results = DFS_all(t, end, succ, seen=seen.copy())
        if len(results) > 0:
            paths.extend([ [start] + r for r in results ])
    return paths

class DiGraph:
    def __init__(self):
        self.g = defaultdict(set)

    def add(self, a, b):
        self.g[a].add(b)

    def get(self, a):
        return self.g[a]

    def keys(self):
        return self.g.keys()

    def reverse(self):
        new = Graph()
        for key in self.keys():
            for n in self.get(key):
                new.add(n, key)
        return new

    def __str__(self):
        return '{}'.format(self.g)

    def cycle(self):
        totalseen = set()
        for key in list(self.keys()):
            if key in totalseen:
                continue

            seen = set([key])
            q = deque([key])
            while len(q) > 0:
                cur = q.pop()
                for n in self.get(cur):
                    if n in seen:
                        return True
                    seen.add(n)
                    q.appendleft(n)

            totalseen = totalseen.union(seen)

        return False

    def reach(self, a, b):
        seen = set()
        q = deque([a])
        while len(q) > 0:
            cur = q.pop()
            for n in self.get(cur):
                if n is b:
                    return True
                q.appendleft(n)

        return False
