# hm..

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
ids -= 1

for i in range(ids, -1, -1):
    # l is inclusive, r is exclusive
    back_r = len(disk)-1
    while disk[back_r] != str(i):
        back_r -= 1
    back_l = back_r
    back_r += 1
    while disk[back_l] == str(i):
        back_l -= 1
    back_l += 1

    front_l, front_r = 0, 0
    try:
        while front_r < back_l:
            while disk[front_l] != '.':
                front_l += 1
            front_r = front_l
            while disk[front_r] == '.':
                front_r += 1
            if front_r - front_l >= back_r - back_l:
                disk[front_l: front_l + back_r - back_l], disk[back_l:back_r] = disk[back_l:back_r], disk[front_l: front_l + back_r - back_l]
                break
            
            front_l = front_r
    except IndexError:
        pass


# calc checksum
res = 0
for i in range(len(disk)):
    if disk[i].isnumeric():
        res += i * int(disk[i])


print(res)

