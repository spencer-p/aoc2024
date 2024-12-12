# aoc 2024 day 2
from itertools import pairwise


def readinput(fname):
    reports = []
    with open(fname, "r") as f:
        for line in f:
            report = list(map(int, line.split()))
            reports.append(report)

    return reports


def testinput():
    return [[ 7, 6, 4, 2, 1 ],
            [ 1, 2, 7, 8, 9 ],
            [ 9, 7, 6, 2, 1 ],
            [ 1, 3, 2, 4, 5 ],
            [ 8, 6, 4, 4, 1 ],
            [ 1, 3, 6, 7, 9 ]]


def solve1(reports):
    unsafe = 0
    for report in reports:
        increasing = None
        for pair in pairwise(report):
            diff = pair[1] - pair[0]
            if increasing is None:
                increasing = True if diff > 0 else False

            if diff < 0 and increasing:
                unsafe += 1
                break
            if diff > 0 and not increasing:
                unsafe += 1
                break

            diff = abs(diff)
            if diff < 1 or diff > 3:
                unsafe += 1
                break

    return len(reports) - unsafe


def solve2(reports):
    unsafe = 0
    for report in reports:
        if not verify_report(report, allow_skip=True):
            unsafe += 1

    return len(reports) - unsafe


# While I tried to implement a backtracking solution, it was too buggy and I
# resorted to brute force.
def verify_report(report, allow_skip=False):
    valid, _ = verify_report_r(report, allow_skip=False)
    if valid:
        return True
    if allow_skip:
        for i in range(len(report)):
            subset = report.copy()
            del subset[i]
            valid, _ = verify_report_r(subset, allow_skip=False)
            if valid:
                return True
    return False

def verify_report_r(report, allow_skip=False) -> (bool, bool):
    # Base case - one or zero numbers is always valid.
    if len(report) < 2:
        return True, None
    if len(report) == 2 and allow_skip:
        # If there's two and we can drop one, again it's the vacuous case.
        return True, None

    # Compute the diff of the first two numbers
    diff = report[1] - report[0]

    # Check the rest.
    rest_valid, increasing = verify_report_r(report[1:], allow_skip=allow_skip)
    if not rest_valid:
        if not allow_skip:
            return False, None
        else:
            # Attempt to recover by dropping element 1.
            # Note dropping 0 cannot recover.
            return verify_report_r([report[0]]+report[2:], allow_skip=False)

    # Figure out if we should be increasing or not.
    if increasing is None:
        increasing = True if diff > 0 else False

    # Check if we broke the monotonic rule.
    nonmono = (diff < 0 and increasing) or (diff > 0 and not increasing)
    if nonmono:
        return False, None

    # Check if the diff is too large.
    diff = abs(diff)
    if diff < 1 or diff > 3:
        return False, None

    return True, increasing


reports = testinput()
print(reports[1])
print(solve2(reports))
reports = readinput("input.txt")
print(solve2(reports))
