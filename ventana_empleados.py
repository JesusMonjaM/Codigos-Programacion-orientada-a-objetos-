import tkinter as tk
from tkinter import ttk

class VentanaEmpleados:
    def __init__(self, sistema, notebook):
        self.sistema = sistema
        self.notebook = notebook
        
    def crear_pestana(self):
        """Crear la pestaña de empleados (solo admin)"""
        # Frame para empleados
        self.emp_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.emp_frame, text="👨‍💼 Empleados")
        
        # Título principal
        header_frame = tk.Frame(self.emp_frame, bg='#2c3e50', height=60)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text="👨‍💼 GESTIÓN DE EMPLEADOS", 
                font=('Arial', 18, 'bold'), fg='white', bg='#2c3e50').pack(pady=15)
        
        # Frame principal con scroll
        main_frame = tk.Frame(self.emp_frame, bg='#ecf0f1')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Crear canvas y scrollbar
        canvas = tk.Canvas(main_frame, bg='#ecf0f1')
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#ecf0f1')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Información detallada de empleados
        self.crear_info_empleados(scrollable_frame)
        
        # Pack canvas y scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def crear_info_empleados(self, parent):
        """Crear la información detallada de empleados"""
        
        # Resumen general
        resumen_frame = tk.LabelFrame(parent, text="📊 Resumen del Sistema", 
                                     font=('Arial', 14, 'bold'), bg='#ecf0f1', fg='#2c3e50')
        resumen_frame.pack(fill='x', pady=10)
        
        resumen_info = f"""
🔧 SISTEMA DE LLANTERA - GESTIÓN DE USUARIOS
═══════════════════════════════════════════

👥 Total de usuarios en el sistema: {len(self.sistema.usuarios)}
🔐 Tipos de rol disponibles: 3
⚡ Estado del sistema: ACTIVO
👤 Usuario actual: {self.sistema.usuario_actual.upper()}
🎯 Rol actual: {self.sistema.role_actual.upper()}
        """
        
        tk.Label(resumen_frame, text=resumen_info, font=('Courier', 10), 
                bg='#ecf0f1', fg='#2c3e50', justify='left').pack(padx=15, pady=10)
        
        # Información de cada usuario
        for i, (usuario, datos) in enumerate(self.sistema.usuarios.items()):
            self.crear_tarjeta_empleado(parent, usuario, datos, i)
        
        # Información de permisos
        permisos_frame = tk.LabelFrame(parent, text="🔒 Matriz de Permisos", 
                                      font=('Arial', 14, 'bold'), bg='#ecf0f1', fg='#2c3e50')
        permisos_frame.pack(fill='x', pady=10)
        
        permisos_info = """
PERMISOS POR ROL:
════════════════

📦 INVENTARIO:
   • admin: ✅ Crear ✅ Leer ✅ Actualizar ✅ Eliminar
   • almacenista: ✅ Crear ✅ Leer ✅ Actualizar ✅ Eliminar
   • vendedor: ❌ Crear ✅ Leer ❌ Actualizar ❌ Eliminar

💰 VENTAS:
   • admin: ✅ Crear ✅ Leer ✅ Reportes
   • vendedor: ✅ Crear ✅ Leer ❌ Reportes
   • almacenista: ❌ Crear ❌ Leer ❌ Reportes

👥 CLIENTES:
   • admin: ✅ Crear ✅ Leer ✅ Actualizar
   • vendedor: ✅ Crear ✅ Leer ✅ Actualizar
   • almacenista: ❌ Crear ❌ Leer ❌ Actualizar

📊 REPORTES:
   • admin: ✅ Todos los reportes
   • vendedor: ❌ Sin acceso
   • almacenista: ❌ Sin acceso

👨‍💼 EMPLEADOS:
   • admin: ✅ Ver información completa
   • vendedor: ❌ Sin acceso
   • almacenista: ❌ Sin acceso
        """
        
        tk.Label(permisos_frame, text=permisos_info, font=('Courier', 9), 
                bg='#ecf0f1', fg='#2c3e50', justify='left').pack(padx=15, pady=10)
    
    def crear_tarjeta_empleado(self, parent, usuario, datos, index):
        """Crear una tarjeta individual para cada empleado"""
        
        # Colores por rol
        colores_rol = {
            'admin': '#e74c3c',      # Rojo
            'vendedor': '#3498db',   # Azul
            'almacenista': '#27ae60' # Verde
        }
        
        # Iconos por rol
        iconos_rol = {
            'admin': '👑',
            'vendedor': '💼',
            'almacenista': '📦'
        }
        
        # Descripción por rol
        descripciones = {
            'admin': 'Acceso completo al sistema. Gestión de inventario, ventas, clientes, reportes y empleados.',
            'vendedor': 'Gestión de ventas y clientes. Consulta de inventario disponible.',
            'almacenista': 'Gestión completa del inventario. Control de stock y productos.'
        }
        
        rol = datos['role']
        color = colores_rol.get(rol, '#95a5a6')
        icono = iconos_rol.get(rol, '👤')
        
        # Frame de la tarjeta
        card_frame = tk.LabelFrame(parent, text=f"{icono} {usuario.upper()}", 
                                  font=('Arial', 12, 'bold'), bg='white', fg=color,
                                  relief='raised', bd=2)
        card_frame.pack(fill='x', pady=5, padx=5)
        
        # Información del empleado
        info_frame = tk.Frame(card_frame, bg='white')
        info_frame.pack(fill='x', padx=15, pady=10)
        
        # Fila 1: Información básica
        basic_frame = tk.Frame(info_frame, bg='white')
        basic_frame.pack(fill='x', pady=5)
        
        tk.Label(basic_frame, text=f"🔐 Usuario:", font=('Arial', 10, 'bold'), 
                bg='white', fg='#2c3e50').pack(side='left')
        tk.Label(basic_frame, text=usuario, font=('Arial', 10), 
                bg='white', fg='#34495e').pack(side='left', padx=(5,20))
        
        tk.Label(basic_frame, text=f"🎯 Rol:", font=('Arial', 10, 'bold'), 
                bg='white', fg='#2c3e50').pack(side='left')
        tk.Label(basic_frame, text=rol.upper(), font=('Arial', 10), 
                bg='white', fg=color).pack(side='left', padx=(5,0))
        
        # Fila 2: Estado
        status_frame = tk.Frame(info_frame, bg='white')
        status_frame.pack(fill='x', pady=2)
        
        estado = "🟢 CONECTADO" if usuario == self.sistema.usuario_actual else "⚪ DESCONECTADO"
        tk.Label(status_frame, text=f"📡 Estado: {estado}", font=('Arial', 10), 
                bg='white', fg='#27ae60' if usuario == self.sistema.usuario_actual else '#95a5a6').pack(side='left')
        
        # Fila 3: Descripción
        desc_frame = tk.Frame(info_frame, bg='white')
        desc_frame.pack(fill='x', pady=5)
        
        tk.Label(desc_frame, text="📋 Descripción:", font=('Arial', 10, 'bold'), 
                bg='white', fg='#2c3e50').pack(anchor='w')
        tk.Label(desc_frame, text=descripciones.get(rol, ''), font=('Arial', 9), 
                bg='white', fg='#7f8c8d', wraplength=600, justify='left').pack(anchor='w', padx=(20,0))
        
        # Estadísticas si es vendedor
        if rol == 'vendedor':
            ventas_vendedor = [v for v in self.sistema.ventas if v['vendedor'] == usuario]
            if ventas_vendedor:
                stats_frame = tk.Frame(info_frame, bg='white')
                stats_frame.pack(fill='x', pady=5)
                
                total_ventas = sum(v['total'] for v in ventas_vendedor)
                num_ventas = len(ventas_vendedor)
                
                tk.Label(stats_frame, text="📊 Estadísticas:", font=('Arial', 10, 'bold'), 
                        bg='white', fg='#2c3e50').pack(anchor='w')
                stats_text = f"   • Ventas realizadas: {num_ventas}   • Total vendido: ${total_ventas:.2f}"
                tk.Label(stats_frame, text=stats_text, font=('Arial', 9), 
                        bg='white', fg='#16a085').pack(anchor='w', padx=(20,0))