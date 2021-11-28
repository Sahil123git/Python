from tkinter import*
def click1():
    f['bg']="red"

def click2():
    f["bg"]="green"
    
def click3():
    f["bg"]="blue"       
    
root = Tk()
root.title("Notepad")

f = Frame(root,height= 200, width = 300,bg="white")
f.propagate(0)
f.pack()

b1 = Button(f,text="Login",width=20, height= 2, bg="yellow",
           fg="blue",
           activebackground = "green",activeforeground="red",
           command=click1)

b2 = Button(f,text="Login",width=20, height= 2, bg="yellow",
           fg="blue",
           activebackground = "green",activeforeground="red",
           command=click2)

b3 = Button(f,text="Login",width=20, height= 2, bg="yellow",
           fg="blue",
           activebackground = "green",activeforeground="red",
           command=click3)
b1.pack()
b2.pack()
b3.pack()
root.mainloop()
