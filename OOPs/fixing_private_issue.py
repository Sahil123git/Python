class Animal:
    def __init__(self,a,b):
        self.v1=a
        self.__v2=b #v2 is now private
        
    def add(self):
        print(self.v1," ",end="")
        print(self.__v2,)
        
    def __sub(self):
        print(self.v1+2," ",end="")
        
        
a1=Animal(12,34)
a1.add()
a1._Animal__sub()#to accessing private ele or fun we can use this method underscore class name
print(a1.v1," ",end="")
print(a1._Animal__v2)