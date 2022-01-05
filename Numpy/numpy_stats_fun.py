import numpy as np
arr1=np.array([1,2,3,3,6,8,5,1]).reshape(2,4)  
# print(arr1)
arr2=np.array([3,1,1,1,1,8,1,1]).reshape(2,4)  
print(arr2)
print(np.sum(arr2))
print(np.amin(arr1))
print(np.ptp(arr1)," ptp")
print(np.amin(arr1,0))
