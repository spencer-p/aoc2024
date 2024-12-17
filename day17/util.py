import sys
import re
from itertools import pairwise
from collections import Counter, defaultdict, deque
import subprocess
from functools import cache, reduce
import operator
from dataclasses import dataclass

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

@dataclass(eq=True, frozen=True)
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

    def oob(self, m):
        return self.r >= 0 and self.c >= 0 and self.r < len(m) and self.c < len(m[x])

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
