rules = open('rules2.txt')

# this dictionary holds values that cannot appear after the key
record = dict()
for line in rules:
    line = line[:-1].split('|')
    
    if line[1] in record:
        record[line[1]].append(line[0])
    else:
        record[line[1]] = [line[0]]
print(record)

manuals = open('manuals2.txt')

res = 0
for line in manuals:
    pages = line[:-1].split(',')
    correctly_ordered = True

    unallowed = set()

    for page_num in pages:
        if page_num in unallowed:
            correctly_ordered = False
            break
        try:
            for val in record[page_num]:
                unallowed.add(val)
        except KeyError:
            pass
    if correctly_ordered:
        # get middle num
        res += int(pages[len(pages)//2])
print(res)