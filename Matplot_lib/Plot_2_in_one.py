import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,10,5)
y=x**2
print(x)
print(y)

plt.plot(x,x**2,'r',label="x**2")
plt.plot(x,x**3,'g',label="x**3")
plt.title("Graph-AB")
plt.legend()#bydefault inside legend there is 0
plt.show()
