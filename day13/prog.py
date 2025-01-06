import re

'''
a_x*a + b_x*b = prize_x
a_y*a + b_y*b = prize_y

a = (prize_x - b_x*b) / a_x
a_y((prize_x - b_x*b) / a_x) + b_y*b = prize_y

prize_x*a_y/a_x - a_y*b_x*b/a_x + b_y*b = prize_y
(b_y - a_y*b_x/a_x) * b = prize_y - prize_x*a_y/a_x
b = (prize_y - prize_x*a_y/a_x) / (b_y - a_y*b_x/a_x)
b = (a_y * prize_x - a_x) / (a_y * b_x - a_x * b_y)
'''



def calc_tokens(a_x, a_y, b_x, b_y, prize_x, prize_y):
    '''
    let a rep num of button A presses
    let b rep num of button B presses
    '''
    a, b = 0, 0
    b, b_remainder = divmod((a_y * prize_x - a_x * prize_y), (a_y * b_x - a_x * b_y))
    a, a_remainder = divmod((prize_x - b_x*b), a_x)
    res1 = 0 if a_remainder or b_remainder else 3*a + b
    
    base = 10000000000000
    prize_x += base
    prize_y += base
    b, b_remainder = divmod((a_y * prize_x - a_x * prize_y), (a_y * b_x - a_x * b_y))
    a, a_remainder = divmod((prize_x - b_x*b), a_x)
    res2 = 0 if a_remainder or b_remainder else 3*a + b
    return [res1, res2]

f = open(0, 'r')

machines = [tuple(map(int, re.findall(r'\d+', machine)))
            for machine in f.read().split('\n\n')]

res1 = 0
res2 = 0
for line in machines:
    print(line)
    res = calc_tokens(line[0], line[1], line[2], line[3], line[4], line[5])
    res1 += res[0]
    res2 += res[1]
print(res1)
print(res2)
