
class Base:
    def features(self):
        print("featrues of base")
        
class Derived(Base):
    def features1(self):
        print("features of derived")
        
class Super_derived(Derived):
    def features2(self):
        print("features of super derived class")
  
A=Derived()
A.features()
A.features1()

B=Super_derived()
B.features2()
B.features1()
B.features()