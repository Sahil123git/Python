import re
s="an  apple a day keeps the a doctor away"
result=re.findall(r'a[\w]*',s)#this will find where there is a and print all its after chars
print(result)