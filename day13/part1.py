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
        "x": x,
        "y": y,
        })

def solvep(p):
    target = (p["x"], p["y"])
    q = deque([target])
    costs = defaultdict(lambda: 0)
    while len(q) > 0:
        cur = q.pop()

        if cur[0] < 0 or cur[1] < 0:
            continue

        t = (cur[0]-p["ax"], cur[1]-p["ay"])
        cost = costs[cur]+3 # A costs 3.

        if t == (0,0):
            return cost

        if costs[t] == 0 or cost < costs[t]:
            costs[t] = cost
            q.appendleft(t)

        t = (cur[0]-p["bx"], cur[1]-p["by"])
        cost = costs[cur]+1 # B costs 1.

        if t == (0,0):
            return cost

        if costs[t] == 0 or cost < costs[t]:
            costs[t] = cost
            q.appendleft(t)

    return 0

printc(sum([solvep(i) for i in problems]))
