def fact(num,mul):#this is tail recursion
    if(num==1):
        return mul
    return fact(num-1,num*mul)

num=int(input())
print(fact(num,1))