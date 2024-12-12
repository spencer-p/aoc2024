import sys
import re
from itertools import pairwise
from collections import Counter, defaultdict, deque
import subprocess

def dd():
    return defaultdict(lambda: None)

def nums(s):
    return list(map(int, re.findall(r'\d+', s)))

def printc(x):
    s = '{}'.format(x)
    print(s)
    subprocess.run(["xclip", "-i", "-sel", "c"], input=str.encode(s))

def input():
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
