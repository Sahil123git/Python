import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,10,5)
y=x**2
print(x)
print(y)

plt.subplot(1,3,1)#1st is no's of row 2nd is no's of col and 3rd is which one u r ptng
plt.plot(x,y,'r')
plt.title("Graph-A")

plt.subplot(1,2,2)#now u r ptng to 2nd graph
plt.title("Graph-B")
plt.plot(y,x,'b')

plt.show()
