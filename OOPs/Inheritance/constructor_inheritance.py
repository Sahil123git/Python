class A:
    def __init__(self):
         print("hello")

    def features(self):
        print("base")

        
class B(A):
    def features(self):
        print("sa")
        
a=B()

    