try:
    file=open("Hello.txt","w")
    a=eval(input("enter the val"))
    b=eval(input("enter the val"))
    c=a/b#if there will be error in this line it will go to ZeroDivError
    z=str(c)
    print("it cannot find error")
    file.write(z)
except ZeroDivisionError:
    print("there is an error")
    print("Zero div erro")
    
finally:
    print("fix this")
    # print(z)
    file.close()
    