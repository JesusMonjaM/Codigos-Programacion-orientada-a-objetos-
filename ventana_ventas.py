import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class VentanaVentas:
    def __init__(self, sistema, notebook):  # Corregido
        self.sistema = sistema
        self.notebook = notebook
        self.tree_ventas = None
        
    def crear_pestana(self):
        """Crear la pestaña de ventas"""
        # Frame para ventas
        self.ventas_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.ventas_frame, text="💰 Ventas")
        
        # Frame de botones
        btn_frame = tk.Frame(self.ventas_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Button(btn_frame, text="🛒 Nueva Venta", command=self.nueva_venta, 
                 bg='#27ae60', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="🔄 Actualizar", command=self.actualizar_ventas, 
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=5)
        
        # Tabla de ventas
        columns = ("ID", "Cliente", "Producto", "Cantidad", "Total", "Fecha", "Vendedor")
        self.tree_ventas = ttk.Treeview(self.ventas_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_ventas.heading(col, text=col)
            self.tree_ventas.column(col, width=100)
        
        scrollbar_ventas = ttk.Scrollbar(self.ventas_frame, orient='vertical', command=self.tree_ventas.yview)
        self.tree_ventas.configure(yscrollcommand=scrollbar_ventas.set)
        
        self.tree_ventas.pack(side='left', fill='both', expand=True, padx=(10,0), pady=10)
        scrollbar_ventas.pack(side='right', fill='y', padx=(0,10), pady=10)
        
        self.actualizar_ventas()
    
    def nueva_venta(self):
        """Abrir ventana para nueva venta"""
        if not self.sistema.inventario:
            messagebox.showwarning("Advertencia", "No hay productos en inventario")
            return
        
        if not self.sistema.clientes:
            messagebox.showwarning("Advertencia", "No hay clientes registrados")
            return
        
        ventana = VentanaNuevaVenta(self.sistema, self)
        ventana.crear_ventana()
    
    def actualizar_ventas(self):
        """Actualizar la tabla de ventas"""
        if not self.tree_ventas:
            return
            
        # Limpiar tabla
        for item in self.tree_ventas.get_children():
            self.tree_ventas.delete(item)
        
        # Llenar con datos
        for venta in self.sistema.ventas:
            self.tree_ventas.insert('', 'end', values=(
                venta["id"], venta["cliente"], venta["producto"], 
                venta["cantidad"], f"${venta['total']}", venta["fecha"], venta["vendedor"]
            ))


class VentanaNuevaVenta:
    def __init__(self, sistema, ventana_ventas):  # Corregido
        self.sistema = sistema
        self.ventana_ventas = ventana_ventas
        
    def crear_ventana(self):
        """Crear ventana para nueva venta"""
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Nueva Venta")
        self.ventana.geometry("500x400")
        self.ventana.configure(bg='#ecf0f1')
        
        # Cliente
        tk.Label(self.ventana, text="Cliente:", bg='#ecf0f1').pack(pady=5)
        self.combo_cliente = ttk.Combobox(self.ventana, width=40)
        self.combo_cliente['values'] = [f"{c['id']} - {c['nombre']}" for c in self.sistema.clientes]
        self.combo_cliente.pack(pady=5)
        
        # Producto
        tk.Label(self.ventana, text="Producto:", bg='#ecf0f1').pack(pady=5)
        self.combo_producto = ttk.Combobox(self.ventana, width=40)
        self.combo_producto['values'] = [f"{p['id']} - {p['marca']} {p['modelo']} ({p['medida']}) - ${p['precio']}" 
                                       for p in self.sistema.inventario if p['stock'] > 0]
        self.combo_producto.pack(pady=5)
        
        # Cantidad
        tk.Label(self.ventana, text="Cantidad:", bg='#ecf0f1').pack(pady=5)
        self.entry_cantidad = tk.Entry(self.ventana, width=10)
        self.entry_cantidad.pack(pady=5)
        
        # Frame para mostrar información de la venta
        info_frame = tk.Frame(self.ventana, bg='#ecf0f1')
        info_frame.pack(pady=10)
        
        self.label_total = tk.Label(info_frame, text="Total: $0.00", 
                                   font=('Arial', 14, 'bold'), bg='#ecf0f1')
        self.label_total.pack(pady=5)
        
        # Calcular total automáticamente
        self.combo_producto.bind('<<ComboboxSelected>>', self.calcular_total)
        self.entry_cantidad.bind('<KeyRelease>', self.calcular_total)
        
        tk.Button(self.ventana, text="Realizar Venta", command=self.realizar_venta, 
                 bg='#27ae60', fg='white', font=('Arial', 12, 'bold')).pack(pady=30)
    
    def calcular_total(self, event=None):
        """Calcular el total de la venta automáticamente"""
        try:
            if not self.combo_producto.get() or not self.entry_cantidad.get():
                self.label_total.config(text="Total: $0.00")
                return
            
            producto_id = int(self.combo_producto.get().split(" - ")[0])
            cantidad = int(self.entry_cantidad.get())
            
            producto = next((p for p in self.sistema.inventario if p["id"] == producto_id), None)
            if producto:
                total = producto["precio"] * cantidad
                self.label_total.config(text=f"Total: ${total:.2f}")
        except (ValueError, IndexError):
            self.label_total.config(text="Total: $0.00")
    
    def realizar_venta(self):
        """Realizar la venta"""
        try:
            if not self.combo_cliente.get() or not self.combo_producto.get() or not self.entry_cantidad.get():
                messagebox.showerror("Error", "Complete todos los campos")
                return
            
            cliente_id = int(self.combo_cliente.get().split(" - ")[0])
            producto_id = int(self.combo_producto.get().split(" - ")[0])
            cantidad = int(self.entry_cantidad.get())
            
            # Encontrar producto y cliente
            producto = next((p for p in self.sistema.inventario if p["id"] == producto_id), None)
            cliente = next((c for c in self.sistema.clientes if c["id"] == cliente_id), None)
            
            if not producto or not cliente:
                messagebox.showerror("Error", "Producto o cliente no encontrado")
                return
            
            if producto["stock"] < cantidad:
                messagebox.showerror("Error", f"Stock insuficiente. Disponible: {producto['stock']}")
                return
            
            if cantidad <= 0:
                messagebox.showerror("Error", "La cantidad debe ser mayor a 0")
                return
            
            # Realizar venta
            total = producto["precio"] * cantidad
            nueva_venta = {
                "id": len(self.sistema.ventas) + 1,
                "cliente": cliente["nombre"],
                "producto": f"{producto['marca']} {producto['modelo']}",
                "cantidad": cantidad,
                "total": total,
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "vendedor": self.sistema.usuario_actual
            }
            
            self.sistema.ventas.append(nueva_venta)
            producto["stock"] -= cantidad
            
            self.ventana_ventas.actualizar_ventas()
            # Actualizar inventario si existe la ventana
            if hasattr(self.sistema, 'ventana_inventario') and self.sistema.ventana_inventario:
                self.sistema.ventana_inventario.actualizar_inventario()
            
            self.ventana.destroy()
            messagebox.showinfo("Éxito", f"Venta realizada. Total: ${total}")
            
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número")