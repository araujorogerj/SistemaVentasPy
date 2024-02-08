from tkinter import Tk, Button

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Ventas')
        self.configure(bg="lightblue")
        self.state("zoomed")
        self.boton = Button(self, text="Clickea", command=self.on_click_button)
        self.boton.pack()

    def on_click_button(self):
        print("Boton Clickeado")

def main():
    app = Window()
    app.mainloop()

if __name__=='__main__':
    main()