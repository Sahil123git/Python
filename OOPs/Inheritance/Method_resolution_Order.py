class A:
    def __init__(self):
         print("Constructor of Base")

    def features(self):
        print("fun")

        
class B:
    def __init__(self):
        print("construtor of derived")

    def features(self):
        print("fun2")
    
class C(B,A):#here it is using Method resolution order will not print constructor of A
    
    def __init__(self):
        print("constructor of C")
        super().__init__()
        
a=C()
a.features()

    