from tkinter import Entry, Tk, Frame, Button, Label, LabelFrame, Toplevel

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Ventas')
        self.login_window()

    def login_window(self):
        self.frame_login = Frame(self)
        self.frame_login.pack()
        self.state('zoomed')
        
        self.lblframe_login = LabelFrame(self.frame_login, text="Acceso")
        self.lblframe_login.pack(padx=10, pady=10)

        txt_user = Entry(self.lblframe_login)
        txt_user.pack(padx=10, pady=10)

        btn_ingresar = Button(self.lblframe_login, text="Ingresar", command=self.open_new_window)
        btn_ingresar.pack(pady=10)

    def open_new_window(self):
        new_window = Toplevel(self)
        new_window.title("Nueva ventana")
        label = Label(new_window, text="Has ingresado")
        label.pack(padx=10, pady=10)

def main():
    app = Window()
    app.mainloop()

if __name__=='__main__':
    main()
