f = open(0)

line = f.readline().strip()

disk = list()
ids = 0
for i in range(len(line)):
    if i % 2 == 0:
        block = [str(ids)] * int(line[i])
        ids += 1
    else:
        block = ['.'] * int(line[i])
    disk += block


l, r = 0, len(disk)-1
while l < r:
    if disk[l] != '.':
        l += 1
    elif disk[r] == '.':
        r -= 1
    else:
        disk[l], disk[r] = disk[r], disk[l]
        l += 1
        r -= 1

# calc checksum
res = 0
for i in range(len(disk)):
    if disk[i].isnumeric():
        res += i * int(disk[i])


print(res)


