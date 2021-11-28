from tkinter import*
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "dfgdsfgsdf",
    database = "t20wc"
    )
m = db.cursor()
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
        
        self.bt1=Button(
            self.fr,
            text="SignIN",
            font=("Verdana",20),
            command=self.Signin,
        )
        self.bt1.pack(pady=(30,5))
        self.bt2=Button(
            self.fr,
            text="SignUP",
            font=("Verdana",20),
            command=self.signup,
        )
        self.bt2.pack(pady=(5,30))
#--------------------------------User credential checking------------------        
    def show_txt_right(self,user,pass_w):
        self.lb1.destroy() 
        self.lb2.destroy() 
        self.en1.destroy() 
        self.en2.destroy() 
        self.bt1.destroy()
        self.bt2.destroy()
        # self.b
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
    def show_txt_wrong(self,user,pass_w):
        self.lb1.destroy() 
        self.lb2.destroy() 
        self.en1.destroy() 
        self.en2.destroy() 
        self.bt1.destroy()
        self.bt2.destroy()
        
        lb3=Label(
            self.fr,
            font=("Verdana",20),
            bg="red",
            text="Please try again"
        )
        lb3.pack()
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
 #--------------------------------------------------------------------------        
    def Signin(self):
            UserN=self.en1.get()
            pass_w=self.en2.get()
            self.lb1.destroy() 
            self.lb2.destroy() 
            self.en1.destroy() 
            self.en2.destroy() 
            self.bt1.destroy()
            self.bt2.destroy()
            sql="select * from nam_usr where Reg_No=%s"
            val=(UserN,)
            m.execute(sql,val)
            pd=m.fetchone()
            if (pd):
                self.show_txt_right(UserN,pass_w)
            else:
                 print('There is no user with registration no ',UserN)
                 self.show_txt_wrong(UserN,pass_w)
                
            
    def signup(self):
         user_reg=str(self.en1.get())
         user_pass=str(self.en2.get())
         m.execute("INSERT INTO nam_usr(Reg_No,Password) VALUES(%s,%s)",(user_reg,user_pass))
         db.commit()
         self.bt2.destroy()
mb=login(root)
root.mainloop()
        
