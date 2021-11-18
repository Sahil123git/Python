class animal:
    def __init__(self):
        self.name="sahil"
        self.rol=12
        self.wt=40

    def sleep(self):
        print(self.name,"hello")
    
    def bark(self):
        print(self.rol," ",self.wt)
        
        
d1=animal()
d1.sleep()
d1.bark()