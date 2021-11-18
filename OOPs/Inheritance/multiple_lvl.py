class Base:
    def features(self):
        print("featrues of base")
        
class Derived:
    def features1(self):
        print("features of derived")
        
class Super_derived(Base,Derived):
    def features2(self):
        print("features of super derived class")

B=Super_derived()
B.features2()
B.features1()
B.features()