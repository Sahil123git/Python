import pandas as p
dictnry={'Name':['a','b','c','d','y'],
   'Python':[1,2,3,4,5],
   'ds':[5,6,7,8,9]
   }
dataset=p.DataFrame(dictnry)#converting dic to dataset
print(dataset)

print(dataset['Python'][2]," ",end="")
print(dataset['Name'][2])#to access val from data set

print(dataset['Name'])
print(dataset[['Name','Python']])#2brackets becoz we assume this as our 2D arr

print(dataset.dtypes)
print(dataset.ndim)
print(dataset.shape," printing shape of dataset")
print(dataset.size," Printing size")
print("printing head val")#bydef 5 val
print(dataset.head)
print("printing tail val")
print(dataset.tail(3))