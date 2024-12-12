from util import *

s = input()
m = s.split('\n')

dirs = [ ( 0, 1 ), ( 1, 0 ), ( -1, 0 ), ( 0, -1 ) ]

def cardinals(r, c):
    return [ (r+i, c+j) for (i, j) in dirs]

def find_region(m, r, c, seen=None):
    if seen is None: seen = set()

    result = set()

    plant = m[r][c]
    result.add((r,c))
    seen.add((r,c))

    for r, c in cardinals(r,c):
        if oob(m,r,c) or (r,c) in seen:
            continue
        if m[r][c] != plant:
            continue
        seen.add((r,c))
        result.add((r,c))
        result |= find_region(m,r,c,seen)
    
    return result

def all_regions(m):
    accounted = set()
    regions = []
    for r in range(len(m)):
        for c in range(len(m[r])):
            if (r,c) in accounted:
                continue
            region = find_region(m, r, c)
            accounted |= region
            regions.append(region)
    return regions


def score_region(region):
    area = len(region)
    perimeter = 0
    for cur in region:
        for r, c in cardinals(*cur):
            if (r,c) not in region:
                perimeter += 1
    return perimeter*area

printc(sum(list(map(score_region, all_regions(m)))))
