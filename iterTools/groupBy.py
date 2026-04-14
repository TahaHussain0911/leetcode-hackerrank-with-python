from itertools import groupby

data='1222311'

groups = []
for k, g in groupby(data):
    count = len(list(g))
    groups.append((count,int(k)))          # count consecutive items
    # print()
    
print(*groups)