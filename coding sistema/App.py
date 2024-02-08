from tkinter import*

class Window(Tk):
    def __init__(self):
        super().__init__()

def main():
    app = Window()
    app.title('Sistema de Ventas')
    app.mainloop()


if __name__=='__main__':
    main()
