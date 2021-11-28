import pandas as p
dictnry={'Name':['a','b','c','d','y'],
   'Python':[1,2,3,4,4],
   'ds':[5,6,7,8,9]
   }
dataset=p.DataFrame(dictnry)#converting dic to dataset
print(dataset)
print(dataset['Python'].max()," print the max val from any col")
print(dataset['Python'].min()," print the min val from any col")
print(dataset['Python'].mean()," print the mean val from any col")
print(dataset['Python'].mode()," print the mode val from any col")#ele with max freq
print(dataset['Python'].median()," print the median val from any col")
