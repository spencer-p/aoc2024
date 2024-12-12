from util import *

s = input()
m = s.split()

startr, startc = None, None
for r, row in enumerate(m):
    if '^' in row:
        startr = r
        for c, t in enumerate(row):
            if t == '^':
                startc = c
                break
        break


dirs = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1],
        ]
di = 0

def splice(s, x, c):
    return s[:x]+c+s[x+1:]

def debug(rt, ct):
    global m
    for r, row in enumerate(m):
        if r == rt:
            print(splice(row, ct, 'O'))
        else:
            print(row)

def ingrid(r, c):
    return r >= 0 and r < len(m) and c >= 0 and c < len(m[0])

print("=======================================================")

r, c = startr, startc
p = set()
obs = set()
while True:
    p.add((r,c))

    if True:
        # try setting a rock in front of guard
        ro, co = r+dirs[di][0], c+dirs[di][1]
        # if that rock is in the grid, and it's not already blocked, and not the
        # start position
        if ingrid(ro, co) and m[ro][co] != '#' and (ro,co) != (startr,startc):
            # new coords and direction
            r2, c2, d2 = r, c, di
            o = set() # track where we've been
            while True:
                # if we've been to this spot before, we have a loop
                if (r2,c2,d2) in o:
                    #print("place at {} returned to {}".format((ro,co), (r2,c2)))
                    #debug(ro,co)
                    #print()
                    obs.add((ro,co))
                    break
                # mark that we've been to this spot
                o.add((r2,c2,d2))

                # compute where we would go next with this new config
                rn, cn = r2+dirs[d2][0], c2+dirs[d2][1]
                # if we walk off the grid, end search.
                if not ingrid(rn, cn):
                    break
                # if the next spot is blocked (or the rock), turn
                t = m[rn][cn]
                if t == '#' or (rn, cn) == (ro, co):
                    d2 = (d2+1)%4
                # otherwise step into it
                else:
                    r2, c2 = rn, cn


    rn, cn = r+dirs[di][0], c+dirs[di][1]
    if not ingrid(rn, cn):
        break
    t = m[rn][cn]
    if t == '#':
        di = (di+1)%4
    else:
        r, c = rn, cn



printc(len(p))
printc(len(obs)) # 1606 is too low, 1965 and 2013 wrong
