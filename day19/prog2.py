from collections import defaultdict
from functools import cache

f = open(0, 'r')
patterns = f.readline().strip().split(', ')
f.readline()

@cache
def possible_design(design):
    if design == '': return 1
    possible = 0
    for pattern in patterns:
        if design.startswith(pattern):
            possible += possible_design(design[len(pattern):])
    return possible

res = 0
for line in f:
    res += possible_design(line.strip())

print(res)
