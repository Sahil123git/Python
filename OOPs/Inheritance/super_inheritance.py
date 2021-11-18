class A:
    def __init__(self):
         print("hello")

    def features(self):
        print("base")

        
class B(A):
    def __init__(self):
        print("derived")
        super().__init__()#super keyword can achieve both
        super().features()

    def features(self):
        print("sa")
        
a=B()

    