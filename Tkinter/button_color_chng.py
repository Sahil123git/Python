from tkinter import*
class button:
    def __init__(self,root):

        self.f = Frame(root,height= 400, width=500,bg="red")
        self.f.propagate(0)
        self.f.pack()

        self.b1 = Button(self.f,text="Red",width=15, height= 2,
                         command = lambda: self.click(1))
        self.b2 = Button(self.f,text="Green",width=15, height= 2,
                         command = lambda: self.click(2))
        self.b3 = Button(self.f,text="Blue",width=15, height= 2,
                         command = lambda: self.click(3))

        # self.b1.grid(row=0,column=0)
        # self.b2.grid(row=0,column=1)
        # self.b3.grid(row=0,column=2)
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()

    def click(self,num):
        print("sfd")
        if num==1:
            self.f["bg"]= "red"
        if num == 2:
            self.f["bg"]= "green"
        if num==3:
            self.f["bg"]= "blue"

root = Tk()

mb= button(root)
root.mainloop()