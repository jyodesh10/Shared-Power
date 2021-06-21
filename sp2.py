from tkinter import *
class LoginRegister:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1020x680+160+10")
        self.window.title("Shared Power || Login")
        self.window.resizable(0, 0)
        bg_img = PhotoImage(file="sp.png")
        bg_label = Label(self.window, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.window.mainloop()

    def Register_UI(self):
        self.Register_win = tk.Toplevel()
        self.Register_win.title("Shared Power || Register")
        self.Register_win.geometry("1020x680+160+10")
        self.Register_win.resizable(0, 0)

        register_name = Entry(self.Register_win)
        register_name.insert(0, "Full Name")
        register_name.pack()


c=LoginRegister()
