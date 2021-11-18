class invalidAge(Exception):
    def display(self):
        print("Sorry !!! Age cannot be below 18...You cannot vote")
class invalidName(Exception):
    def display(self):
        print("Please enter a valid name....")

try:
    name= input("Enter the name")
    if len(name)==0:
        raise invalidName
    age = int(input("Enter the age"))
    if age < 18:
        raise invalidAge
except invalidName as n:
    n.display()
except invalidAge as a:
    a.display()
else:
    print("Congrats!!! you can vote")
finally:
    print("every thing is done")




    
