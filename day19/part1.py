from util import *

s = inputtxt()
parts = s.split('\n\n')
available = set(parts[0].split(', '))
designs = parts[1].split('\n')

@cache
def search(design):
    global available
    if len(design) == 0:
        return 1
    total = 0
    for a in available:
        if design.startswith(a):
            total += search(design.removeprefix(a))
    return total

r = [ search(d) for d in designs ]
printc(sum([ 1 if way > 0 else 0 for way in r]))
printc(sum(r))
