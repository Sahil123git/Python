class Base:
    def features(self):
        print("I am at base class")
        
class Derived:
    def features(self):
        print("I am at derived class")
        
A=Derived()
A.features()