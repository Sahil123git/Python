try:
    a=eval(input("enter the val"))
    b=eval(input("enter the val"))
    c=a/b
    z=str(c)
except ZeroDivisionError:
    print("there is an error")
    print("Zero div erro")
    
finally:
    print("Now fixed")
    