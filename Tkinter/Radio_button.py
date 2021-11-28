from tkinter import*
class sb:
    def __init__(self,root):

        self.f = Frame(root,height = 400, width = 500)
        self.f.propagate(0)
        self.f.pack()
        
        self.v1 = StringVar()
        self.v1.set(-1)
        
        self.c1=Radiobutton(
            self.f,bg="yellow",fg="green",
            text="C",
            value="C",
            variable=self.v1,
            command=self.display,
            font=("Arial",15,"bold")
        )
        self.c2=Radiobutton(
            self.f,bg="yellow",fg="green",
            text="C++",
            value="C++",
            variable=self.v1,
            command=self.display,
            font=("Arial",15,"bold")
        )
        self.c3=Radiobutton(
            self.f,bg="yellow",fg="green",
            text="Java",
            value="Java",
            variable=self.v1,
            command=self.display,
            font=("Arial",15,"bold")
        )
        self.c4=Radiobutton(
            self.f,bg="yellow",fg="green",
            text="Py",
            value="Py",
            variable=self.v1,
            command=self.display,
            font=("Arial",15,"bold")
        )
       
        
        self.c1.place(x=50,y=70)
        self.c2.place(x=50,y=120)
        self.c3.place(x=50,y=170)
        self.c4.place(x=50,y=220)
    

    def display(self):
        sb1 = self.v1.get()
        
        self.l1 = Label(self.f,text= str(sb1))
        self.l1.pack()


root= Tk()
s = sb(root)

root.mainloop()