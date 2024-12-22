from util import *

s = inputtxt()
lines = s.split('\n')
nums = list(map(int, lines))

def mixprune(a, b):
    a ^= b
    a = a % 16777216 # this is 2 to the 24
    return a

def secretseq(s, n=2000):
    result = [s%10]
    for i in range(n):
        s = mixprune(s, s*64)
        s = mixprune(s, s//32)
        s = mixprune(s, s*2048)
        result.append(s%10)
    return result

def windows(diffs, seq, total=None):
    if total is None: total=set()
    first = {}
    for i in range(len(diffs)-3):
        chg = tuple(diffs[i:i+4])
        total.add(chg)
        if chg not in first:
            first[chg] = seq[i+4]
    return first

def profit(chg, tables):
    p = 0
    for i, table in enumerate(tables):
        if chg in table:
            p += table[chg]
    return p

chgs = set()
lookup = []
for seed in nums:
    seq = secretseq(seed)
    diffs = [b-a for a,b in pairwise(seq)]
    lookup.append(windows(diffs, seq, total=chgs))

cd = None
best = -10000000000000
for chg in chgs:
    p = profit(chg, lookup)
    if p > best:
        cd = chg
        best = p

print(cd)
printc(best)
