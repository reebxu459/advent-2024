# part 2

f = open('input.txt')

def get_trin_array(num:int):
    arr = list()
    def gentrin(n, ts = ''):
        if len(ts) == n:
            arr.append(ts)
        else:
            gentrin(n, ts + '0')
            gentrin(n, ts + '1')
            gentrin(n, ts + '2')
    gentrin(num)
    return arr

def calib_result(nums):
    num_operators = len(nums)-1

    # list of all bitstrings with length num_operators
    trin_strings = get_trin_array(num_operators)
    
    for trin in trin_strings:
        acc = int(nums[0])
        for i in range(len(trin)):
            if trin[i] == '0': 
                acc += int(nums[i+1])
            elif trin[i] == '1': 
                acc *= int(nums[i+1])
            else:
                acc = int(str(acc) + nums[i+1])

        if acc == ans:
            return ans

    return 0

res = 0
for line in f:
    line = line[:-1].strip().split()
    
    ans = int(line[0][:-1])
    nums = line[1:]
    
    res += calib_result(nums)

print(res)

