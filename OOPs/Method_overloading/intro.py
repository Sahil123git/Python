class base:
    def sum(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            print("all are present")
        elif(a!=None and b!=None):
            print("2 are present")
        else:
            print("only one is present")

a=base()
a.sum(1,2,3)
a.sum(1,2)
a.sum(1)
