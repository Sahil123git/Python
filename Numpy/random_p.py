import numpy as n
g=n.random.random([2,3])
print(g)

# print(g.flatten())#it works on copy
# print(g.ravel())#it works on original arr and modify that
# h=g.T
h=n.transpose(g)
print(g)