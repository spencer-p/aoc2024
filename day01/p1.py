# 2024 advent of code day 1

def readinput(fname):
    left, right = [], []
    with open(fname, "r") as f:
        for line in f:
            l, r = map(int, line.split())
            left.append(l)
            right.append(r)
    return left, right


def testinput():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    return left, right


def solve1(left, right):
    left = sorted(left)
    right = sorted(right)
    total = 0
    for l, r in zip(left, right):
        total += abs(r-l)
    return total


def solve2(left, right):
    left = sorted(left)
    right = sorted(right)
    table = {}
    for r in right:
        if r not in table:
            table[r] = 0
        table[r] += 1

    score = 0
    for l in left:
        if l in table:
            score += table[l] * l
    return score

#left, right = testinput()
left, right = readinput("input1.txt")
print(solve2(left, right))
