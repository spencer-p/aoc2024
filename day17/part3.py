from util import *

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

    match op:
        case 0: s.A = s.A//(2**combo(s, imm))
        case 1: s.B = s.B^imm
        case 2: s.B = combo(s,imm)%8
        case 3:
            if s.A != 0:
                s.ip = imm
                return s, output
        case 4: s.B = s.B^s.C
        case 5: output = combo(s,imm)%8 
        case 6: s.B = s.A//(2**combo(s,imm))
        case 7: s.C = s.A//(2**combo(s,imm))

    s.ip += 2
    return s, output 


def run(state, program):
    out = []
    while state.ip < len(program):
        state, x = next(state, program)
        if x is not None:
            out.append(x)
    return state, out


def search(program, a=0, i=None):
    if i is None: i = 0
    N = len(program)
    if i == N: return a
    want = program[N-i-1:]
    for t in range(8):
        aprime = (a << 3) + t
        _, result = run(State(aprime,0,0,0), program)
        if result == want:
            aprime = search(program, aprime, i+1)
            if aprime is not None:
                return aprime
    return None


# 164279024971453 is desired result 
result = search(program)
if result is None:
    print("no solution")
    quit()
printc(result)
_, out = run(State(result,0,0,0), program)
print(','.join(map(str, program)))
print(','.join(map(str, out)))
