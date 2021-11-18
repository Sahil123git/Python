class person:
    def __init__(self):
       self.d=10

    def display(self):
        print("name",self.d)

class teacher(person):
    def __init__(self):
        self.e='s'
        super().__init__()
        
    def display(self):
        super().display()
        print("re",self.e)
        print("wk")


t=teacher()
t.display()