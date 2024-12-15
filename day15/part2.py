from util import *

s = inputtxt()
fh, sh = s.split('\n\n')

m = [list(x) for x in fh.split('\n')]
moves = ''.join(sh.split('\n'))

Right = Cardinals[1]
Down = Cardinals[0]
Up = Cardinals[2]
Left = Cardinals[3]

def todir(move):
    translate = {
            '>': Right,
            'v': Down,
            '^': Up,
            '<': Left,
            }
    return translate[move]

def find_bot(m):
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == '@':
                return Vec(r,c)

def find_affected(m, d, start):
    affected = set()
    l = start
    hit = m[start.r][start.c] 
    if hit == '[':
        affected.add(start)
        affected.add(start+Vec(0,1))
    elif hit == ']':
        affected.add(start)
        l = start+Vec(0,-1)
        affected.add(l)
    elif hit == '.':
        return affected, True
    elif hit == '#':
        return None, False

    if d == Left:
        tocheck = [ l + Left]
    elif d == Right:
        tocheck = [ l + Right + Right ]
    else:
        tocheck = [ l + d, l + d + Right ]

    for t in tocheck:
        next_aff, ok = find_affected(m, d, t)
        if not ok:
            return None, False
        affected |= next_aff

    return affected, True


def move_bot(m, move):
    bot = find_bot(m)
    d = todir(move)
    next = bot + d
    if m[next.r][next.c] == '.':
        m[next.r][next.c] = '@'
        m[bot.r][bot.c] = '.'
        return m
    elif m[next.r][next.c] == '#':
        return m

    affected, can_move = find_affected(m, d, next)
    if not can_move:
        return m
    
    # Now every coord in affected must advance by d.
    newm = [ r.copy() for r in m ]
    for p in affected:
        newp = p+d
        newm[newp.r][newp.c] = m[p.r][p.c]
        if (p - d) not in affected:
            newm[p.r][p.c] = '.'

    newm[next.r][next.c] = '@'
    newm[bot.r][bot.c] = '.'
    return newm


def debug(m):
    for r in range(len(m)):
        print(''.join(m[r]))

def score(m):
    total = 0
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == '[':
                total += 100*r + c
    return total

for i, move in enumerate(moves):
    m = move_bot(m, move) 

# 1557150 is too high - I had forgotten to remove a debug break!
# 1550677 is correct.
printc(score(m))
