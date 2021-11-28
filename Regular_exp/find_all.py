import re
s="cat mat bat rat mattten monke mohan"
r=re.compile(r'm\w\w')
result=r.findall(s)
print(result)
