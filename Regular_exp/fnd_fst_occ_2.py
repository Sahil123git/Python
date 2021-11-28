import re
s="an apple a day keeps the a doctor away"
result=re.findall(r'\ba[\w]*',s)#this will find where there is ' a' word and will pick that
print(result)