# fuck this bruh

import copy

f = open('input.txt')

rotations = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}

class Guard():
    def __init__(self, i:int, j:int):
        self.i = i
        self.j = j
        self.direction = 'N'

    def rotate(self):
        self.direction = rotations[self.direction]

    def move(self):
        if self.direction == 'N': self.i -= 1
        elif self.direction == 'E': self.j += 1
        elif self.direction == 'S': self.i += 1
        else: self.j -= 1


# this function checks if there is an infinite loop
def test_obstacle(m:list, guard:Guard)->bool:
    try:
        while guard.i >= 0 and guard.j >= 0:
            if type(m[guard.i][guard.j]) != set:
                m[guard.i][guard.j] = set(guard.direction)
            else:
                m[guard.i][guard.j].add(guard.direction)
        
            # print(guard.i, guard.j, guard.direction)
            if guard.direction == 'N':
                next_point = m[guard.i-1][guard.j]
            elif guard.direction == 'E':
                next_point = m[guard.i][guard.j+1]
            elif guard.direction == 'S':
                next_point = m[guard.i+1][guard.j]
            else:
                next_point = m[guard.i][guard.j-1]

            if next_point == '.':
                guard.move()
            elif type(next_point) == set:
                if guard.direction in next_point:
                    return True # case where we have traversed this direction alrdy
                else:
                    guard.move()
            elif next_point == '#':
                guard.rotate()
        return False
    except IndexError:
        for line in m:
            print(line)
        return False


cleared_m = list()
for line in f:
    row = list()
    for ch in line[:-1].strip():
        row.append(ch)
    cleared_m.append(row)

col_length = len(cleared_m)
row_length = len(cleared_m[0])

m = list()
for row in cleared_m:
    m.append(row[:])

# locate
i, j = 0, 0
for x in range(col_length):
    for y in range(row_length):
        if cleared_m[x][y] == '^':
            i, j = x, y
            cleared_m[x][y] = '.'
            m[x][y] = 'X'

guard = Guard(i, j)

try:
    while guard.i >= 0 and guard.j >= 0:
        # print(guard.i, guard.j, guard.direction)
        next_point = str()
        if guard.direction == 'N':
            next_point = m[guard.i-1][guard.j]
        elif guard.direction == 'E':
            next_point = m[guard.i][guard.j+1]
        elif guard.direction == 'S':
            next_point = m[guard.i+1][guard.j]
        else:
            next_point = m[guard.i][guard.j-1]

        if next_point == '.':
            guard.move()
            m[guard.i][guard.j] = 'X'
        elif next_point == 'X':
            guard.move()
        elif next_point == '#':
            guard.rotate()
except IndexError:
    pass

'''
    at this point, m has marked the traversed path with X's
'''
res = 0
for x in range(len(m)):
    for y in range(len(m[0])):
        if m[x][y] == 'X':

            clear_copy = list()
            for row in cleared_m:
                clear_copy.append(row[:])

            clear_copy[x][y] = '#'
            if test_obstacle(clear_copy.copy(), Guard(i, j)):
                res += 1

print(res)
