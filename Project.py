from tkinter import *
import tkinter as tk
import sqlite3

conn = sqlite3.connect('users.db')
c=conn.cursor();
c.execute("""CREATE TABLE users(NAME VARCHAR(20) NOT NULL,ID INT NOT NULL);""")
conn.commint()
c.close()
conn.close()
class ogReg:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x500+160+10")
        self.window.title("Shared Power Login")
        self.window.resizable(0, 0)
        self.logUI()
        self.window.mainloop()

    def logUI(self):
        logEntry=Entry(self.window)
        logEntry.insert(0,"Enter Username")
        logEntry.config(bd=0)
        logEntry.pack()

        passEntry=Entry(self.window,show="*")
        passEntry.insert(0,"Enter password")
        passEntry.config(bd=0)
        passEntry.pack()

        #loginButtonImg=PhotoImage(file="img//loginbutton.png")
        logButton=Button(self.window,text="LOGIN",bd=3,bg="red",command=self.login)
        logButton.config(bd=0)
        logButton.place(x=460, y=480)
        logButton.pack()

        registerLabel=Label(self.window,text="Have you Registered?")
        registerLabel.pack()
        clickButton=Button(self.window,text="Register",font=2,command=self.register).pack()      

    def register(self):
        self.regWin=tk.Toplevel()
        self.regWin.title("REGISTER")
        self.regWin.geometry("500x500+160+10")
        self.regWin.resizable(0,0)

        regName1=Entry(self.regWin)
        regName2=Entry(self.regWin)
        regName1.insert(0,"Enter First Name")
        regName2.insert(0,"Enter Last Name")
        regName1.pack()
        regName2.pack()

        regMobile=Entry(self.regWin)
        regMobile.insert(0,"Enter Mobile Number")
        regMobile.pack()

        regPass=Entry(self.regWin,show="*")
        regPass.insert(0,"            ")
        regPass.pack()

        Radiobutton(self.regWin, text="Male").pack()
        Radiobutton(self.regWin, text="Female").pack()

        regButton=Button(self.regWin,text="REGISTER",command=self.logUI).pack()
        
        self.regWin.mainloop()
   
        

    def login(self):
        pass
        
        
        

s=LogReg()
