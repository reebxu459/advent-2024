from collections import Counter

f = open('input.txt')

l1, l2 = list(), list()

for line in f:
    line = line.split()
    l1.append(line[0])
    l2.append(line[1])

counter = Counter(l2)

res = 0
for n1 in l1:
    res += counter[n1] * int(n1)

print(res)
