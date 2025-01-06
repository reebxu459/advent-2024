with open(0, 'r') as f:
    garden = [list(line.strip()) for line in f]


def get_region(i, j, ch):
    region = set()
    s = 0 # number of sides
    
    def search(i, j, ch):
        region.add((i, j))
        garden[i][j] = '.'
        
        if i > 0 and garden[i-1][j] == ch: search(i-1, j, ch)
        if i < len(garden)-1 and garden[i+1][j] == ch: search(i+1, j, ch)
        if j > 0 and garden[i][j-1] == ch: search(i, j-1, ch)
        if j < len(garden[0])-1 and garden[i][j+1] == ch: search(i, j+1, ch)
    
    search(i, j, ch)

    for x, y in region:
        # Outer corners
        s += ( x - 1, y ) not in region and ( x, y - 1 ) not in region
        s += ( x + 1, y ) not in region and ( x, y - 1 ) not in region
        s += ( x - 1, y ) not in region and ( x, y + 1 ) not in region
        s += ( x + 1, y ) not in region and ( x, y + 1 ) not in region
        # Inner corners
        s += ( x - 1, y ) in region and ( x, y - 1 ) in region and ( x - 1, y - 1 ) not in region
        s += ( x + 1, y ) in region and ( x, y - 1 ) in region and ( x + 1, y - 1 ) not in region
        s += ( x - 1, y ) in region and ( x, y + 1 ) in region and ( x - 1, y + 1 ) not in region
        s += ( x + 1, y ) in region and ( x, y + 1 ) in region and ( x + 1, y + 1 ) not in region

        # if (
        #     garden[tile[0]-1][tile[1]+1] != ch
        #     and (
        #             (
        #                 garden[tile[0]-1][tile[1]] == ch and
        #                 garden[tile[0]][tile[1]+1] == ch
        #             ) 
        #             or 
        #             (
        #                 garden[tile[0]-1][tile[1]] != ch and
        #                 garden[tile[0]][tile[1]+1] != ch
        #             )
        #         )
        #     ): edges.add((tile[0]-1, tile[1]+1))
    return [region, s]


def calc_price(sets):
    region = sets[0]
    num_sides = sets[1]
    def num_fences(i, j) -> int:
        fences = 0
        if (i-1, j) not in region: fences += 1
        if (i+1, j) not in region: fences += 1
        if (i, j-1) not in region: fences += 1
        if (i, j+1) not in region: fences += 1
        return fences
    
    a = len(region)
    p = 0
    for tile in region:
        p += num_fences(tile[0], tile[1])

    return [a * p, a * num_sides]

ans1 = 0
ans2 = 0
for i in range(len(garden)):
    for j in range(len(garden[0])):
        if garden[i][j] != '.':
            res = calc_price(get_region(i, j, garden[i][j]))
            ans1 += res[0]
            ans2 += res[1]

print(ans1)
print(ans2)

