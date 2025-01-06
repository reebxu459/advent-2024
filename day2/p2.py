f = open('input.txt')
# f.readline()
# for line in f

def is_safe(report):
    if int(report[0]) < int(report[1]):
        # increasing
        for i in range(len(report)-1):
            diff = int(report[i+1]) - int(report[i])
            if diff > 3 or diff < 1:
                return False
        return True

    elif int(report[0]) > int(report[1]):
        # decreasing
        for i in range(len(report)-1):
            diff = int(report[i]) - int(report[i+1])
            if diff > 3 or diff < 1:
                return False
        return True
    
    return False


res = 0
for line in f:
    report = line.split()
    if is_safe(report): res += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                res += 1
                break

print(res)





