import tkinter
from tkinter import *
import random

#----------------------------Quiz starts---------------------------
questions=[
    "Q).Which of the following is a Python tuple?",#index=0
    "Q).What is the maximum possible length of an identifier in Python?",
    "Q).To add a new element to a list we use which Python command?",
    "Q).What arithmetic operators cannot be used with strings in Python?",
    "Q).Which of the following expressions is an example of type conversion?",
    "Q).What will be the output of the “hello” +1+2+3?",
    "Q).What will be displayed by print(ord(‘b’) – ord(‘a’))?",
    '''Q).Say s="hello" what will be the return value of type(s)?''',
    '''Q).What is "Hello".replace("l", "e")?''',
    "Which of the following commands will create a list?",#index=9
]
ans_choice=[#2D list
    ["{1, 2, 3}","{1:2,3:4}","[1, 2, 3]","(1, 2, 3)"],#ans 3 option
    ["79 characters","31 characters","63 characters","None of the above"],#ans 3 optn
    ["list1.addEnd(5)","list1.addLast(5)","list1.append(5)","list1.add(5)  "],#and 2 optn
    ["*","-","+","All of the above"],#ans 1 optn
    ["4.0 + float(3)","5.3 + 6.3","5.0 + 3","3 + 7"],#ans 0 optn
    ["hello123","hello","Error","hello6"],#ans error
    ["0","1","-1","2"],#ans 1 optn 98-97
    ["int","bool","str","String"],#ans 2
    ["Heeeo","Heelo","Heleo","None"],#ans 0
    ["list1 = list()","list1 = []","list1 = list([1, 2, 3])","all of the mentioned"],#ans 3
]

answers=[3,3,2,1,0,2,1,2,0,3]#all are acc to 0 based index
user_ans=[]
indexes=[]
def que_gen():#for getting random values in list to get diff Ques each time
    global indexes
    # indexes.append(3) to add any ques and check that 
    while(len(indexes)<6):
        x=random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
            
    print(indexes,"Ques indexes")
 
def show_result(score):
    label_ques.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    label_image=Label(
        root,
        border=0,
    )
    label_image.pack(pady=(40,30))
    label_text=Label(
        root,
        font=("Consolas",20),
        bg="orange",
    )
    label_text.pack()
    print("You got ",score)
    if(score>=20):
        img=PhotoImage(file="great.png")
        label_image.config(image=img)
        label_image.image=img 
        label_text.config(text="You can get O grade in ETE!!")
        
    elif(score>=10 and score<20):
        img=PhotoImage(file="ok.png")
        label_image.config(image=img)
        label_image.image=img       
        label_text.config(text="You can do better!!")
    
    else:
        img=PhotoImage(file="bad.png")
        label_image.config(image=img)
        label_image.image=img       
        label_text.config(text="You have to work hard to pass ETE!!")
        
    Show_score=Label(
    root,
    text="You got "+str(score)+" out of 30",
    width=25,
    font=("Times",14),
    background="black",
    foreground="gold",
    )
    Show_score.pack(pady=(10,0))


def chk_score():#To calculate the score +5 for every correct ans
     global indexes,user_ans,answers
     iter=0
     score=0
     for i in indexes:
         if(answers[i]==user_ans[iter]):
             score+=5
         iter+=1
     print("Marks obtained ",score)   
     show_result(score)     
            
ques=1    
def Selected():
    global radio_var,user_ans
    global label_ques,r1,r2,r3,r4
    global ques

    x=radio_var.get()#to access user's selected ans
    user_ans.append(x)#user ans list
    print("pressed",x)#to see what option user has pressed
    print(user_ans)
    if(ques < 6):#linking ques and optn to their correct place
        label_ques.config(text=questions[indexes[ques]])
        r1.config(text=ans_choice[indexes[ques]][0])
        r2.config(text=ans_choice[indexes[ques]][1])
        r3.config(text=ans_choice[indexes[ques]][2])
        r4.config(text=ans_choice[indexes[ques]][3])
        ques+=1
    else:
        chk_score()
             
def start_quiz():
    global label_ques,r1,r2,r3,r4#making global so that we can use in selected function
    label_ques=Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas",15),
        width = 700,
        justify="center",
        wraplength=600,
        background="black",
        foreground="white"
    )
    label_ques.pack(pady=(50,5))

    global radio_var #making this variable accessable outside this function
    radio_var=IntVar()
    radio_var.set(-1)
    
    r1=Radiobutton(
        root,
        text=ans_choice[indexes[0]][0],
        font=("Times",12),
        value=0,#this value we are saving in  radio_var 
        variable=radio_var,#here we will store value
        background="brown",
        foreground="yellow",
        command=Selected,#from here we will send value
    )
    r1.pack(pady=(10,0))
    r2=Radiobutton(
        root,
        text=ans_choice[indexes[0]][1],
        font=("Times",12),
        value=1,
        variable=radio_var,
        background="brown",
        foreground="yellow",
        command=Selected,
    )
    r2.pack(pady=(10,0))
    r3=Radiobutton(
        root,
        text=ans_choice[indexes[0]][2],
        font=("Times",12),
        value=2,
        variable=radio_var,
        background="brown",
        foreground="yellow",
        command=Selected,
    )
    r3.pack(pady=(10,0))
    r4=Radiobutton(
        root,
        text=ans_choice[indexes[0]][3],
        font=("Times",12),
        value=3,
        variable=radio_var,
        background="brown",
        foreground="yellow",
        command=Selected,
    )
    r4.pack(pady=(10,0))
 #-------------------------------Quiz----------------------------   


root=tkinter.Tk()#root is instance of tk class 
#this creates basic gui that is available in every GUI
root.title("Quiz App")#writing root.title so that it will call root's title
root.geometry("800x750")
root.config(background="white")
root.resizable(0,0)
root.configure(bg="orange")#making background colourful

img=PhotoImage(file="Logo_quiz.png")

def Start_pressed():
    lb_txt.destroy()
    start_bt.destroy()
    lb_img.destroy()
    lbl_rules.destroy()
    lbl_inst.destroy()
    que_gen()
    start_quiz()

lb_img =Label(
    root,
    image=img,
    background="orange",
)
lb_img.pack(pady=(0,0))

lb_txt=Label(
    root,
    text="QUIZ APP",
    font=("Comic sans MS",24,"bold"),
    background="orange",
)
lb_txt.pack(pady=(20,0))

st_bt_image=PhotoImage(file="St_button.png")
start_bt=Button(
    root,
    image=st_bt_image,
    relief="flat",
    background="orange",
    border=0,
    command=Start_pressed,
)
start_bt.pack(pady=(20,0))

#------------Rules start-------------------------------------------
lbl_inst=Label(
    root,
    text="Read the rules and\n Click start once ready",
    background="orange",
    font=("Times",14),
    justify="center",
)
lbl_inst.pack()
lbl_rules=Label(
    root,
    text="This quiz is having 6 question.\n Every ques is of 5 marks.\nOnce you select the option that will be final choice ",
    width=100,
    font=("Times",14),
    background="black",
    foreground="gold",
)
lbl_rules.pack(pady=(130,0))
#-------------------Rules end-------------------------------------
root.mainloop()