with open(0, 'r') as f:
    garden = [list(line.strip()) for line in f]

def get_region(i, j, ch) -> set:
    ret = set()
    if garden[i][j] == ch: ret |= {(i, j)}
    else: return set()
    garden[i][j] = '.'
    
    if i > 0 and garden[i-1][j] == ch: ret |= get_region(i-1, j, ch)
    if i < len(garden)-1 and garden[i+1][j] == ch: ret |= get_region(i+1, j, ch)
    if j > 0 and garden[i][j-1] == ch: ret |= get_region(i, j-1, ch)
    if j < len(garden[0])-1 and garden[i][j+1] == ch: ret |= get_region(i, j+1, ch)

    return ret


def calc_price(region):
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

    print(a, p, a * p)
    return a * p

total_price = 0
for i in range(len(garden)):
    for j in range(len(garden[0])):
        if garden[i][j] != '.':
            total_price += calc_price(get_region(i, j, garden[i][j]))
            # print('\n')
            # for line in garden:
            #     print(line)

print(total_price)

