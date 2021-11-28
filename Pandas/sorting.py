import pandas as p
dictnry={'Name':['a','b','c','d','y'],
   'Python':[5,9,3,4,4],
   'ds':[5,6,7,8,9]
   }
dataset=p.DataFrame(dictnry)#converting dic to dataset
print(dataset)
print(dataset.sort_values(by=['Python']))
