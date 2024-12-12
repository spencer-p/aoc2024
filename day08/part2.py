from util import *

s = input()
m = s.split('\n')

def filter_nodes(m):
    nodes = defaultdict(set)
    for r, row in enumerate(m):
        for c, col in enumerate(row):
            if col != '.':
                nodes[col].add((r, c))
    return nodes

def antinodes(nodes, maxr, maxc):
    anti = set()
    for signal, coords in nodes.items():
        for pair in combinations(coords, 2):
            a, b = pair[0], pair[1]
            rdiff = a[0]-b[0]
            cdiff = a[1]-b[1]
            i = 0
            while True:
                a1 = (a[0]+ i*rdiff, a[1]+ i*cdiff)
                if a1[0] >= 0 and a1[0] < maxr and a1[1] >= 0 and a1[1] < maxc:
                    anti.add(a1)
                else:
                    break
                i += 1

            i = 0
            while True:
                a1 = (b[0]- i*rdiff, b[1]- i*cdiff)
                if a1[0] >= 0 and a1[0] < maxr and a1[1] >= 0 and a1[1] < maxc:
                    anti.add(a1)
                else:
                    break
                i += 1
    return anti

def debug(antis, maxr, maxc):
    for r in range(maxr):
        for c in range(maxr):
            if (r,c) in antis:
                print('#', end='')
            else:
                print('.', end='')
        print()

nodes = filter_nodes(m)
antis = antinodes(nodes, len(m), len(m[0]))
debug(antis, len(m), len(m[0]))
printc(len(antis))
