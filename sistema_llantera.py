import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from ventana_login import VentanaLogin
from ventana_inventario import VentanaInventario
from ventana_ventas import VentanaVentas
from ventana_clientes import VentanaClientes
from ventana_reportes import VentanaReportes
from ventana_empleados import VentanaEmpleados

class SistemaLlantera:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clamatin")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Datos del sistema
        self.usuarios = {
            "admin": {"password": "admin", "role": "admin"},
            "vendedor": {"password": "vendedor", "role": "vendedor"},
            "almacenista": {"password": "almacenista", "role": "almacenista"}
        }
        
        # Inicializar datos
        self.inventario = [
            {"id": 1, "marca": "Michelin", "modelo": "Primacy", "medida": "205/55R16", "precio": 2500, "stock": 10},
            {"id": 2, "marca": "Bridgestone", "modelo": "Turanza", "medida": "185/65R15", "precio": 2100, "stock": 8},
            {"id": 3, "marca": "Continental", "modelo": "ContiPremium", "medida": "225/45R17", "precio": 2800, "stock": 6}
        ]
        
        self.clientes = [
            {"id": 1, "nombre": "Juan Pérez", "telefono": "555-1234", "email": "juan@email.com"},
            {"id": 2, "nombre": "María García", "telefono": "555-5678", "email": "maria@email.com"}
        ]
        
        self.ventas = []
        self.reportes = []
        
        self.usuario_actual = None
        self.role_actual = None
        
        # Instanciar ventanas
        self.ventana_login = VentanaLogin(self)
        self.ventana_inventario = None
        self.ventana_ventas = None
        self.ventana_clientes = None
        self.ventana_reportes = None
        self.ventana_empleados = None
        
        self.ventana_login.crear_ventana()
    
    def iniciar_sesion(self, usuario, role):
        """Método para iniciar sesión y crear el menú principal"""
        self.usuario_actual = usuario
        self.role_actual = role
        self.crear_menu_principal()
    
    def crear_menu_principal(self):
        """Crear el menú principal con pestañas según el rol"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text=f"🔧 CLAMATIN", 
                font=('Arial', 18, 'bold'), fg='white', bg='#2c3e50').pack(side='left', padx=20, pady=25)
        
        user_info = tk.Label(header_frame, text=f"Usuario: {self.usuario_actual.upper()} | Rol: {self.role_actual.upper()}", 
                           font=('Arial', 12), fg='white', bg='#2c3e50')
        user_info.pack(side='right', padx=20, pady=25)
        
        # Botón logout
        btn_logout = tk.Button(header_frame, text="Cerrar Sesión", 
                              command=self.cerrar_sesion, bg='#e74c3c', fg='white')
        btn_logout.pack(side='right', padx=10, pady=25)
        
        # Notebook para pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Crear pestañas según el rol
        self.crear_pestanas_por_rol()
    
    def cerrar_sesion(self):
        """Cerrar sesión y volver al login"""
        self.usuario_actual = None
        self.role_actual = None
        self.ventana_login.crear_ventana()
    
    def crear_pestanas_por_rol(self):
        """Crear pestañas según el rol del usuario"""
        if self.role_actual == "admin":
            self.crear_pestana_inventario(completa=True)
            self.crear_pestana_ventas()
            self.crear_pestana_clientes()
            self.crear_pestana_reportes()
            self.crear_pestana_empleados()
        
        elif self.role_actual == "vendedor":
            self.crear_pestana_ventas()
            self.crear_pestana_clientes()
            self.crear_pestana_inventario(completa=False)
        
        elif self.role_actual == "almacenista":
            self.crear_pestana_inventario(completa=True)
    
    def crear_pestana_inventario(self, completa=True):
        """Crear pestaña de inventario"""
        self.ventana_inventario = VentanaInventario(self, self.notebook, completa)
        self.ventana_inventario.crear_pestana()
    
    def crear_pestana_ventas(self):
        """Crear pestaña de ventas"""
        self.ventana_ventas = VentanaVentas(self, self.notebook)
        self.ventana_ventas.crear_pestana()
    
    def crear_pestana_clientes(self):
        """Crear pestaña de clientes"""
        self.ventana_clientes = VentanaClientes(self, self.notebook)
        self.ventana_clientes.crear_pestana()
    
    def crear_pestana_reportes(self):
        """Crear pestaña de reportes"""
        self.ventana_reportes = VentanaReportes(self, self.notebook)
        self.ventana_reportes.crear_pestana()
    
    def crear_pestana_empleados(self):
        """Crear pestaña de empleados"""
        self.ventana_empleados = VentanaEmpleados(self, self.notebook)
        self.ventana_empleados.crear_pestana()
    
    def run(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()