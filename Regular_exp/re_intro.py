import re
s="cat mat bat rat"
r=re.compile(r'm\w\w')
result=r.search(s)
print(result.group())
