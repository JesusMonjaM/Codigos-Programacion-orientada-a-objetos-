import tkinter as tk
from tkinter import ttk, messagebox

class VentanaInventario:
    def __init__(self, sistema, notebook, completa=True):  # Corregido
        self.sistema = sistema
        self.notebook = notebook
        self.completa = completa
        self.tree_inventario = None

        
    def crear_pestana(self):
        """Crear la pestaña de inventario"""
        # Frame para inventario
        self.inv_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.inv_frame, text="📦 Inventario")
        
        # Frame de botones
        btn_frame = tk.Frame(self.inv_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        if self.completa:
            tk.Button(btn_frame, text="➕ Agregar Llanta", command=self.agregar_llanta, 
                     bg='#27ae60', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            tk.Button(btn_frame, text="✏ Modificar", command=self.modificar_llanta, 
                     bg='#f39c12', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            tk.Button(btn_frame, text="🗑 Eliminar", command=self.eliminar_llanta, 
                     bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🔄 Actualizar", command=self.actualizar_inventario, 
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=5)
        
        # Tabla de inventario
        columns = ("ID", "Marca", "Modelo", "Medida", "Precio", "Stock")
        self.tree_inventario = ttk.Treeview(self.inv_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_inventario.heading(col, text=col)
            self.tree_inventario.column(col, width=120)
        
        # Scrollbar
        scrollbar_inv = ttk.Scrollbar(self.inv_frame, orient='vertical', command=self.tree_inventario.yview)
        self.tree_inventario.configure(yscrollcommand=scrollbar_inv.set)
        
        self.tree_inventario.pack(side='left', fill='both', expand=True, padx=(10,0), pady=10)
        scrollbar_inv.pack(side='right', fill='y', padx=(0,10), pady=10)
        
        self.actualizar_inventario()
    
    def agregar_llanta(self):
        """Abrir ventana para agregar nueva llanta"""
        ventana = VentanaAgregarLlanta(self.sistema, self)
        ventana.crear_ventana()
    
    def modificar_llanta(self):
        """Abrir ventana para modificar llanta seleccionada"""
        seleccion = self.tree_inventario.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una llanta para modificar")
            return
        
        item = self.tree_inventario.item(seleccion[0])
        llanta_id = int(item['values'][0])
        
        # Encontrar la llanta
        llanta = next((item for item in self.sistema.inventario if item["id"] == llanta_id), None)
        if not llanta:
            return
        
        ventana = VentanaModificarLlanta(self.sistema, self, llanta)
        ventana.crear_ventana()
    
    def eliminar_llanta(self):
        """Eliminar llanta seleccionada"""
        seleccion = self.tree_inventario.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una llanta para eliminar")
            return
        
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta llanta?"):
            item = self.tree_inventario.item(seleccion[0])
            llanta_id = int(item['values'][0])
            self.sistema.inventario = [item for item in self.sistema.inventario if item["id"] != llanta_id]
            self.actualizar_inventario()
            messagebox.showinfo("Éxito", "Llanta eliminada correctamente")
    
    def actualizar_inventario(self):
        """Actualizar la tabla de inventario"""
        if not self.tree_inventario:
            return
            
        # Limpiar tabla
        for item in self.tree_inventario.get_children():
            self.tree_inventario.delete(item)
        
        # Llenar con datos
        for llanta in self.sistema.inventario:
            self.tree_inventario.insert('', 'end', values=(
                llanta["id"], llanta["marca"], llanta["modelo"], 
                llanta["medida"], f"${llanta['precio']}", llanta["stock"]
            ))


class VentanaAgregarLlanta:
    def __init__(self, sistema, ventana_inventario):  # Corregido
        self.sistema = sistema
        self.ventana_inventario = ventana_inventario
        
    def crear_ventana(self):
        """Crear ventana para agregar llanta"""
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Agregar Llanta")
        self.ventana.geometry("400x300")
        self.ventana.configure(bg='#ecf0f1')
        
        # Campos
        tk.Label(self.ventana, text="Marca:", bg='#ecf0f1').pack(pady=5)
        self.entry_marca = tk.Entry(self.ventana, width=30)
        self.entry_marca.pack(pady=5)
        
        tk.Label(self.ventana, text="Modelo:", bg='#ecf0f1').pack(pady=5)
        self.entry_modelo = tk.Entry(self.ventana, width=30)
        self.entry_modelo.pack(pady=5)
        
        tk.Label(self.ventana, text="Medida:", bg='#ecf0f1').pack(pady=5)
        self.entry_medida = tk.Entry(self.ventana, width=30)
        self.entry_medida.pack(pady=5)
        
        tk.Label(self.ventana, text="Precio:", bg='#ecf0f1').pack(pady=5)
        self.entry_precio = tk.Entry(self.ventana, width=30)
        self.entry_precio.pack(pady=5)
        
        tk.Label(self.ventana, text="Stock:", bg='#ecf0f1').pack(pady=5)
        self.entry_stock = tk.Entry(self.ventana, width=30)
        self.entry_stock.pack(pady=5)
        
        tk.Button(self.ventana, text="Guardar", command=self.guardar, 
                 bg='#27ae60', fg='white').pack(pady=20)
    
    def guardar(self):
        """Guardar nueva llanta"""
        try:
            nuevo_id = max([item["id"] for item in self.sistema.inventario]) + 1 if self.sistema.inventario else 1
            nueva_llanta = {
                "id": nuevo_id,
                "marca": self.entry_marca.get(),
                "modelo": self.entry_modelo.get(),
                "medida": self.entry_medida.get(),
                "precio": float(self.entry_precio.get()),
                "stock": int(self.entry_stock.get())
            }
            self.sistema.inventario.append(nueva_llanta)
            self.ventana_inventario.actualizar_inventario()
            self.ventana.destroy()
            messagebox.showinfo("Éxito", "Llanta agregada correctamente")
        except ValueError:
            messagebox.showerror("Error", "Precio y stock deben ser números")


class VentanaModificarLlanta:
    def __init__(self, sistema, ventana_inventario, llanta):  # Corregido
        self.sistema = sistema
        self.ventana_inventario = ventana_inventario
        self.llanta = llanta
        
    def crear_ventana(self):
        """Crear ventana para modificar llanta"""
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Modificar Llanta")
        self.ventana.geometry("400x300")
        self.ventana.configure(bg='#ecf0f1')
        
        # Campos pre-llenados
        tk.Label(self.ventana, text="Marca:", bg='#ecf0f1').pack(pady=5)
        self.entry_marca = tk.Entry(self.ventana, width=30)
        self.entry_marca.pack(pady=5)
        self.entry_marca.insert(0, self.llanta["marca"])
        
        tk.Label(self.ventana, text="Modelo:", bg='#ecf0f1').pack(pady=5)
        self.entry_modelo = tk.Entry(self.ventana, width=30)
        self.entry_modelo.pack(pady=5)
        self.entry_modelo.insert(0, self.llanta["modelo"])
        
        tk.Label(self.ventana, text="Medida:", bg='#ecf0f1').pack(pady=5)
        self.entry_medida = tk.Entry(self.ventana, width=30)
        self.entry_medida.pack(pady=5)
        self.entry_medida.insert(0, self.llanta["medida"])
        
        tk.Label(self.ventana, text="Precio:", bg='#ecf0f1').pack(pady=5)
        self.entry_precio = tk.Entry(self.ventana, width=30)
        self.entry_precio.pack(pady=5)
        self.entry_precio.insert(0, str(self.llanta["precio"]))
        
        tk.Label(self.ventana, text="Stock:", bg='#ecf0f1').pack(pady=5)
        self.entry_stock = tk.Entry(self.ventana, width=30)
        self.entry_stock.pack(pady=5)
        self.entry_stock.insert(0, str(self.llanta["stock"]))
        
        tk.Button(self.ventana, text="Guardar Cambios", command=self.guardar, 
                 bg='#f39c12', fg='white').pack(pady=20)
    
    def guardar(self):
        """Guardar cambios en la llanta"""
        try:
            self.llanta["marca"] = self.entry_marca.get()
            self.llanta["modelo"] = self.entry_modelo.get()
            self.llanta["medida"] = self.entry_medida.get()
            self.llanta["precio"] = float(self.entry_precio.get())
            self.llanta["stock"] = int(self.entry_stock.get())
            self.ventana_inventario.actualizar_inventario()
            self.ventana.destroy()
            messagebox.showinfo("Éxito", "Llanta modificada correctamente")
        except ValueError:
            messagebox.showerror("Error", "Precio y stock deben ser números")

