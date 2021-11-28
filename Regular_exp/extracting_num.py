import re
str="the meeting is schedled on 1st and 30th of nxt month"
result=re.findall(r'\d[\w]*',str)
print(result)