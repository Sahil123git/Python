class base:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        
        sum=base(m1,m2)
        return sum #return this new sum obj
    
    def print_(self): 
        print(self.m1,self.m2)

a=base(12,13)
b=base(1,2)

c=a+b
# print(type(c))
c.print_()