try:
    def cc(li):
        sum=0 
        for i in li:
            sum=sum+i       
        avg=sum/len(li) 
        return (sum,avg)

    sum1=0
    avg1=0

    sum1,avg1=cc([1,2,3])
    print(sum1," ",avg1)  
    sum1,avg1=cc([])
    print(sum1," ",avg1)
    sum1,avg1=cc([1,2,'a'])
    print(sum1," ",avg1)


except ZeroDivisionError as n:
    print("zero division error")
except TypeError as n:
    print("data types are not valid")
finally:
    print("no error")


