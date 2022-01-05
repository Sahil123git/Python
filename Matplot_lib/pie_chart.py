import matplotlib.pyplot as mp
slices=[40,20,20,20]
dept=["sales","production","HR","IT"]
col=("r","g","b","y")
mp.pie(slices,labels=dept,colors=col,startangle=150,explode=(0.2,0,0,0))
mp.legend()
mp.show()
