from cProfile import label
from tkinter import NS, NSEW, Entry, Tk, Frame, Button, Label, LabelFrame, Toplevel, ttk
import ttkbootstrap as tb


#Se define la clase Window que hereda de Tk (ventana principal de tkinter). En el método __init__, 
#se inicializa la ventana con un título y se llama al método login_window() para crear la ventana 
#de inicio de sesión.

class Window(tb.Window):
    def __init__(self):
        super().__init__()
        self.login_window()
            
    #Este método crea la ventana de inicio de sesión. Se crea un Frame dentro de la ventana principal, 
    #se configura para que se expanda a toda la ventana (self.state('zoomed')) y se establece un color 
    #de fondo.

    def login_window(self):
        self.frame_login = Frame(self)
        self.frame_login.pack()
        
        #Se crea un LabelFrame dentro del Frame principal con un título y colores personalizados. Luego, 
        #se configuran el peso de la fila y columna principal para que el LabelFrame se expanda y se centre
        #en la ventana.
        
        self.lblframe_login = LabelFrame(self.frame_login, text="Acceso", bg="#3f8189", fg="white")
        self.lblframe_login.pack(padx=40, pady=10)
        
        #Se crean un Label con el texto "Inicio de sesión", un campo de entrada (Entry) y un botón
        #dentro del LabelFrame.
        lbltitle=ttk.Label(self.lblframe_login, text="Inicio de sesion" , font=('Arial', 18))
        lbltitle.pack(padx=10,pady=35)
    
        txt_user = ttk.Entry(self.lblframe_login, width=40, justify="center", font=('arial', 14))
        txt_user.pack(padx=35, pady=10)
        txt_password = ttk.Entry(self.lblframe_login, width=40, justify="center", font=('arial', 14))
        txt_password.pack(padx=35, pady=10)
        txt_password.configure(show='*')
        btn_enter = ttk.Button(self.lblframe_login, text="Ingresar", width=20, command=self.login)
        btn_enter.pack(pady=10, padx=10)

        #Este método es responsable de crear y mostrar la ventana del menú principal de la aplicación. 
        #En este método se dividen y colocan en la interfaz gráfica los diferentes botones que representan 
        #las distintas secciones o funcionalidades de la aplicación, como "Productos", "Ventas", "Clientes", etc. 
        #También se crean y se colocan los marcos (Frame) que contienen estos elementos. 

    def menu_window(self):
        self.frame_left=Frame(self, width=200)
        self.frame_left.grid(row=0, column=0, sticky=NS)
        self.frame_center=Frame(self)
        self.frame_center.grid(row=0, column=1, sticky=NSEW)
        self.frame_right=Frame(self, width=400)
        self.frame_right.grid(row=0, column=2, sticky=NSEW)
        
        btn_productos=ttk.Button(self.frame_left, text='Productos', width=15)
        btn_productos.grid(row=0, column=0, padx=10, pady=10)
        btn_ventas=ttk.Button(self.frame_left, text='Ventas', width=15)
        btn_ventas.grid(row=1, column=0, padx=10, pady=10)
        btn_clientes=ttk.Button(self.frame_left, text='Clientes', width=15)
        btn_clientes.grid(row=2, column=0, padx=10, pady=10)
        btn_compras=ttk.Button(self.frame_left, text='Compras', width=15)
        btn_compras.grid(row=3, column=0, padx=10, pady=10)
        btn_usuarios=ttk.Button(self.frame_left, text='Usuarios', width=15)
        btn_usuarios.grid(row=4, column=0, padx=10, pady=10)
        btn_reportes=ttk.Button(self.frame_left, text='Reportes', width=15)
        btn_reportes.grid(row=5, column=0, padx=10, pady=10)
        btn_backup=ttk.Button(self.frame_left, text='Backup', width=15)
        btn_backup.grid(row=6, column=0, padx=10, pady=10)
        btn_restaurabd=ttk.Button(self.frame_left, text='Restaurar BDD', width=15)
        btn_restaurabd.grid(row=7, column=0, padx=10, pady=10)
        
        
        lbl2=Label(self.frame_center, text='Ventanas')
        lbl2.grid(row=0, column=0, padx=10, pady=10)
        
        lbl3=Label(self.frame_right, text='busquedas')
        lbl3.grid(row=0, column=0, padx=10, pady=10)    

        #Este método se llama cuando se presiona el botón "Ingresar" en la ventana de inicio de sesión. 
        #Su función es ocultar la ventana de inicio de sesión y mostrar la ventana del menú principal. 
        #En otras palabras, este método gestiona la transición de una ventana a otra después de que el 
        #usuario haya iniciado sesión correctamente.

    def login(self):
        self.frame_login.pack_forget()
        self.menu_window()
    
    def user_list_window(self):
        self.frame_user_list=Frame(self.frame_center)
        self.frame_user_list.grid(row=0, column=0, columnspan=2, sticky= NSEW)

        self.lblframe_userlist_btn=LabelFrame(self.frame_user_list)
        self.lblframe_userlist_btn.grid(row=0, column=0, sticky=NSEW)

        btn_new_user=ttk.Button(self.lblframe_userlist_btn, text='Nuevo', width=15)
        btn_new_user.grid(row=0, column=0, padx=5, pady=5)
        btn_modify_user=ttk.Button(self.lblframe_userlist_btn, text='Nuevo', width=15)
        btn_modify_user.grid(row=0, column=0, padx=5, pady=5)
        btn_delete_user=ttk.Button(self.lblframe_userlist_btn, text='Nuevo', width=15)
        btn_delete_user.grid(row=0, column=0, padx=5, pady=5)

#Se define la función main() que crea una instancia de la clase Window y ejecuta el bucle 
#principal de la aplicación.

def main():
    app = Window()
    app.title('Sistema de Ventas')
    app.state('zoomed')
    tb.Style('superhero')
    app.mainloop()

#se utiliza para asegurarse de que el bloque de código que le sigue solo se ejecute cuando el script 
#se está ejecutando directamente como un programa principal, y no cuando se importa como un módulo en otro script
if __name__=='__main__':
    main()