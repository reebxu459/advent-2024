import re

#211773366
class Bot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.board_px = (self.px + self.vx * 100) % 101
        self.board_py = (self.py + self.vy * 100) % 103

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

q1, q2, q3, q4 = 0, 0, 0, 0

for bot in bots:
    if bot.board_px > 50:
        if bot.board_py > 51:
            q4 += 1
        if bot.board_py < 51:
            q2 += 1
    if bot.board_px < 50:
        if bot.board_py > 51:
            q3 += 1
        if bot.board_py < 51:
            q1 += 1

print(q1 * q2 * q3 * q4)