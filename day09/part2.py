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
    r0, r1 = last_filled(b, len(b)-1)
    while r0 is not None:
        #print("last full at", r0, r1)
        sfull = r1-r0
        l0, l1 = None, 0
        bare_min = b.index('.')
        while True:
            l0, l1 = first_free(b, max(l1, bare_min))
            if l0 is None or l1 > r0:
                #print("no fit for", b[r0])
                break
            sempty = l1-l0
            if sfull > sempty:
                continue
            # found a fit
            #print(sfull, "of", b[r0], "will fit at", l0)
            for i in range(sfull):
                b[l0+i], b[r0+i] = b[r0+i], b[l0+i] 
            break
            
        #print(''.join(map(str, b)))
        r0, r1 = last_filled(b, r0-1)
    return b

def first_free(b, i):
    start = i
    while True:
        if start >= len(b):
            return None, None
        if b[start] == '.':
            break
        start += 1

    end = start+1
    while True:
        if end >= len(b):
            return None, None
        if b[end] != '.':
            return start, end
            break
        end += 1


def last_filled(b, i):
    t = None
    end = i
    while True:
        if end < 0:
            return None, None
        if b[end] != '.':
            t = b[end]
            break
        end -= 1

    start = end - 1
    while True:
        if start < 0:
            return None, None
        if b[start] != t:
            return start+1, end+1
        start -= 1

blocks = to_blocks(s) 
defragged = defrag(blocks)
printc(sum([ i * v if v != '.' else 0 for i, v in enumerate(defragged) ]))
# 6351802065320 is too high
# 6351801932670 is correct
# mistake : l1 must be less than or equal to r0. because l1 is actually the
# first *not free* spot.
