from util import *

s = input()
lines = s.split('\n')

equations = list(map(nums, lines))

def solve(target, l):
    if len(l) == 1:
        return target == l[0]
    
    last = l[-1]

    # plus case.
    new_target = target-last
    if solve(new_target, l[:-1]):
        return True

    # mult case.
    new_target = target/last
    if solve(new_target, l[:-1]):
        return True

    
    # For the merging case, there's no sense using fractions
    # Terminate fractions and drop to int if needed.
    if target != round(target):
        return False
    target = int(target)

    # merge case.
    # solve for target = new_target+last
    # or new_target = target with stripped suffix last
    lasts = str(last)
    targets = str(target)
    if targets.endswith(lasts):
        new_target = int(targets.removesuffix(lasts))
        if solve(new_target, l[:-1]):
            return True

    return False

def sovle2(target, l):
    table = {
            '+': [None]*len(l),
            '*': [None]*len(l),
            }

def solve3(target, l):
    for n in range(3**len(l)):
        t = l[0]
        for i, x in enumerate(l):
            if i == 0: continue
            sel = extract(n, i)
            if sel == 0:
                t += x
            elif sel == 1:
                t *= x
            else:
                t = int('{}{}'.format(t, x))
        if t == target:
            return True

    return False


def extract(x, n):
    return (x // 3**n) % 3
    for i in range(n):
        x //= 3
    return x%3


total = 0
for eq in equations:
    target, l = eq[0], eq[1:]
    if solve(target, l):
        total += target


printc(total)
