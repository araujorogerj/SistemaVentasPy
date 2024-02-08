from tkinter import Entry, Tk, Frame
from tkinter.ttk import LabelFrame

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Ventas')
        self.login_window()
        self.state('zoomed')
        self.configure(bg="lightblue")

    def login_window(self):
        self.frame_login = Frame(self)
        self.frame_login.pack()
        
        self.lblframe_login = LabelFrame(self.frame_login, text="Acceso")
        self.lblframe_login.pack(padx=30, pady=30)

        txt_user = Entry(self.lblframe_login)
        txt_user.pack(padx=30, pady=30)

def main():
    app = Window()
    app.mainloop()

if __name__=='__main__':
    main()
