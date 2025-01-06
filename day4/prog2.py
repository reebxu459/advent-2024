f = open('input.txt')

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
        if m[i][j] == 'A':
            asc, desc = False, False
            if (m[i-1][j-1] == 'M' and m[i+1][j+1] == 'S' or
                m[i-1][j-1] == 'S' and m[i+1][j+1] == 'M'):
                desc = True
            if (m[i+1][j-1] == 'M' and m[i-1][j+1] == 'S' or
                m[i+1][j-1] == 'S' and m[i-1][j+1] == 'M'):
                asc = True
            if desc and asc: res += 1


for row in m:
    print(row)
print(res)