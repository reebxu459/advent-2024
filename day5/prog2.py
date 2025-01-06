# returns -1 if allowed. returns value of rule-breaker if not
def is_unallowed(unallowed, val)->int:
    for tup in unallowed:
        if val == tup[1]: return tup[0]
    return -1

rules = open('rules2.txt')

# this dictionary holds values that cannot appear after the key
record = dict()
for line in rules:
    line = line[:-1].split('|')
    
    if line[1] in record:
        record[line[1]].append(line[0])
    else:
        record[line[1]] = [line[0]]
for r in record:
    print(r, record[r])

manuals = open('manuals2.txt')

res = 0
for line in manuals:
    pages = line[:-1].split(',')
    correctly_ordered = True

    unallowed = list()

    i = 0
    while i < len(pages):
        # print(pages, i)
        unallowed_val = is_unallowed(unallowed, pages[i])
        if unallowed_val != -1:
            correctly_ordered = False
            after_index = pages.index(unallowed_val)
            before_item = pages.pop(i)
            pages.insert(after_index, before_item)
            i = 0
            unallowed = list()
        try:
            for val in record[pages[i]]:
                unallowed.append((pages[i], val))
        except KeyError:
            pass
        i += 1

    if not correctly_ordered:
        print(pages)
        # get middle num
        res += int(pages[len(pages)//2])
print(res)
