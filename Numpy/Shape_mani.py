import numpy as n
e=n.array([[3,2,1,4],[6,8,4,2]])
print(e.shape)#will present no. of rows and col
e.shape=(4,2)#it will chng the col and row 
print(e)

r=e.reshape(2,4)
print(r)#but e will remain in prev chngd

