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
    if new_target == round(new_target) and solve(new_target, l[:-1]):
        return True

    return False


total = 0
for eq in equations:
    target, l = eq[0], eq[1:]
    if solve(target, l):
        print(target)
        total += target


# not 16322788747517
printc(total)
