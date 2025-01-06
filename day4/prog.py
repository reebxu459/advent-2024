f = open('input.txt')

def check_hor(m, i, j, ch):
    res = 0
    index = indices[ch]
    # check forward
    forward = ''
    for n in range(1, index+1):
        forward = m[i][j-n] + forward
    for n in range(4 - index):
        forward += m[i][j+n]

    if forward == 'XMAS': res += 1

    # check backward
    backward = ''
    for n in range(1, index+1):
        backward = m[i][j+n] + backward
    for n in range(4 - index):
        backward += m[i][j-n]
    
    if backward == 'XMAS': res += 1
    return res

def check_vert(m, i, j, ch):
    res = 0
    index = indices[ch]
    # check forward
    forward = ''
    for n in range(1, index+1):
        forward = m[i-n][j] + forward
    for n in range(4 - index):
        forward += m[i+n][j]

    if forward == 'XMAS': res += 1

    # check backward
    backward = ''
    for n in range(1, index+1):
        backward = m[i+n][j] + backward
    for n in range(4 - index):
        backward += m[i-n][j]
    
    if backward == 'XMAS': res += 1
    return res

def check_diag_desc(m, i, j, ch):
    res = 0
    index = indices[ch]
    # check forward
    forward = ''
    for n in range(1, index+1):
        forward = m[i-n][j-n] + forward
    for n in range(4 - index):
        forward += m[i+n][j+n]

    if forward == 'XMAS': res += 1

    # check backward
    backward = ''
    for n in range(1, index+1):
        backward = m[i+n][j+n] + backward
    for n in range(4 - index):
        backward += m[i-n][j-n]
    
    if backward == 'XMAS': res += 1
    return res

def check_diag_asc(m, i, j, ch):
    res = 0
    index = indices[ch]
    # check forward
    forward = ''
    for n in range(1, index+1):
        forward = m[i+n][j-n] + forward
    for n in range(4 - index):
        forward += m[i-n][j+n]

    if forward == 'XMAS': res += 1

    # check backward
    backward = ''
    for n in range(1, index+1):
        backward = m[i-n][j+n] + backward
    for n in range(4 - index):
        backward += m[i+n][j-n]
    
    if backward == 'XMAS': res += 1
    return res

# put into padded matrix
m = list()
for line in f:
    row = list()
    for ch in line[:-1]:
        row.append(ch)
    m.append(['.','.','.'] + row + ['.','.','.'])

column_len = len(m)
row_len = len(m[0]) - 6
fill_row = (column_len + 6) * ['.']
m = [fill_row] * 3 + m + [fill_row] * 3

indices = {'X':0, 'M':1, 'A':2, 'S':3}

res = 0
for i in range(3, column_len+3):
    for j in range(3, row_len+3):
        res += check_vert(m, i, j, m[i][j])
        res += check_hor(m, i, j, m[i][j])
        res += check_diag_asc(m, i, j, m[i][j])
        res += check_diag_desc(m, i, j, m[i][j])


for row in m:
    print(row)
print(res / 4)