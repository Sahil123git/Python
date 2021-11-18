class base:
    def __init__(self,pages):
        self.pages=pages
        
    def __gt__(self,other):
        return self.pages>other.pages
        
class derived:
    def __init__(self,pages):
        self.pages=pages

        
b1=base(10)
b2=derived(20)

if(b1>b2):#here we r writing b1 first so __gt__ fun should be in that
    print("b1 is greater")
else:
    print("b2 is greater")