from tkinter import *
import sqlite3

windows = Tk()
windows.geometry('600x600')
windows.title("Shared Power")

def login():

     def login_database():
         conn=sqlite3.connect("sp.db")
         cur=conn.cursor()
         cur.execute('SELECT * FROM test WHERE email=? AND password=?',(e1.get(),e2.get()))     #FOR Validatation
         sow=cur.fetchall()
         conn.close()
         print(sow)
        # if sow!=[]:
        #     user_name= sow[0][1]
        #     l3.config(text="User created as :" + user_name)
        #else:
        #  l3.config(text='User not found')

     windows.destroy()
     login_windows=Tk()
     login_windows.geometry('500x500')
     l1=Label(login_windows,text='email',font='times 20')
     l1.grid(row=1,column=1)
     l2=Label(login_windows,text='password',font='times 20')
     l2.grid(row=2,column=1)
     l3=Label(login_windows, font='times 20')
     l3.grid(row=5,column=2)

     email_text=StringVar()
     e1=Entry(login_windows,textvariable=email_text)
     e1.grid(row=1,column=2)
     password_text=StringVar()
     e2=Entry(login_windows,textvariable=password_text)
     e2.grid(row=2,column=2)

     b1=Button(login_windows,text='Login',width=20,command=login_database)
     b1.grid(row=4,column=2)
     login_windows.mainloop()




def signUp():

    def signup_database():
        conn=sqlite3.connect("sp.db")
        cur=conn.cursor()
        try:
            cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text, email text,password text)")
        except Exception as e:
            pass
        cur.execute("INSERT INTO test VALUES(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
        l4=Label(signUp_windows,text='Account has been Creted',font='times 15')
        l4.grid(row=6,column=2)
        conn.commit()
        conn.close()


    windows.destroy()
    signUp_windows=Tk()
    signUp_windows.geometry('600x600')
    l1=Label(signUp_windows,text='user name',font='times 20')
    l1.grid(row=1,column=1)
    l2=Label(signUp_windows,text='User Email',font='times 20')
    l2.grid(row=2,column=1)
    l3=Label(signUp_windows,text='User Password',font='times 20')
    l3.grid(row=3,column=1)
    l4=Label(signUp_windows,text='Phone Number',font='times 20')
    l4.grid(row=4,column=1)
    l5=Label(signUp_windows,text='Address',font='times 20')
    l5.grid(row=5,column=1)

    name_text=StringVar()
    e1=Entry(signUp_windows,textvariable=name_text)
    e1.grid(row=1,column=2)
    email_text=StringVar()
    e2=Entry(signUp_windows,textvariable=email_text)
    e2.grid(row=2,column=2)
    password_text=StringVar()
    e3=Entry(signUp_windows,textvariable=password_text)
    e3.grid(row=3,column=2)
    phone_text=IntVar()
    e4=Entry(signUp_windows,textvariable=phone_text)
    e4.grid(row=4,column=2)
    address_text=StringVar()
    e5=Entry(signUp_windows,textvariable=address_text)
    e5.grid(row=5,column=2)

    b1=Button(signUp_windows,text='Register',width=20,command=signup_database)
    b1.grid(row=7,column=2)
    b2=Button(signUp_windows)







l1 = Label(windows,text='If you are Registered select Login. If not select Signup', font='times 20')
l1.grid(row=1,column=2,columnspan=2)

b1 = Button(windows,text="login",width=20,command=login)
b1.grid(row=2,column=2)

b2 = Button(windows,text='signUp',width=20,command=signUp)
b2.grid(row=2,column=3)

windows.mainloop()
