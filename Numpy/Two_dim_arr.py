import numpy as np
arr1=np.array([1,2,3,3,6,8,0,1]).reshape(2,4)  
print(arr1)
arr2=np.array([3,6,9,9,16,80,10,15]).reshape(2,4)  
print(arr2)
print(" ")
# print(np.maximum(arr1,arr2))
print(np.minimum(arr1,arr2))


arr1=np.array([1,2,3,3,6,8,0,1]).reshape(2,4)  
# print(arr1)
arr2=np.array([3,6,9,9,16,80,10,15]).reshape(2,4)  
# print(arr2)
print(np.multiply(arr1,arr2))
# print(np.multiply(arr1,5))

