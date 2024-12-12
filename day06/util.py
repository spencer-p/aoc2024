import sys
import re
from itertools import pairwise
from collections import Counter, defaultdict, deque
import subprocess

sys.setrecursionlimit(1000000)

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

    def remove(self, a, b):
        self.g[a].remove(b)

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
        seen = set()
        for key in list(self.keys()):
            if key in seen:
                continue
            t = self.dfs(key, key, seen=seen)
            if t is not None:
                print("cycle:", t)
                return True

        return False

    def dfs(self, start, target, seen=None):
        if seen is None: seen = set()
        seen.add(start)
        for i in self.get(start):
            if i is target:
                return [start, target]
            if i in seen:
                continue
            t = self.dfs(i, target, seen=seen)
            if t is not None:
                return [start]+t
        return None
