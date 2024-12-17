from util import *
from math import trunc

s = inputtxt()
lines = s.split('\n')
A = nums(lines[0])[0]
B = nums(lines[1])[0]
C = nums(lines[2])[0]

program = nums(lines[4])
print(program)

def combo(x):
    global A, B, C
    if x <= 3: return x
    elif x == 4: return A
    elif x == 5: return B
    elif x == 6: return C
    else: None

out = []
i = 0
while i < len(program):
    op, imm = program[i], program[i+1]

    if op == 0: # adv
        A = trunc(A/(2**combo(imm)))
    elif op == 1: # bxl
        B = B^imm
    elif op == 2: # bst
        B = combo(imm)%8
    elif op == 3: # jnz
        if A != 0:
            i = imm
            continue
    elif op == 4: # bxc
        B = B^C
    elif op == 5: # out
        out.append(combo(imm)%8)
    elif op == 6: # bdv
        B = trunc(A/(2**combo(imm)))
    elif op == 7: # cdv
        C = trunc(A/(2**combo(imm)))

    i+=2

printc(','.join(map(str, out)))
