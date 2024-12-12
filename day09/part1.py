from util import *

s = input()

def to_blocks(m):
    m = list(map(int, list(m)))
    b = [None] * sum(m)
    i = 0
    bid = 0
    d = True
    for n in m:
        # set the b[i:n] to bid
        target = bid if d else '.'
        for j in range(i, n+i):
            b[j] = target
        i += n
        bid += 1 if d else 0
        d = not d
    return b

def defrag(b):
    l, r = first(b, 0, '.'), lastnot(b, len(b)-1, '.')
    while l is not None and r is not None and l < r:
        b[l], b[r] = b[r], b[l]
        l, r = first(b, l, '.'), lastnot(b, r, '.')
    return b

def first(b, i, target):
    while True:
        if i >= len(b):
            return None
        if b[i] == target:
            return i
        i += 1

def lastnot(b, i, target):
    while True:
        if i < 0:
            return None
        if b[i] != target:
            return i
        i -= 1


blocks = to_blocks(s) 
defragged = defrag(blocks)
printc(sum([ i * v if v != '.' else 0 for i, v in enumerate(defragged) ]))
