from tkinter import*
class sb:
    def __init__(self,root):

        self.f = Frame(root,height = 400, width = 500)
        self.f.propagate(0)
        self.f.pack()

        self.v1 = IntVar()
        self.v2 = IntVar() 
        self.v3 = IntVar() 
        self.v4 = IntVar() 
        
        self.c1=Checkbutton(
            self.f,bg="yellow",fg="green",
            variable=self.v1,
            text="C",
            command=self.display,
            font=("Arial",15,"bold")
        )
        self.c2=Checkbutton(
            self.f,bg="yellow",fg="green",
            variable=self.v2,
            text="C++",
            command=self.display,
            font=("Arial",15,"bold")
        )
        self.c3=Checkbutton(
            self.f,bg="yellow",fg="green",
            variable=self.v3,
            text="Java",
            command=self.display,
            font=("Arial",15,"bold")
        )
        self.c4=Checkbutton(
            self.f,bg="yellow",fg="green",
            variable=self.v4,
            text="Py",
            command=self.display,
            font=("Arial",15,"bold")
        )
       
        
        self.c1.place(x=50,y=70)
        self.c2.place(x=50,y=120)
        self.c3.place(x=50,y=170)
        self.c4.place(x=50,y=220)
    

    def display(self):
        sb1 = self.v1.get()
        sb2 = self.v2.get()
        sb3 = self.v3.get()
        sb4 = self.v4.get()
        
        print(sb1," ",sb2," ",sb3," ",sb4)
        ans=""
        if sb1==1:
            ans+="C"
        elif sb2==1:
            ans+="C++"
        elif sb3==1:
            ans+="Java"
        elif sb4==1:
            ans+="Py"
                     
        print(ans)
        self.l1 = Label(self.f,text= ans)
        self.l1.pack()


root= Tk()
s = sb(root)

root.mainloop()