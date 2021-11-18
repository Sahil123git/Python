str=input()
new_str=str.lower()
# print(new_str);

dic={}
for i in new_str:
    dic[i]=0
    
for i in new_str:
    dic[i]=dic[i]+1
    
# print(dic)
for key,i in dic.items():
    print(key," ",end="")
    for j in range(i):
        print("*",end="")   
    print() 