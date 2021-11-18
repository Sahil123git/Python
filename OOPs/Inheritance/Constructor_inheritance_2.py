class A:
    def __init__(self):
         print("hello")

    def features(self):
        print("base")

        
class B(A):
    def __init__(self):
        print("derived")#because it having its const so it will not call A const
    def features(self):
        print("sa")
        
a=B()

    