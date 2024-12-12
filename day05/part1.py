import re

f = open("input.txt", "r")
rules, updates = f.read().strip().split("\n\n")
rules = rules.split()
updates = updates.split()

def nums(s):
    return list(map(int, re.findall(r'\d+', s)))

graph = {}
rgraph = {}
for rule in rules:
    a, b = nums(rule)
    if a not in graph:
        graph[a] = set()
    graph[a].add(b)

    if b not in rgraph:
        rgraph[b] = set()
    rgraph[b].add(a)


def validate_update(rgraph, pages):
    for i in range(len(pages)):
        for j in range(i+1, len(pages)):
            tocheck = rgraph.get(pages[i], None)
            if tocheck is not None and pages[j] in tocheck:
                return False
    return True

total = 0
for pageset in updates:
    pages = nums(pageset)
    if validate_update(rgraph, pages):
        print(pages)
        total += pages[len(pages)//2]

print(total)
