from tkinter import*
def click1(clk):
    print(clk)
    if(clk==1):
        f['bg']="red"
    elif(clk==2):
        f["bg"]="green"
    else:
        f["bg"]="blue"
          
    
root = Tk()
root.title("Notepad")

f = Frame(root,height= 200, width = 300,bg="white")
f.propagate(0)
f.pack()

b1 = Button(f,text="Login",width=20, height= 2, bg="yellow",
           fg="blue",
           activebackground = "green",activeforeground="red",
           command=lambda:click1(1))#w/o lambda it will not work

b2 = Button(f,text="Login",width=20, height= 2, bg="yellow",
           fg="blue",
           activebackground = "green",activeforeground="red",
           command=lambda:click1(2))

b3 = Button(f,text="Login",width=20, height= 2, bg="yellow",
           fg="blue",
           activebackground = "green",activeforeground="red",
           command=lambda:click1(3))
b1.pack()
b2.pack()
b3.pack()
root.mainloop()
