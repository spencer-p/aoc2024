from itertools import pairwise

f = open("input.txt", "r")
lines = f.read().strip().split()
m = [ [c for c in lines[i]] for i in range(len(lines)) ]

def read(x, y):
    if x < 0 or y < 0:
        return '\0'
    try:
        return m[x][y]
    except:
        return '\0'

def solve():
    total = 0
    diffs = [
            [[0,1], [0,2], [0,3]], # east
            [[1,0], [2,0], [3,0]], # south
            [[0,-1], [0,-2], [0,-3]], # north
            [[-1,0], [-2,0], [-3,0]], # west
            [[-1,-1], [-2,-2], [-3,-3]], # nw
            [[-1,1], [-2,2], [-3,3]], # sw
            [[1,-1], [2,-2],[3,-3]], # ne
            [[1,1],[2,2],[3,3]], # se
            ]
    for x in range(len(m)):
        for y in range(len(m[x])):
            if read(x, y) != 'X':
                continue
            for diff in diffs:
                t = ''.join([ read(x+c[0], y+c[1]) for c in diff ])
                if t == "MAS":
                    total += 1
    return total

#m = [['X', 'M', 'A', 'S']]
print(solve())
