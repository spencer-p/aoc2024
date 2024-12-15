from util import *

s = inputtxt()
fh, sh = s.split('\n\n')

m = [list(x) for x in fh.split('\n')]
moves = ''.join(sh.split('\n'))

def todir(move):
    translate = {
            '>': 1,
            'v': 0,
            '^': 2,
            '<': 3,
            }
    return Cardinals[translate[move]]

def find_bot(m):
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == '@':
                return Vec(r,c)

def move_bot(m, move):
    bot = find_bot(m)
    d = todir(move)
    next = bot + d
    if m[next.r][next.c] == '.':
        m[next.r][next.c] = '@'
        m[bot.r][bot.c] = '.'
        return
    elif m[next.r][next.c] == '#':
        return

    firstbox = next
    next = next + d
    while m[next.r][next.c] == 'O':
        next = next + d

    if m[next.r][next.c] == '.':
        m[next.r][next.c] = 'O'
        m[firstbox.r][firstbox.c] = '@'
        m[bot.r][bot.c] = '.'
        return
    # other case is #, nothing happens

def debug(m):
    for r in range(len(m)):
        print(''.join(m[r]))

def score(m):
    total = 0
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == 'O':
                total += 100*r + c
    return total

for move in moves:
    move_bot(m, move) 

printc(score(m))
