class Animal:
    def __init__(self,n=10,s="sahil"):
        self.name=s
        self.val=n
    
    def sleep(self):
        print(self.name)
        print(self.val)

ob=Animal()
ob.sleep()

ob1=Animal(21,"rahil")
ob1.sleep()

