from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Login Page")
root.geometry("925x550")
root.configure(bg="#fff")
root.resizable(False,False)

owner="Muzzamil"
def signin():
    username=user.get()
    password=code.get()
    if username=="Admin" and password=="admin1234":
        messagebox.showinfo("Login",f"Welcome Mr: {owner}")
    else:
        messagebox.showerror("Login","Invalid Credentials")


img=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\login (2).png")
Label(root,image=img,bg="white").place(x=50,y=50)
frame=Frame(root,width=360,height=360,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign in",fg="#57a1f8",bg="white",font=("Broadway",25,"bold"))
heading.place(x=120,y=10)

def on_enter(e):
    user.delete(0, "end")
def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Username")


user=Entry(frame,width=27,fg="black",border=0,bg="white",font=("Calibri",14))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
Frame(frame,width=300,height=3,bg="black").place(x=25,y=107)


def on_enter(e):
    code.delete(0, "end")
def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Password")
code=Entry(frame,width=27,fg="black",border=0,bg="white",font=("Calibri",14))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)
Frame(frame,width=300,height=3,bg="black").place(x=25,y=177)


Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=205)
label=Label(frame,text="Don't have an account?",fg='black',bg="white",font=("Broadway",10))
label.place(x=75,y=270)

signup=Button(frame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8")
signup.place(x=250,y=270)
root.mainloop()
