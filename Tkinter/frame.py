from tkinter import*
root=Tk()

root.title("notepad")

f=Frame(root,height=200,width=300,bg="black",)
f.propagate(0)#our function sometime shrinks so this will not let that happen
f.pack()

b=Button(f,text="login",bg="yellow",height=2,width=20,fg="blue",activebackground="green",activeforeground="red",cursor="cross")
b.pack()

root.mainloop()
