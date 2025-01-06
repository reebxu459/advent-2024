f = open('input.txt')

l1, l2 = list(), list()

for line in f:
    line = line.split()
    l1.append(line[0])
    l2.append(line[1])

l1.sort()
l2.sort()

res = 0
for n1, n2 in zip(l1, l2):
    res += abs(int(n1) - int(n2))

print(res)
