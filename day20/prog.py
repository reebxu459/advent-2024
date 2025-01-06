from collections import deque, Counter

def bfs(g, coords, goal):
    visited=set()
    q = deque()
    dis = dict()
    dis[coords] = 0

    q.append(coords)
    visited.add(coords)

    while q:
        cur = q.pop()
        x, y = cur[0], cur[1]
        
        for adj1, adj2 in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
            adjacent = (x + adj1, y + adj2)

            if len(g) > adjacent[0] >= 0 and len(g[0]) > adjacent[1] >= 0 and adjacent not in visited:
                if g[adjacent[0]][adjacent[1]] == '.' or g[adjacent[0]][adjacent[1]] == goal:
                    visited.add(adjacent)
                    q.appendleft(adjacent)
                    dis[adjacent] = dis[cur] + 1

    print(dis)
    return dis


f = open(0, 'r')

s_coords = (0,0)
e_coords = (0,0)
g = list()

for line in f:
    row = list()
    for ch in line.strip():
        row.append(ch)
    g.append(row)

for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j] == 'S': s_coords = (i, j)
        if g[i][j] == 'E': e_coords = (i, j)

s_dis = bfs(g, s_coords, 'E')
e_dis = bfs(g, e_coords, 'S')

res = 0

thresh = 0

for i in range(len(g)):
    for j in range(len(g[0])):
        for i2 in range(len(g)):
            for j2 in range(len(g[0])):
                if (
                    (i != i2 or j != j2) and
                    g[i][j] != '#' and g[i2][j2] != '#' and
                    ((j == j2 and abs(i - i2) == 2) or (i == i2 and abs(j - j2) == 2))
                ):
                    end1 = (i, j)
                    end2 = (i2, j2)
                    if s_dis[e_coords] - (s_dis[end1] + e_dis[end2]) - 2 >= 100:
                        res += 1

print(res)
