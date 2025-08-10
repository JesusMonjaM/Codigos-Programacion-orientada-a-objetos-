import tkinter as tk
from tkinter import ttk, messagebox

class VentanaClientes:
    def __init__(self, sistema, notebook):  # Corregido
        self.sistema = sistema
        self.notebook = notebook
        self.tree_clientes = None
        
    def crear_pestana(self):
        """Crear la pestaña de clientes"""
        # Frame para clientes
        self.clientes_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.clientes_frame, text="👥 Clientes")
        
        # Frame de botones
        btn_frame = tk.Frame(self.clientes_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Button(btn_frame, text="➕ Agregar Cliente", command=self.agregar_cliente, 
                 bg='#27ae60', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="✏ Modificar", command=self.modificar_cliente, 
                 bg='#f39c12', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="🔄 Actualizar", command=self.actualizar_clientes, 
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=5)
        
        # Tabla de clientes
        columns = ("ID", "Nombre", "Teléfono", "Email")
        self.tree_clientes = ttk.Treeview(self.clientes_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_clientes.heading(col, text=col)
            self.tree_clientes.column(col, width=150)
        
        scrollbar_clientes = ttk.Scrollbar(self.clientes_frame, orient='vertical', command=self.tree_clientes.yview)
        self.tree_clientes.configure(yscrollcommand=scrollbar_clientes.set)
        
        self.tree_clientes.pack(side='left', fill='both', expand=True, padx=(10,0), pady=10)
        scrollbar_clientes.pack(side='right', fill='y', padx=(0,10), pady=10)
        
        self.actualizar_clientes()
    
    def agregar_cliente(self):
        """Abrir ventana para agregar cliente"""
        ventana = VentanaAgregarCliente(self.sistema, self)
        ventana.crear_ventana()
    
    def modificar_cliente(self):
        """Abrir ventana para modificar cliente"""
        seleccion = self.tree_clientes.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un cliente para modificar")
            return
        
        item = self.tree_clientes.item(seleccion[0])
        cliente_id = int(item['values'][0])
        
        # Encontrar el cliente
        cliente = next((c for c in self.sistema.clientes if c["id"] == cliente_id), None)
        if not cliente:
            return
        
        ventana = VentanaModificarCliente(self.sistema, self, cliente)
        ventana.crear_ventana()
    
    def actualizar_clientes(self):
        """Actualizar la tabla de clientes"""
        if not self.tree_clientes:
            return
            
        # Limpiar tabla
        for item in self.tree_clientes.get_children():
            self.tree_clientes.delete(item)
        
        # Llenar con datos
        for cliente in self.sistema.clientes:
            self.tree_clientes.insert('', 'end', values=(
                cliente["id"], cliente["nombre"], cliente["telefono"], cliente["email"]
            ))


class VentanaAgregarCliente:
    def __init__(self, sistema, ventana_clientes):  # Corregido
        self.sistema = sistema
        self.ventana_clientes = ventana_clientes
        
    def crear_ventana(self):
        """Crear ventana para agregar cliente"""
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Agregar Cliente")
        self.ventana.geometry("400x250")
        self.ventana.configure(bg='#ecf0f1')
        
        tk.Label(self.ventana, text="Nombre:", bg='#ecf0f1').pack(pady=5)
        self.entry_nombre = tk.Entry(self.ventana, width=30)
        self.entry_nombre.pack(pady=5)
        
        tk.Label(self.ventana, text="Teléfono:", bg='#ecf0f1').pack(pady=5)
        self.entry_telefono = tk.Entry(self.ventana, width=30)
        self.entry_telefono.pack(pady=5)
        
        tk.Label(self.ventana, text="Email:", bg='#ecf0f1').pack(pady=5)
        self.entry_email = tk.Entry(self.ventana, width=30)
        self.entry_email.pack(pady=5)
        
        tk.Button(self.ventana, text="Guardar", command=self.guardar, 
                 bg='#27ae60', fg='white').pack(pady=20)
    
    def guardar(self):
        """Guardar nuevo cliente"""
        if not self.entry_nombre.get():
            messagebox.showerror("Error", "El nombre es obligatorio")
            return
        
        nuevo_id = max([c["id"] for c in self.sistema.clientes]) + 1 if self.sistema.clientes else 1
        nuevo_cliente = {
            "id": nuevo_id,
            "nombre": self.entry_nombre.get(),
            "telefono": self.entry_telefono.get(),
            "email": self.entry_email.get()
        }
        self.sistema.clientes.append(nuevo_cliente)
        self.ventana_clientes.actualizar_clientes()
        self.ventana.destroy()
        messagebox.showinfo("Éxito", "Cliente agregado correctamente")


class VentanaModificarCliente:
    def __init__(self, sistema, ventana_clientes, cliente):  # Corregido
        self.sistema = sistema
        self.ventana_clientes = ventana_clientes
        self.cliente = cliente
        
    def crear_ventana(self):
        """Crear ventana para modificar cliente"""
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Modificar Cliente")
        self.ventana.geometry("400x250")
        self.ventana.configure(bg='#ecf0f1')
        
        tk.Label(self.ventana, text="Nombre:", bg='#ecf0f1').pack(pady=5)
        self.entry_nombre = tk.Entry(self.ventana, width=30)
        self.entry_nombre.pack(pady=5)
        self.entry_nombre.insert(0, self.cliente["nombre"])
        
        tk.Label(self.ventana, text="Teléfono:", bg='#ecf0f1').pack(pady=5)
        self.entry_telefono = tk.Entry(self.ventana, width=30)
        self.entry_telefono.pack(pady=5)
        self.entry_telefono.insert(0, self.cliente["telefono"])
        
        tk.Label(self.ventana, text="Email:", bg='#ecf0f1').pack(pady=5)
        self.entry_email = tk.Entry(self.ventana, width=30)
        self.entry_email.pack(pady=5)
        self.entry_email.insert(0, self.cliente["email"])
        
        tk.Button(self.ventana, text="Guardar Cambios", command=self.guardar, 
                 bg='#f39c12', fg='white').pack(pady=20)
    
    def guardar(self):
        """Guardar cambios en el cliente"""
        if not self.entry_nombre.get():
            messagebox.showerror("Error", "El nombre es obligatorio")
            return
        
        self.cliente["nombre"] = self.entry_nombre.get()
        self.cliente["telefono"] = self.entry_telefono.get()
        self.cliente["email"] = self.entry_email.get()
        self.ventana_clientes.actualizar_clientes()
        self.ventana.destroy()
        messagebox.showinfo("Éxito", "Cliente modificado correctamente")