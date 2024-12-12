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
            print(pair)
            a, b = pair[0], pair[1]
            rdiff = a[0]-b[0]
            cdiff = a[1]-b[1]
            a1 = (a[0]+rdiff, a[1]+cdiff)
            a2 = (b[0]-rdiff, b[1]-cdiff)
            if a1[0] >= 0 and a1[0] < maxr and a1[1] >= 0 and a1[1] < maxc:
                anti.add(a1)
            if a2[0] >= 0 and a2[0] < maxr and a2[1] >= 0 and a2[1] < maxc:
                anti.add(a2)
            print(a1, a2)
    return anti

nodes = filter_nodes(m)
printc(nodes)
antis = antinodes(nodes, len(m), len(m[0]))
printc(antis)
printc(len(antis))
