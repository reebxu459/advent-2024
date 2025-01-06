ops = {0:'+', 1:'*'}

f = open('input.txt')

def get_bin_array(num:int):
    arr = list()
    def genbin(n, bs = ''):
        if len(bs) == n:
            arr.append(bs)
        else:
            genbin(n, bs + '0')
            genbin(n, bs + '1')
    genbin(num)
    return arr

def calib_result(nums):
    num_operators = len(nums)-1

    # list of all bitstrings with length num_operators
    bin_strings = get_bin_array(num_operators)
    
    for bin in bin_strings:
        acc = int(nums[0])
        for i in range(len(bin)):
            if bin[i] == '0': acc += int(nums[i+1])
            else: acc *= int(nums[i+1])
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

