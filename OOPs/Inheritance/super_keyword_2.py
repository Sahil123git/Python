class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print("name",self.name)
        print("age",self.age)

class teacher(person):
    def __init__(self,name,age,rs,we):
        super().__init__(name,age)
        self.rs="sahil"
        self.we=10
        
    def display(self):
        super().display()
        print("re",self.rs)
        print("wk",self.we)


t=teacher("sahil",50,"dl",12)
t.display()