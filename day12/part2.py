from util import *

s = input()
m = s.split('\n')

dirs = [ ( 0, 1 ), ( 1, 0 ), ( -1, 0 ), ( 0, -1 ) ]

northsouth = [ ( 1, 0 ), ( -1, 0 ) ]
eastwest = [ ( 0, 1 ), ( 0, -1 ) ]

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
    sidecount = 0
    sides = dd()
    region = list(region)
    region.sort()
    for cur in region:
        for d in northsouth:
            r, c = cur[0]+d[0], cur[1]+d[1]
            if (r,c) not in region:
                # note r is fixed when going n/s
                # this coord is on a side
                # is it a side we know about already?
                right = (cur[0], cur[1]+1)
                if (right,d) in sides:
                    sides[(cur,d)] = sides[(right,d)]
                    continue
                left = (cur[0], cur[1]-1)
                if (left,d) in sides:
                    sides[(cur,d)] = sides[(left,d)]
                    continue
                # not adjacent to an existing side
                # create a new side index and add it.
                #print(cur, "going", d, "is new")
                sidecount += 1
                sides[(cur,d)] = sidecount

        for d in eastwest:
            r, c = cur[0]+d[0], cur[1]+d[1]
            if (r,c) not in region:
                down = (cur[0]+1, cur[1])
                if (down,d) in sides:
                    sides[(cur,d)] = sides[(down,d)]
                    continue
                up = (cur[0]-1, cur[1])
                if (up,d) in sides:
                    sides[(cur,d)] = sides[(up,d)]
                    continue
                #print(cur, "going", d, "is new")
                sidecount += 1
                sides[(cur,d)] = sidecount
    #print()
    return area*sidecount

printc(sum(list(map(score_region, all_regions(m)))))
