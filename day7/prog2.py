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

def calib_result(nums, ans):
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

def get_all_concats(nums):
    arr = list()
    bins = get_bin_array(len(nums)-1)

    for bin in bins:
        new_nums = list()
        cur = nums[0]
        for i in range(len(bin)):
            if bin[i] == '0':
                cur += nums[i+1]
            elif bin[i] == '1':
                new_nums.append(cur)
                cur = nums[i+1]
        if cur != '':
            new_nums.append(cur)
        arr.append(new_nums)

    return arr

res = 0
for line in f:
    line = line[:-1].strip().split()
    
    ans = int(line[0][:-1])
    nums = line[1:]
    
    concats = get_all_concats(nums)

    for concat in concats:
        ret = calib_result(concat, ans)
        if ret != 0:
            res += ret
            break

print(res)

