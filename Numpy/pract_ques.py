import numpy as np
array3d = np.array([ [[1, 2, 5],[6,0,2]] , [[5,9,8],[0,3,2]] ]) 
print(array3d) 
print(array3d[1,0,1]," ans")

#---------------------------------------------
a=np.array([[1,2],[3,4],[5,6]])
y=a[[0,1,2],[0,1,1]]#index is 1st->(0,0)=1, 2nd->(1,1)=4,3rd->(2,1)=6
print(y)

#---------------------------------------------
a=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# print("our array is:")
# print(a)
rows =np.array([[0,0],[3,3]])
col =np.array([[0,2],[0,2]])
y=a[rows,col]
print(y)

#---------------------------------------------
a=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print("our array is:")
print(a)
print(a[a>5])

