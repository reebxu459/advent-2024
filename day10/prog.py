f = open(0)

class Map():
    def __init__(self):
        self.map = list()
        for line in f:
            row = list()
            for ch in line[:-1].strip():
                row.append(ch)
            self.map.append(row)

    def get_trail_score(self, i:int, j:int, ch='0') ->int:
        nine_coords = set()

        def find_path(i, j, ch):
            if ch == '.': return
            if ch == '9': nine_coords.add((i, j))
            
            else:
                surroundings = list()

                if i+1 < len(self.map): surroundings.append([self.map[i+1][j], i+1, j])
                if i-1 >= 0: surroundings.append([self.map[i-1][j], i-1, j])
                if j+1 < len(self.map[0]): surroundings.append([self.map[i][j+1], i, j+1])
                if j-1 >= 0: surroundings.append([self.map[i][j-1], i, j-1])

                for i in range(len(surroundings)):
                    if int(surroundings[i][0]) != int(ch) + 1:
                        surroundings[i][0] = '.'
                
                for s in surroundings:
                    find_path(s[1], s[2], s[0])
        find_path(i, j, ch)
        return len(nine_coords)

m = Map()
res = 0
for i in range(len(m.map)):
    for j in range(len(m.map[0])):
        if m.map[i][j] == '0':
            res += m.get_trail_score(i, j)
print(res)


