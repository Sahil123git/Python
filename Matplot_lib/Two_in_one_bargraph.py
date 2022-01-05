import pandas as pd
import matplotlib.pyplot as mp
d={"rollno":[1,2,3,4,5],"python":[100,23,45,72,34],"ds":[80,3,5,50,7]}
df=pd.DataFrame(d)

print(df["rollno"])
x=df["rollno"]
y=df["python"]
z=df["ds"]

mp.bar(x,y,label="Student py CA3 marks",color="red")
mp.bar(x,z,label="Student py CA2 marks",color="b")

mp.title("class report")
mp.legend()
mp.show()