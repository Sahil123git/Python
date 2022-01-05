import pandas as pd
import matplotlib.pyplot as mp
d={"rollno":[1,2,3,4,5],"python":[10,23,45,12,34]}
df=pd.DataFrame(d)

print(df["rollno"])
x=df["rollno"]
y=df["python"]
mp.bar(x,y,color="r",label="Student py CA3 marks")#r only will also work
mp.title("class report")
mp.legend()
mp.show()