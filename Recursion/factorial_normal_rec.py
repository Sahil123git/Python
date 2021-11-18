def fact(num):#this is normal recursion
    if(num==1):
        return 1
    return num*fact(num-1)

num=int(input())
print(fact(num))