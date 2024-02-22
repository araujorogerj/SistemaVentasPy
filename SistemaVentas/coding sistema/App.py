from cProfile import label
from tkinter import END, NS, NSEW, W, Entry, Scrollbar, Tk, Frame, Button, Label, LabelFrame, Toplevel, ttk, messagebox
import ttkbootstrap as tb
import sqlite3


# Se define la clase Window que hereda de Tk (ventana principal de tkinter). En el método __init__,
# se inicializa la ventana con un título y se llama al método login_window() para crear la ventana
# de inicio de sesión.

class Window(tb.Window):
    def __init__(self):
        super().__init__()
        self.login_window()

    # Este método crea la ventana de inicio de sesión. Se crea un Frame dentro de la ventana principal,
    # se configura para que se expanda a toda la ventana (self.state('zoomed')) y se establece un color
    # de fondo.

    def login_window(self):
        self.frame_login = Frame(self)
        self.frame_login.pack(pady=200)

        # Se crea un LabelFrame dentro del Frame principal con un título y colores personalizados. Luego,
        # se configuran el peso de la fila y columna principal para que el LabelFrame se expanda y se centre
        # en la ventana.

        self.lblframe_login = tb.LabelFrame(
            self.frame_login, text="Acceso", bootstyle='success')
        self.lblframe_login.pack(padx=40, pady=10)

        # Se crean un Label con el texto "Inicio de sesión", un campo de entrada (Entry) y un botón
        # dentro del LabelFrame.
        lbltitle = tb.Label(self.lblframe_login, text="Inicio de sesion", font=(
            'Arial', 18), bootstyle='success')
        lbltitle.pack(padx=10, pady=35)

        self.txt_user = tb.Entry(self.lblframe_login, width=40, justify="center", font=(
            'arial', 14), bootstyle='success')
        self.txt_user.pack(padx=35, pady=10)
        self.txt_password = tb.Entry(self.lblframe_login, width=40, justify="center", font=(
            'arial', 14), bootstyle='success')
        self.txt_password.pack(padx=35, pady=10)
        self.txt_password.configure(show='*')
        btn_enter = tb.Button(self.lblframe_login, text="Ingresar",
                              width=20, command=self.login, bootstyle='success')
        btn_enter.pack(pady=10, padx=10)
        
        self.txt_user.focus()

        # Este método es responsable de crear y mostrar la ventana del menú principal de la aplicación.
        # En este método se dividen y colocan en la interfaz gráfica los diferentes botones que representan
        # las distintas secciones o funcionalidades de la aplicación, como "Productos", "Ventas", "Clientes", etc.
        # También se crean y se colocan los marcos (Frame) que contienen estos elementos.

    def menu_window(self):
        self.frame_left = Frame(self, width=200)
        self.frame_left.grid(row=0, column=0, sticky=NS)
        self.frame_center = Frame(self)
        self.frame_center.grid(row=0, column=1, sticky=NSEW)
        self.frame_right = Frame(self, width=400)
        self.frame_right.grid(row=0, column=2, sticky=NSEW)

        btn_productos = ttk.Button(self.frame_left, text='Productos', width=15)
        btn_productos.grid(row=0, column=0, padx=10, pady=10)
        btn_ventas = ttk.Button(self.frame_left, text='Ventas', width=15)
        btn_ventas.grid(row=1, column=0, padx=10, pady=10)
        btn_clientes = ttk.Button(self.frame_left, text='Clientes', width=15)
        btn_clientes.grid(row=2, column=0, padx=10, pady=10)
        btn_compras = ttk.Button(self.frame_left, text='Compras', width=15)
        btn_compras.grid(row=3, column=0, padx=10, pady=10)
        btn_usuarios = ttk.Button(
            self.frame_left, text='Usuarios', width=15, command=self.user_list_window)
        btn_usuarios.grid(row=4, column=0, padx=10, pady=10)
        btn_reportes = ttk.Button(self.frame_left, text='Reportes', width=15)
        btn_reportes.grid(row=5, column=0, padx=10, pady=10)
        btn_backup = ttk.Button(self.frame_left, text='Backup', width=15)
        btn_backup.grid(row=6, column=0, padx=10, pady=10)
        btn_restaurabd = ttk.Button(
            self.frame_left, text='Restaurar BDD', width=15)
        btn_restaurabd.grid(row=7, column=0, padx=10, pady=10)

        lbl2 = Label(self.frame_center, text='Ventanas')
        lbl2.grid(row=0, column=0, padx=10, pady=10)

        lbl3 = Label(self.frame_right, text='busquedas')
        lbl3.grid(row=0, column=0, padx=10, pady=10)

        # Este método se llama cuando se presiona el botón "Ingresar" en la ventana de inicio de sesión.
        # Su función es ocultar la ventana de inicio de sesión y mostrar la ventana del menú principal.
        # En otras palabras, este método gestiona la transición de una ventana a otra después de que el
        # usuario haya iniciado sesión correctamente.

    def login(self):
        # Try & catch errores
        try:
            # Establece conexion con base de datos
            connection = sqlite3.connect('Ventas.db')
            # Creacion del cursor
            cursor = connection.cursor()

            user_name = self.txt_user.get()
            user_password = self.txt_password.get()
            # Consultar la base de datos
            cursor.execute(
                "SELECT * FROM Usuarios WHERE Nombre=? AND Clave=?", (user_name, user_password))
            # Traer registros y guardar en la expresion datas
            datos_login = cursor.fetchall()
            if datos_login != "":
                for row in datos_login:
                    user_cod = row[0]
                    user_nam = row[1]
                    user_psw = row[2]
                    user_rol = row[3]
                if (user_nam == self.txt_user.get() and user_psw == self.txt_password.get()):
                    self.frame_login.pack_forget()
                    self.menu_window()

            # Guardar cambios
            connection.commit()
            # Cerrar conexión
            connection.close()

        except:
            messagebox.showerror(
                "Error de Acceso", f"Usuario o clave inválidos:")

    def user_list_window(self):
        self.frame_user_list = Frame(self.frame_center)
        self.frame_user_list.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_userlist_btn = LabelFrame(self.frame_user_list)
        self.lblframe_userlist_btn.grid(
            row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_new_user = ttk.Button(self.lblframe_userlist_btn, text='Nuevo Usuario', width=15,
                                  bootstyle='primary', command=self.new_user_window)
        btn_new_user.grid(row=0, column=0, padx=5, pady=5)
        btn_modify_user = ttk.Button(
            self.lblframe_userlist_btn, text='Modificar Usuario', width=15, bootstyle='warning', command=self.modify_user_window)
        btn_modify_user.grid(row=0, column=1, padx=5, pady=5)
        btn_delete_user = ttk.Button(
            self.lblframe_userlist_btn, text='Eliminar Usuario', width=15, bootstyle='danger', command=self.delete_user)
        btn_delete_user.grid(row=0, column=2, padx=5, pady=5)

        self.lblframe_searchuser = LabelFrame(self.frame_user_list)
        self.lblframe_searchuser.grid(
            row=1, column=0, padx=10, pady=10, sticky=NSEW)

        self.txt_search_user = ttk.Entry(self.lblframe_searchuser, width=50)
        self.txt_search_user.grid(row=0, column=0, padx=5, pady=5)
        self.txt_search_user.bind('<Key>', self.search_user)

        # VISTA USUARIOS CON TREEVIEW

        self.lblframe_tree_userlist = LabelFrame(self.frame_user_list)
        self.lblframe_tree_userlist.grid(
            row=2, column=0, padx=10, pady=10, sticky=NSEW)

        columns = ("Codigo", "Nombre", "Clave", "Rol")

        self.tree_user_list = ttk.Treeview(self.lblframe_tree_userlist, columns=columns,
                                           height=17, show='headings', bootstyle='dark')
        self.tree_user_list.grid(row=0, column=0)

        self.tree_user_list.heading("Codigo", text="Codigo", anchor=W)
        self.tree_user_list.heading("Nombre", text="Nombre", anchor=W)
        self.tree_user_list.heading("Clave", text="Clave", anchor=W)
        self.tree_user_list.heading("Rol", text="Rol", anchor=W)
        self.tree_user_list['displaycolumns'] = ("Codigo", "Nombre", "Rol")

        # Scrollbar
        tree_scroll_userlist = tb.Scrollbar(
            self.frame_user_list, bootstyle='round-primary')
        tree_scroll_userlist.grid(row=2, column=1)
        # Funcionamiento Scrollbar
        tree_scroll_userlist.config(command=self.tree_user_list.yview)
    

        # Llamar la funcion de mostrar los usuarios de la DB

        self.search_user('')
        self.txt_search_user.focus()
        

    def search_user(self, event):
        # Try & catch errores
        try:
            # Establece conexion con base de datos
            connection = sqlite3.connect('Ventas.db')
            # Creacion del cursor
            cursor = connection.cursor()
            # limpiar el treeview con los usuarios
            data = self.tree_user_list.get_children()
            # Escanear cada registro
            for elements in data:
                self.tree_user_list.delete(elements)
            # Consultar la base de datos
            cursor.execute("SELECT * FROM Usuarios WHERE Nombre LIKE ?", (self.txt_search_user.get()+'%',))
            # Traer registros y guardar en la expresion datas
            datos = cursor.fetchall()
            # Consultar cada fila
            for row in datos:
                # rellenar la tabla del treeview con los datos encontrados
                self.tree_user_list.insert(
                    "", 0, text=row[0], values=(row[0], row[1], row[2], row[3]))
            # Guardar cambios
            connection.commit()
            # Cerrar conexión
            connection.close()

        # Mensaje en caso de tener un error, y especificar el error como tal
        except sqlite3.Error as error:
            messagebox.showerror("Error de conexión a la base de datos",
                                 f"Ocurrió un error al conectarse a la base de datos: {error}")

    def new_user_window(self):
        self.frame_new_user = Toplevel(self)
        self.frame_new_user.title('Nuevo Usuario')
        self.center_window_new_user(250, 350)
        self.frame_new_user.resizable(0, 0)
        # No permite ninguna accion hasta el cierre de la nueva vetana
        self.frame_new_user.grab_set()

        lblframe_new_user = LabelFrame(self.frame_new_user)
        lblframe_new_user.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

        lbl_new_user_cod = Label(lblframe_new_user, text='Código')
        lbl_new_user_cod.grid(row=0, column=0, padx=10, pady=10)
        self.txt_new_user_cod = Entry(lblframe_new_user, width=40)
        self.txt_new_user_cod.grid(row=0, column=1, padx=10, pady=10)

        lbl_new_user_name = Label(lblframe_new_user, text='Nombre')
        lbl_new_user_name.grid(row=1, column=0, padx=10, pady=10)
        self.txt_new_user_name = Entry(lblframe_new_user, width=40)
        self.txt_new_user_name.grid(row=1, column=1, padx=10, pady=10)

        lbl_new_user_psw = Label(lblframe_new_user, text='Clave')
        lbl_new_user_psw.grid(row=2, column=0, padx=10, pady=10)
        self.txt_new_user_psw = Entry(lblframe_new_user, width=40)
        self.txt_new_user_psw.grid(row=2, column=1, padx=10, pady=10)
        self.txt_new_user_psw.config(show='*')

        lbl_new_user_rol = Label(lblframe_new_user, text='Rol')
        lbl_new_user_rol.grid(row=3, column=0, padx=10, pady=10)
        self.txt_new_user_rol = ttk.Combobox(
            lblframe_new_user, values=('Admin', 'Vendedor',), width=37)
        self.txt_new_user_rol.grid(row=3, column=1, padx=10, pady=10)
        self.txt_new_user_rol.current(0)

        btn_save_new_user = ttk.Button(
            lblframe_new_user, text='Guardar', width=37, command=self.save_user)
        btn_save_new_user.grid(row=4, column=1, padx=10, pady=10)

    def save_user(self):
        # Try & catch errores
        try:

            new_user_data = self.txt_new_user_cod.get(), self.txt_new_user_name.get(
            ), self.txt_new_user_psw.get(), self.txt_new_user_rol.get()
            # Establece conexion con base de datos
            connection = sqlite3.connect('Ventas.db')
            # Creacion del cursor
            cursor = connection.cursor()
            # Consultar la base de datos
            cursor.execute(
                "INSERT INTO Usuarios VALUES(?,?,?,?)", (new_user_data))
            # Mensaje
            messagebox.showinfo('Guardado de usuarios',
                                'Usuario guardado correctamente')
            # Guardar cambios
            connection.commit()
            # Cerrar conexión
            connection.close()
            # Cerrar ventana
            self.frame_new_user.destroy()
            

        except:
            messagebox.showerror(
                "Error de Guardado de usuarios", f"Ocurrió un error al guardar su usuario")

    def modify_user_window(self):

        self.selected_user = self.tree_user_list.focus()
        self.value_selected_user = self.tree_user_list.item(
            self.selected_user, 'values')

        if self.value_selected_user != '':

            self.frame_mod_user = Toplevel(self)
        self.frame_mod_user.title('Modificar Usuario')
        self.center_window_modify_user(250, 350)
        self.frame_mod_user.resizable(0, 0)
        # No permite ninguna accion hasta el cierre de la nueva vetana
        self.frame_mod_user.grab_set()

        lblframe_mod_user = LabelFrame(self.frame_mod_user)
        lblframe_mod_user.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

        lbl_mod_user_cod = Label(lblframe_mod_user, text='Código')
        lbl_mod_user_cod.grid(row=0, column=0, padx=10, pady=10)
        self.txt_mod_user_cod = Entry(lblframe_mod_user, width=40)
        self.txt_mod_user_cod.grid(row=0, column=1, padx=10, pady=10)

        lbl_mod_user_name = Label(lblframe_mod_user, text='Nombre')
        lbl_mod_user_name.grid(row=1, column=0, padx=10, pady=10)
        self.txt_mod_user_name = Entry(lblframe_mod_user, width=40)
        self.txt_mod_user_name.grid(row=1, column=1, padx=10, pady=10)

        lbl_mod_user_psw = Label(lblframe_mod_user, text='Clave')
        lbl_mod_user_psw.grid(row=2, column=0, padx=10, pady=10)
        self.txt_mod_user_psw = Entry(lblframe_mod_user, width=40)
        self.txt_mod_user_psw.grid(row=2, column=1, padx=10, pady=10)
        self.txt_mod_user_psw.config(show='*')

        lbl_mod_user_rol = Label(lblframe_mod_user, text='Rol')
        lbl_mod_user_rol.grid(row=3, column=0, padx=10, pady=10)
        self.txt_mod_user_rol = ttk.Combobox(
            lblframe_mod_user, values=('Admin', 'Vendedor',), width=37)
        self.txt_mod_user_rol.grid(row=3, column=1, padx=10, pady=10)
        self.txt_mod_user_rol.current(0)

        btn_save_mod_user = ttk.Button(
            lblframe_mod_user, text='Modificar', width=37, bootstyle='warning', command=self.modify_user)
        btn_save_mod_user.grid(row=4, column=1, padx=10, pady=10)

        self.fill_entry_modify_user()

    def fill_entry_modify_user(self):
        self.txt_mod_user_cod.delete(0, END)
        self.txt_mod_user_name.delete(0, END)
        self.txt_mod_user_psw.delete(0, END)
        self.txt_mod_user_rol.delete(0, END)

        self.txt_mod_user_cod.insert(0, self.value_selected_user[0])
        self.txt_mod_user_cod.config(state='readonly')
        self.txt_mod_user_name.insert(0, self.value_selected_user[1])
        self.txt_mod_user_psw.insert(0, self.value_selected_user[2])
        self.txt_mod_user_rol.insert(0, self.value_selected_user[3])
        self.txt_mod_user_rol.config(state='readonly')

    def modify_user(self):

        if (self.txt_mod_user_cod.get() == '' or self.txt_mod_user_name.get() == '' or
                self.txt_mod_user_psw.get() == '' or self.txt_mod_user_rol.get() == ''):
            messagebox.showerror('Modificar Usuario',
                                 'Favor rellenar todos los campos')
            return
        # Try & catch errores
        try:
            # Establece conexion con base de datos
            connection = sqlite3.connect('Ventas.db')
            # Creacion del cursor
            cursor = connection.cursor()
            # Modificar datos
            modify_user_data = (self.txt_mod_user_name.get(),
                                self.txt_mod_user_psw.get(), self.txt_mod_user_rol.get())
            # Consultar la base de datos
            cursor.execute(
                "UPDATE Usuarios SET Nombre=?, Clave=?, Rol=? WHERE Codigo=" +
                self.txt_mod_user_cod.get(), (modify_user_data))
            # Mensaje
            messagebox.showinfo('Guardado de usuarios',
                                'Modificación completa')
            # Guardar cambios
            connection.commit()
            # agregando variables
            self.value_selected_user = self.tree_user_list.item(self.user_selected, text='',
                                                                values=(self.txt_mod_user_cod.get(), self.txt_mod_user_name.get(),
                                                                        self.txt_mod_user_psw.get(), self.txt_mod_user_rol.get()))
            # Cerrar ventana
            self.frame_mod_user.destroy()
            # Cerrar conexión
            connection.close()

        except sqlite3.Error as error:
            messagebox.showerror(
                "Error de modificación de usuarios", f"Ocurrió un error al modificar su usuario: {error}")

    def delete_user(self):
            selected_user_delete=self.tree_user_list.focus()
            value_user_selected_delete=self.tree_user_list.item(selected_user_delete, 'values')

            if value_user_selected_delete!='':
                response=messagebox.askquestion('Eliminar usuario', '¿Está seguro que desea eliminar el usuario seleccionado?')
                if response == 'yes':
                    #Conexion a la BD
                    connection=sqlite3.connect('Ventas.db')
                    #Crear Cursosr
                    cursor=connection.cursor()
                    #Crear Consulta
                    cursor.execute('DELETE FROM Usuarios WHERE Codigo='+ str(value_user_selected_delete[0]))
                    #aplicar cambios
                    connection.commit()
                    messagebox.showinfo('Eliminar Usuario', 'Usuario eliminaro exitosamente')
                    self.search_user()
                    #cerrar conexion
                    connection.close()
                else:
                    messagebox.showinfo('Eliminar Usuario', 'Proceso cancelado')
            
    def center_window_new_user(self, width, height):
        window_height=height
        window_width=width
        
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        
        x_cord=int((screen_width/2) - (window_width/2))
        y_cord=int((screen_height/2) - (window_height/2))
        
        self.frame_new_user.geometry('{}x{}+{}+{}'.format(window_height, window_width, x_cord, y_cord))
   
    def center_window_modify_user(self, width, height):
        window_height=height
        window_width=width
        
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        
        x_cord=int((screen_width/2) - (window_width/2))
        y_cord=int((screen_height/2) - (window_height/2))
        
        self.frame_mod_user.geometry('{}x{}+{}+{}'.format(window_height, window_width, x_cord, y_cord)) 
# Se define la función main() que crea una instancia de la clase Window y ejecuta el bucle
# principal de la aplicación.


def main():
    app = Window()
    app.title('Sistema de Ventas')
    app.state('zoomed')
    tb.Style('superhero')
    app.mainloop()


# esta condiconal se utiliza para asegurarse de que el bloque de código que le sigue solo se ejecute cuando el script
# se está ejecutando directamente como un programa principal, y no cuando se importa como un módulo en otro script
if __name__ == '__main__':
    main()