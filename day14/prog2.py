import time

class Bot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def move(self):
        self.px += self.vx
        self.py += self.vy
        self.px %= 101
        self.py %= 103


def empty_grid():
    grid = list()
    for _ in range(103):
        row = list()
        for _ in range(101):
            row.append('.')
        grid.append(row)
    return grid


f = open(0, 'r')

bots = list()
for line in f:
    line = line.strip().split()
    p, v = line[0], line[1]

    p = p.split(',')
    v = v.split(',')

    px = int(p[0][2:])
    py = int(p[1])
    vx = int(v[0][2:])
    vy = int(v[1])
    bots.append(Bot(px,py,vx,vy))

def get_score(bots):
    q1, q2, q3, q4 = 0, 0, 0, 0

    for bot in bots:
        if bot.px > 50:
            if bot.py > 51:
                q4 += 1
            if bot.py < 51:
                q2 += 1
        if bot.px < 50:
            if bot.py > 51:
                q3 += 1
            if bot.py < 51:
                q1 += 1

    return q1 * q2 * q3 * q4

seconds = 0
while True:
    grid = [[0 for _ in range(101)] for _ in range(104)]
    seconds += 1

    bad = False
    for i in range(len(bots)):
        bots[i].move()
        grid[bots[i].py][bots[i].px] += 1
        if grid[bots[i].py][bots[i].px] > 1:
            bad = True

    if not bad:
        print(seconds)
        for row in grid:
            print(row)
        break

