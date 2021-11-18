try:
    a=eval(input("enter the val"))
    b=eval(input("enter the val"))
    c=a/b
    z=str(c)
    raise ZeroDivisionError#it will occur every time even there is error or not
    #use raise with class this error will get resolve
except ZeroDivisionError as z:
    print("there is an error")
    print("Zero div erro")
    
finally:
    print("fix this")
    