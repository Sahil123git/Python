import random
class greater_input(Exception):
    def display(self):
        print("Greater value")
class smaller_input(Exception):
    def display(self):
        print("Smaller value")

while(True):
    rand_val=random.randrange(10,100)
    try:
        val= int(input("Enter the value"))
        # rand_val=val
        if val<rand_val:
            raise smaller_input
        elif val > rand_val:
            raise greater_input
        else:
            print("congrats you got the same value")
    except greater_input as n:
        n.display()
        print(rand_val," ",type(n))
    except smaller_input as a:
        a.display()
        print(rand_val)
    else:
        print(rand_val," Congrats!!! you can vote")
        break




    
