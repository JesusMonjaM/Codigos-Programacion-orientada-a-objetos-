import tkinter as tk
from tkinter import messagebox

class VentanaLogin:
    def __init__(self, sistema):  # <-- ¡Constructor corregido!
        self.sistema = sistema
        self.root = sistema.root
        
    def crear_ventana(self):
        """Crear la ventana de login"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal de login
        login_frame = tk.Frame(self.root, bg='#2c3e50', relief='raised', bd=2)
        login_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=300)
        
        # Título
        title_label = tk.Label(login_frame, text="🔧 CLAMATIN", 
                              font=('Arial', 20, 'bold'), 
                              fg='white', bg='#2c3e50')
        title_label.pack(pady=20)
        
        # Usuario
        tk.Label(login_frame, text="Usuario:", font=('Arial', 12), 
                fg='white', bg='#2c3e50').pack(pady=5)
        self.entry_usuario = tk.Entry(login_frame, font=('Arial', 12), width=20)
        self.entry_usuario.pack(pady=5)
        
        # Contraseña
        tk.Label(login_frame, text="Contraseña:", font=('Arial', 12), 
                fg='white', bg='#2c3e50').pack(pady=5)
        self.entry_password = tk.Entry(login_frame, font=('Arial', 12), width=20, show='*')
        self.entry_password.pack(pady=5)
        
        # Evento Enter para login
        self.entry_password.bind('<Return>', lambda event: self.verificar_login())
        
        # Botón login
        btn_login = tk.Button(login_frame, text="Iniciar Sesión", 
                             font=('Arial', 12, 'bold'), bg='#3498db', fg='white',
                             command=self.verificar_login, width=15)
        btn_login.pack(pady=20)
        
        # Información de usuarios
        info_frame = tk.Frame(self.root, bg='#ecf0f1')
        info_frame.pack(side='bottom', fill='x', pady=10)
        
        tk.Label(info_frame, text="Usuarios disponibles: admin, vendedor, almacenista", 
                font=('Arial', 10), bg='#ecf0f1').pack()
        tk.Label(info_frame, text="Contraseñas: admin, vendedor, almcenista", 
                font=('Arial', 10), bg='#ecf0f1').pack()
    
    def verificar_login(self):
        """Verificar las credenciales de login"""
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        if usuario in self.sistema.usuarios and self.sistema.usuarios[usuario]["password"] == password:
            role = self.sistema.usuarios[usuario]["role"]
            self.sistema.iniciar_sesion(usuario, role)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")