from itertools import permutations

grid = {
    i+j*1j: c 
    for i,r in enumerate(open(0))
    for j,c in enumerate(r.strip())
}

nodes = dict()
antinodes = set()

for row in grid:
    if grid[row] != '.':
        if grid[row] not in nodes:
            nodes[grid[row]] = {row}
        else:   
            nodes[grid[row]].add(row)

for node in nodes:
    pairs = permutations(nodes[node], 2)
    for pair in pairs:
        for i in range(50):
            new = pair[0] + i * (pair[0] - pair[1])
            antinodes.add(new)

print(len(antinodes & set(grid)))

