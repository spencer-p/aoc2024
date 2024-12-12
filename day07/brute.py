from util import *

s = input()
lines = s.split('\n')

equations = list(map(nums, lines))

def solve3(target, l):
    for n in range(2**len(l)):
        t = l[0]
        for i, x in enumerate(l):
            if i == 0: continue
            add = 0 == (n>>i) & 1
            if add:
                t += x
            else:
                t *= x
        if t == target:
            return True

    return False


total = 0
for eq in equations:
    target, l = eq[0], eq[1:]
    if solve3(target, l):
        total += target


# not 16322788747517
printc(total)
