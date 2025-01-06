from collections import Counter

f = open(0)
line = f.readline()[:-1].split()
print(line)


length = len(line)


def blink(old):
    new = dict()
    for stone, val in old.items():
        key = str(stone)
        if key == '0':
            if 1 in new: new[1] += val
            else: new[1] = val

        elif len(key) % 2 == 0:
            half = len(key)//2
            first_half = int(key[:half])
            second_half = int(key[half:])
            if first_half in new: new[first_half] += val
            else: new[first_half] = val
            if second_half in new: new[second_half] += val
            else: new[second_half] = val

        else:
            s = int(key) * 2024
            if s in new: new[s] += val
            else: new[s] = val
    return new

counter = Counter(map(int, line))

for i in range(75):
    counter = blink(counter)

print(sum(counter.values()))
