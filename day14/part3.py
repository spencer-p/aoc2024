from dataclasses import dataclass
from util import *
from functools import reduce
import operator

mul = lambda ls: reduce(operator.mul, ls, 1)

@dataclass
class Vec:
    x: int
    y: int

@dataclass
class Robot:
    start: Vec
    vel: Vec

s = inputtxt()
lines = s.split('\n')
robots = []
for line in lines:
    x, y, a, b = nums(line)
    robots.append(Robot(Vec(x,y),Vec(a,b)))


W=101
H=103

def move_bot(r, n=100):
    newx = (r.start.x + r.vel.x*n) % W #101
    newy = (r.start.y + r.vel.y*n) % H #103
    return Robot(Vec(newx, newy), r.vel)

def debug(rs):
    c = defaultdict(lambda: 0)
    for r in rs:
        c[(r.start.x, r.start.y)] += 1

    for y in range(H):
        for x in range(W):
            if c[(x,y)] == 0:
                print('.', end='')
            else:
                print(c[(x,y)], end='')
        print()

def count_quads(rs):
    quads = [0,0,0,0]
    for r in rs:
        if r.start.x < W//2 and r.start.y < H//2:
            quads[0]+=1
        elif r.start.x > W//2 and r.start.y < H//2:
            quads[1]+=1
        elif r.start.x < W//2 and r.start.y > H//2:
            quads[2]+=1
        elif r.start.x > W//2 and r.start.y > H//2:
            quads[3]+=1
    return quads

def danger(rs):
    return mul(count_quads(rs))

# Loop through states and only print those where the danger is at a new low
i = 0
min_danger=danger(robots)
while True:
    robots = list(map(lambda r: move_bot(r, n=1), robots))
    i+=1
    d = danger(robots)
    if d < min_danger:
        debug(robots)
        print(i)
        input()
        min_danger = d
    else:
        print(i)
