f = open(0, 'r')
patterns = f.read().split('\n\n')

locks = list()
keys = list()

for pattern in patterns:
    pattern = pattern.split()
    if pattern[0] == '#####':
        lock_vals = [-1] * 5
        for row in pattern:
            for i in range(5):
                if row[i] == '#':
                    lock_vals[i] += 1
        locks.append(lock_vals)
    else:
        key_vals = [-1] * 5
        for row in pattern:
            for i in range(5):
                if row[i] == '#':
                    key_vals[i] += 1
        keys.append(key_vals)

res = 0
for lock in locks: 
    for key in keys:
        for i in range(5):
            if lock[i] + key[i] > 5:
                print(lock, key)
                res += 1
                break

print(len(locks) * len(keys) - res)

