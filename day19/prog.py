from collections import defaultdict
from functools import cache

f = open(0, 'r')
patterns = set(f.readline().strip().split(', '))
f.readline()

@cache
def possible_design(design):
    if design == '': return True
    possible = False
    for pattern in patterns:
        if design.startswith(pattern):
            possible = possible or possible_design(design[len(pattern):])
    return possible

res = 0
for line in f:
    res += possible_design(line.strip())

print(res)
