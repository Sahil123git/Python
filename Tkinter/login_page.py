from tkinter import*
root=Tk()

class login:
    def __init__(self,root):#don't write this root with self inside this class
        self.fr=Frame(
            root,
            height="600",
            width="600",
            bg="brown"
        )
        self.fr.propagate(0)
        self.fr.pack()

        self.lb1=Label(
            self.fr,
            text="Enter your Registeration Number",
            font=("Verdana",20),
            bg="orange"
        )
        self.en1=Entry(
            self.fr,
            font=("Verdana",17),
        )
        self.lb1.pack(pady=(20,0))
        self.en1.pack(pady=(6,0))
        
        self.lb2=Label(
            self.fr,
            text="Enter your Password",
            font=("Verdana",20),
            bg="orange"
        )
        self.en2=Entry(
            self.fr,
            font=("Verdana",17),
            show="*",
        )
        self.lb2.pack(pady=(20,0))
        self.en2.pack(pady=(6,0))
        
        self.bt=Button(
            self.fr,
            text="Submit",
            font=("Verdana",20),
            command=self.click,
        )
        self.bt.pack(pady=30)

    def show_txt(self,user,pass_w):
        lb1=Label(
            self.fr,
            font=("Verdana",20),
            bg="orange",
            text="Your username is "+user
        )
        lb2=Label(
            self.fr,
            font=("Verdana",20),
            bg="orange",
            text="Your password is "+pass_w
        )
        lb1.pack()
        lb2.pack()

    def click(self):
            UserN=self.en1.get()
            pass_w=self.en2.get()
            self.lb1.destroy() 
            self.lb2.destroy() 
            self.en1.destroy() 
            self.en2.destroy() 
            self.bt.destroy()
            self.show_txt(UserN,pass_w)
            

mb=login(root)
root.mainloop()
        