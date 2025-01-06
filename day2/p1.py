f = open('input.txt')
# f.readline()
# for line in f

res = 0
for line in f:
    report = line.split()
    if int(report[0]) < int(report[1]):
        # increasing
        unsafe = False
        for i in range(len(report)-1):
            diff = int(report[i+1]) - int(report[i])
            if diff > 3 or diff < 1:
                print(report, diff)
                unsafe = True
                break
        if not unsafe:
            res += 1

    elif int(report[0]) > int(report[1]):
        print(report[0], report[1])
        # decreasing
        unsafe = False
        for i in range(len(report)-1):
            diff = int(report[i]) - int(report[i+1])
            if diff > 3 or diff < 1:
                unsafe = True
                print("decreasing", report, diff)
                break
                
        if not unsafe:
            res += 1
print(res)





