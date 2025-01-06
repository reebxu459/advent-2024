f = open(0)
line = f.readline()[:-1].split()
print(line)


def blink(old):
    new = list()
    for stone in old:
        if stone == '0':
            new.append('1')
        elif len(stone) % 2 == 0:
            half = len(stone)//2
            new.append(stone[:half])
            new.append(str(int(stone[half:])))
        else:
            new.append(str(int(stone) * 2024))
    return new


for i in range(25):
    line = blink(line)

print(len(line))
