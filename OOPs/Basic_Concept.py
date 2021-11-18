class animal:
    val=12
    x=20
    def __init__(self,val,x):
        self.val=val
        self.x=x
    def display(self):
        print(self.x," | ",self.val)

ob=animal(12,45)
ob.display()