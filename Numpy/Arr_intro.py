import numpy as np
r=np.array([2,1,4])
print(r)

t=np.array([[1,2,3,],[6,3,2],[67,12,4]])
print(t)
print(t.dtype)#data type
print(t.ndim)#dimension of matrix
print(t.itemsize)#size of each byte
print(t.nbytes)#total mem consumption (9*4=36)

# t.shape(2,3)