from util import *

s = input()
problems_raw = s.split('\n\n')
problems = []
for p in problems_raw:
    ax, ay, bx, by, x, y = nums(p)
    problems.append({
        "ax": ax,
        "ay": ay,
        "bx": bx,
        "by": by,
        "x": x+10000000000000,
        "y": y+10000000000000,
        })

def solvep(p):
    X, Y = p["x"], p["y"]
    Ax, Ay = p["ax"], p["ay"]
    Bx, By = p["bx"], p["by"]

    b = (Ay*X - Ax*Y)/(Ay*Bx - Ax*By)
    a = (Y-By*b)/Ay

    score = 3*a+b
    return int(score) if score.is_integer() else 0
     

# not 77426298536700
# not 78625675290351
#     103729094227877 ? yes
printc(sum([solvep(i) for i in problems]))
