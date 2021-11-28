from tkinter import*
def click(self):
    print("You have clicked a login button")
root = Tk()
root.title("Notepad")

f = Frame(root,height= 200, width = 300)
f.propagate(0)
f.pack()

b = Button(f,text="Login",width=20, height= 2, bg="yellow",
           fg="blue",
           activebackground = "green",activeforeground="red")
b.pack()
b.bind("<Button-1>" , click)#1 left click, 3 for right click, 2 for middle click
root.mainloop()
