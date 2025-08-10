import tkinter as tk
from tkinter import ttk, messagebox

class VentanaEmpleados:
    def __init__(self, sistema, notebook):
        self.sistema = sistema
        self.notebook = notebook
        self.tree_empleados = None
        
    def crear_pestana(self):
        """Crear la pestaña de empleados"""
        # Frame para empleados
        self.emp_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.emp_frame, text="👨‍💼 Empleados")
        
        # Frame de botones
        btn_frame = tk.Frame(self.emp_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        # Solo mostrar botones de gestión si es admin
        if self.sistema.role_actual == "admin":
            tk.Button(btn_frame, text="➕ Agregar Usuario", command=self.agregar_usuario, 
                     bg='#27ae60', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            tk.Button(btn_frame, text="✏ Modificar", command=self.modificar_usuario, 
                     bg='#f39c12', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            tk.Button(btn_frame, text="🗑 Eliminar", command=self.eliminar_usuario, 
                     bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🔄 Actualizar", command=self.actualizar_empleados, 
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=5)
        
        # Tabla de empleados
        columns = ("Usuario", "Rol", "Estado")
        self.tree_empleados = ttk.Treeview(self.emp_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_empleados.heading(col, text=col)
            self.tree_empleados.column(col, width=150)
        
        scrollbar_empleados = ttk.Scrollbar(self.emp_frame, orient='vertical', command=self.tree_empleados.yview)
        self.tree_empleados.configure(yscrollcommand=scrollbar_empleados.set)
        
        self.tree_empleados.pack(side='left', fill='both', expand=True, padx=(10,0), pady=10)
        scrollbar_empleados.pack(side='right', fill='y', padx=(0,10), pady=10)
        
        self.actualizar_empleados()
    
    def agregar_usuario(self):
        """Abrir ventana para agregar usuario"""
        self.ventana_agregar = tk.Toplevel(self.sistema.root)
        self.ventana_agregar.title("Agregar Usuario")
        self.ventana_agregar.geometry("400x300")
        self.ventana_agregar.resizable(False, False)
        self.ventana_agregar.configure(bg='#ecf0f1')
        
        # Campos del formulario
        tk.Label(self.ventana_agregar, text="Nombre de usuario:", bg='#ecf0f1').pack(pady=5)
        self.entry_usuario = tk.Entry(self.ventana_agregar, width=30)
        self.entry_usuario.pack(pady=5)
        
        tk.Label(self.ventana_agregar, text="Contraseña:", bg='#ecf0f1').pack(pady=5)
        self.entry_password = tk.Entry(self.ventana_agregar, width=30, show='*')
        self.entry_password.pack(pady=5)
        
        tk.Label(self.ventana_agregar, text="Tipo de usuario:", bg='#ecf0f1').pack(pady=5)
        
        self.tipo_usuario = tk.StringVar(value="vendedor")
        frame_tipo = tk.Frame(self.ventana_agregar, bg='#ecf0f1')
        frame_tipo.pack()
        
        tk.Radiobutton(frame_tipo, text="Vendedor", variable=self.tipo_usuario, 
                      value="vendedor", bg='#ecf0f1').pack(side='left', padx=10)
        tk.Radiobutton(frame_tipo, text="Almacenista", variable=self.tipo_usuario, 
                      value="almacenista", bg='#ecf0f1').pack(side='left', padx=10)
        
        # Botón guardar
        tk.Button(self.ventana_agregar, text="Guardar", command=self.guardar_usuario,
                 bg='#27ae60', fg='white').pack(pady=20)
    
    def guardar_usuario(self):
        """Guardar nuevo usuario"""
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()
        role = self.tipo_usuario.get()
        
        if not usuario or not password:
            messagebox.showerror("Error", "Todos los campos son obligatorios", parent=self.ventana_agregar)
            return
            
        if usuario in self.sistema.usuarios:
            messagebox.showerror("Error", "El usuario ya existe", parent=self.ventana_agregar)
            return
            
        # Agregar usuario al sistema
        self.sistema.usuarios[usuario] = {
            "password": password,
            "role": role
        }
        
        messagebox.showinfo("Éxito", "Usuario agregado correctamente", parent=self.ventana_agregar)
        self.ventana_agregar.destroy()
        self.actualizar_empleados()
    
    def modificar_usuario(self):
        """Abrir ventana para modificar usuario"""
        seleccion = self.tree_empleados.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para modificar")
            return
            
        usuario = self.tree_empleados.item(seleccion[0])['values'][0]
        
        if usuario == "admin":
            messagebox.showerror("Error", "No se puede modificar el usuario admin")
            return
            
        datos_usuario = self.sistema.usuarios[usuario]
        
        self.ventana_modificar = tk.Toplevel(self.sistema.root)
        self.ventana_modificar.title("Modificar Usuario")
        self.ventana_modificar.geometry("400x300")
        self.ventana_modificar.resizable(False, False)
        self.ventana_modificar.configure(bg='#ecf0f1')
        
        # Campos del formulario
        tk.Label(self.ventana_modificar, text=f"Usuario: {usuario}", bg='#ecf0f1', 
                font=('Arial', 10, 'bold')).pack(pady=10)
        
        tk.Label(self.ventana_modificar, text="Nueva contraseña:", bg='#ecf0f1').pack(pady=5)
        self.entry_new_pass = tk.Entry(self.ventana_modificar, width=30, show='*')
        self.entry_new_pass.pack(pady=5)
        
        tk.Label(self.ventana_modificar, text="Tipo de usuario:", bg='#ecf0f1').pack(pady=5)
        
        self.tipo_usuario_mod = tk.StringVar(value=datos_usuario['role'])
        frame_tipo = tk.Frame(self.ventana_modificar, bg='#ecf0f1')
        frame_tipo.pack()
        
        tk.Radiobutton(frame_tipo, text="Vendedor", variable=self.tipo_usuario_mod, 
                      value="vendedor", bg='#ecf0f1').pack(side='left', padx=10)
        tk.Radiobutton(frame_tipo, text="Almacenista", variable=self.tipo_usuario_mod, 
                      value="almacenista", bg='#ecf0f1').pack(side='left', padx=10)
        
        # Botón guardar
        tk.Button(self.ventana_modificar, text="Guardar Cambios", 
                 command=lambda: self.guardar_modificacion(usuario),
                 bg='#f39c12', fg='white').pack(pady=20)
    
    def guardar_modificacion(self, usuario):
        """Guardar cambios en el usuario"""
        nueva_password = self.entry_new_pass.get().strip()
        nuevo_role = self.tipo_usuario_mod.get()
        
        if not nueva_password:
            messagebox.showerror("Error", "La contraseña no puede estar vacía", parent=self.ventana_modificar)
            return
            
        # Actualizar usuario
        self.sistema.usuarios[usuario] = {
            "password": nueva_password,
            "role": nuevo_role
        }
        
        messagebox.showinfo("Éxito", "Usuario modificado correctamente", parent=self.ventana_modificar)
        self.ventana_modificar.destroy()
        self.actualizar_empleados()
    
    def eliminar_usuario(self):
        """Eliminar usuario seleccionado"""
        seleccion = self.tree_empleados.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar")
            return
            
        usuario = self.tree_empleados.item(seleccion[0])['values'][0]
        
        if usuario == "admin":
            messagebox.showerror("Error", "No se puede eliminar el usuario admin")
            return
            
        if usuario == self.sistema.usuario_actual:
            messagebox.showerror("Error", "No puede eliminarse a sí mismo")
            return
            
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar al usuario {usuario}?"):
            del self.sistema.usuarios[usuario]
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
            self.actualizar_empleados()
    
    def actualizar_empleados(self):
        """Actualizar la tabla de empleados"""
        if not self.tree_empleados:
            return
            
        # Limpiar tabla
        for item in self.tree_empleados.get_children():
            self.tree_empleados.delete(item)
        
        # Llenar con datos
        for usuario, datos in self.sistema.usuarios.items():
            estado = "Conectado" if usuario == self.sistema.usuario_actual else "Desconectado"
            self.tree_empleados.insert('', 'end', values=(
                usuario, 
                datos['role'].capitalize(), 
                estado
            ))