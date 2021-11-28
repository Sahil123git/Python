import pandas as pd
df=pd.read_csv('weatherAUS.csv')
print(df.head(5))
print(df.MaxTemp.max())
print(df.MinTemp.min())