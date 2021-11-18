class base:
    def __init__(self,pages):
        self.pages=pages
        
        
class derived:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages

        
b1=base(10)#passing one value because init is having only one value
b2=derived(20)
print(b2+b1)#here b2 fun is first so add function will be in that