import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,10,5)
y=x**2
print(x)
print(y)

plt.plot(x,y,"green",label="x,y",linestyle="dotted")#1st is for x axis which val 
#2nd is for y axis which va
#3rd is which color u want
plt.title('graph')
plt.xlabel("x-axis")
plt.ylabel('y-axis')
plt.legend()
plt.show()
