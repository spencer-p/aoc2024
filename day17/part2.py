from util import *
from math import trunc

s = inputtxt()
lines = s.split('\n')
A = nums(lines[0])[0]
B = nums(lines[1])[0]
C = nums(lines[2])[0]

program = nums(lines[4])

@dataclass
class State:
    A: int
    B: int
    C: int
    ip: int

def combo(s, x):
    if x <= 3: return x
    elif x == 4: return s.A
    elif x == 5: return s.B
    elif x == 6: return s.C
    else: None

def next(s, program):
    op, imm = program[s.ip], program[s.ip+1]
    output = None

    if op == 0: # adv
        s.A = trunc(s.A/(2**combo(s, imm)))
    elif op == 1: # bxl
        s.B = s.B^imm
    elif op == 2: # bst
        s.B = combo(s,imm)%8
    elif op == 3: # jnz
        if s.A != 0:
            s.ip = imm
            return s, output
    elif op == 4: # bxc
        s.B = s.B^s.C
    elif op == 5: # out
        output = combo(s,imm)%8 
    elif op == 6: # bdv
        s.B = trunc(s.A/(2**combo(s,imm)))
    elif op == 7: # cdv
        s.C = trunc(s.A/(2**combo(s,imm)))

    s.ip += 2
    return s, output 


def run(state, program):
    out = []
    while state.ip < len(program):
        state, x = next(state, program)
        if x is not None:
            out.append(x)
    return state, out


def search(program):
    out = []
    a = 0
    rprog = program.copy()
    rprog.reverse()
    N = len(program)
    for i in range(N):
        want = program[N-i-1:]
        t = 0
        while True:
            aprime = (a << 3) + t
            _, result = run(State(aprime,0,0,0), program)
            if result == want:
                a = aprime
                break
            t += 1
    return a


# 175753844603718 too high
result = search(program)
printc(result)
_, out = run(State(result,0,0,0), program)
print(','.join(map(str, program)))
print(','.join(map(str, out)))
