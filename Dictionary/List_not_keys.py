d = {(1,2,3,4): 'a', 1: 'b', 2: 'c'}
for x in d.keys():#if list is used as keys it will give error
    print(d[x])
for x in d:
    print(x,d[x])
