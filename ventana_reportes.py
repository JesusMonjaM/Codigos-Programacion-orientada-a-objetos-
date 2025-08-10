import tkinter as tk
from tkinter import ttk

class VentanaReportes:
    def __init__(self, sistema, notebook):  # Corregido
        self.sistema = sistema
        self.notebook = notebook
        self.text_reportes = None
        
    def crear_pestana(self):
        """Crear la pestaña de reportes"""
        # Frame para reportes
        self.reportes_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.reportes_frame, text="📊 Reportes")
        
        # Frame de botones
        btn_frame = tk.Frame(self.reportes_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Button(btn_frame, text="📈 Reporte de Ventas", command=self.generar_reporte_ventas, 
                 bg='#8e44ad', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="📦 Reporte de Inventario", command=self.generar_reporte_inventario, 
                 bg='#2980b9', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="💰 Reporte Financiero", command=self.generar_reporte_financiero, 
                 bg='#16a085', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="🗑 Limpiar", command=self.limpiar_reportes, 
                 bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=5)
        
        # Área de texto para reportes
        self.text_reportes = tk.Text(self.reportes_frame, font=('Courier', 10), wrap='word')
        scrollbar_reportes = ttk.Scrollbar(self.reportes_frame, orient='vertical', command=self.text_reportes.yview)
        self.text_reportes.configure(yscrollcommand=scrollbar_reportes.set)
        
        self.text_reportes.pack(side='left', fill='both', expand=True, padx=(10,0), pady=10)
        scrollbar_reportes.pack(side='right', fill='y', padx=(0,10), pady=10)
        
        # Mostrar mensaje inicial
        mensaje_inicial = """
        🔧 SISTEMA DE REPORTES - LLANTERA
        =====================================
        
        Seleccione un tipo de reporte para generar:
        
        📈 Reporte de Ventas: Muestra todas las ventas realizadas
        📦 Reporte de Inventario: Estado actual del inventario
        💰 Reporte Financiero: Resumen de ingresos y estadísticas
        
        Los reportes aparecerán en esta área.
        """
        self.text_reportes.insert('1.0', mensaje_inicial)
    
    def limpiar_reportes(self):
        """Limpiar el área de reportes"""
        self.text_reportes.delete('1.0', tk.END)
    
    def generar_reporte_ventas(self):
        """Generar reporte detallado de ventas"""
        if not self.sistema.ventas:
            reporte = """
            📈 REPORTE DE VENTAS
            ==================
            
            ⚠  NO HAY VENTAS REGISTRADAS
            
            """
        else:
            reporte = "=" * 80 + "\n"
            reporte += "                           📈 REPORTE DE VENTAS\n"
            reporte += "=" * 80 + "\n\n"
            
            total_ventas = 0
            ventas_por_vendedor = {}
            productos_vendidos = {}
            
            for i, venta in enumerate(self.sistema.ventas, 1):
                reporte += f"🛒 VENTA #{venta['id']}:\n"
                reporte += f"   Cliente: {venta['cliente']}\n"
                reporte += f"   Producto: {venta['producto']}\n"
                reporte += f"   Cantidad: {venta['cantidad']} unidades\n"
                reporte += f"   Total: ${venta['total']:.2f}\n"
                reporte += f"   Fecha: {venta['fecha']}\n"
                reporte += f"   Vendedor: {venta['vendedor']}\n"
                reporte += "-" * 60 + "\n\n"
                
                total_ventas += venta['total']
                
                # Estadísticas por vendedor
                if venta['vendedor'] in ventas_por_vendedor:
                    ventas_por_vendedor[venta['vendedor']]['total'] += venta['total']
                    ventas_por_vendedor[venta['vendedor']]['cantidad'] += 1
                else:
                    ventas_por_vendedor[venta['vendedor']] = {
                        'total': venta['total'],
                        'cantidad': 1
                    }
                
                # Productos más vendidos
                if venta['producto'] in productos_vendidos:
                    productos_vendidos[venta['producto']] += venta['cantidad']
                else:
                    productos_vendidos[venta['producto']] = venta['cantidad']
            
            # Resumen
            reporte += "=" * 80 + "\n"
            reporte += "                              📊 RESUMEN GENERAL\n"
            reporte += "=" * 80 + "\n"
            reporte += f"💰 Total de ventas realizadas: {len(self.sistema.ventas)}\n"
            reporte += f"💵 Ingresos totales: ${total_ventas:.2f}\n"
            reporte += f"💸 Promedio por venta: ${total_ventas/len(self.sistema.ventas):.2f}\n\n"
            
            reporte += "👨‍💼 VENTAS POR VENDEDOR:\n"
            reporte += "-" * 40 + "\n"
            for vendedor, datos in ventas_por_vendedor.items():
                reporte += f"   {vendedor.upper()}:\n"
                reporte += f"     • Ventas: {datos['cantidad']}\n"
                reporte += f"     • Total: ${datos['total']:.2f}\n"
                reporte += f"     • Promedio: ${datos['total']/datos['cantidad']:.2f}\n\n"
            
            if productos_vendidos:
                reporte += "🏆 PRODUCTOS MÁS VENDIDOS:\n"
                reporte += "-" * 40 + "\n"
                productos_ordenados = sorted(productos_vendidos.items(), key=lambda x: x[1], reverse=True)
                for i, (producto, cantidad) in enumerate(productos_ordenados[:5], 1):
                    reporte += f"   {i}. {producto}: {cantidad} unidades\n"
            
            reporte += "\n" + "=" * 80 + "\n"
        
        self.text_reportes.delete('1.0', tk.END)
        self.text_reportes.insert('1.0', reporte)
    
    def generar_reporte_inventario(self):
        """Generar reporte detallado del inventario"""
        reporte = "=" * 80 + "\n"
        reporte += "                        📦 REPORTE DE INVENTARIO\n"
        reporte += "=" * 80 + "\n\n"
        
        valor_total = 0
        productos_bajo_stock = []
        productos_sin_stock = []
        productos_por_marca = {}
        
        for producto in self.sistema.inventario:
            reporte += f"🔧 PRODUCTO ID #{producto['id']}:\n"
            reporte += f"   Marca: {producto['marca']}\n"
            reporte += f"   Modelo: {producto['modelo']}\n"
            reporte += f"   Medida: {producto['medida']}\n"
            reporte += f"   Precio unitario: ${producto['precio']:.2f}\n"
            reporte += f"   Stock disponible: {producto['stock']} unidades\n"
            
            valor_producto = producto['precio'] * producto['stock']
            reporte += f"   Valor en inventario: ${valor_producto:.2f}\n"
            
            # Estado del stock
            if producto['stock'] == 0:
                reporte += "   ❌ SIN STOCK\n"
                productos_sin_stock.append(f"{producto['marca']} {producto['modelo']}")
            elif producto['stock'] < 5:
                reporte += "   ⚠  STOCK BAJO\n"
                productos_bajo_stock.append(f"{producto['marca']} {producto['modelo']} ({producto['stock']} unidades)")
            else:
                reporte += "   ✅ STOCK ADECUADO\n"
            
            valor_total += valor_producto
            
            # Agrupar por marca
            if producto['marca'] in productos_por_marca:
                productos_por_marca[producto['marca']]['cantidad'] += 1
                productos_por_marca[producto['marca']]['valor'] += valor_producto
            else:
                productos_por_marca[producto['marca']] = {
                    'cantidad': 1,
                    'valor': valor_producto
                }
            
            reporte += "-" * 60 + "\n\n"
        
        # Resumen
        reporte += "=" * 80 + "\n"
        reporte += "                              📊 RESUMEN INVENTARIO\n"
        reporte += "=" * 80 + "\n"
        reporte += f"📦 Total de productos diferentes: {len(self.sistema.inventario)}\n"
        reporte += f"📊 Unidades totales en stock: {sum(p['stock'] for p in self.sistema.inventario)}\n"
        reporte += f"💰 Valor total del inventario: ${valor_total:.2f}\n\n"
        
        # Inventario por marca
        reporte += "🏷  INVENTARIO POR MARCA:\n"
        reporte += "-" * 40 + "\n"
        for marca, datos in productos_por_marca.items():
            reporte += f"   {marca.upper()}:\n"
            reporte += f"     • Productos: {datos['cantidad']}\n"
            reporte += f"     • Valor: ${datos['valor']:.2f}\n\n"
        
        # Alertas
        if productos_sin_stock:
            reporte += "❌ PRODUCTOS SIN STOCK:\n"
            reporte += "-" * 40 + "\n"
            for producto in productos_sin_stock:
                reporte += f"   • {producto}\n"
            reporte += "\n"
        
        if productos_bajo_stock:
            reporte += "⚠  PRODUCTOS CON STOCK BAJO (menos de 5 unidades):\n"
            reporte += "-" * 40 + "\n"
            for producto in productos_bajo_stock:
                reporte += f"   • {producto}\n"
            reporte += "\n"
        
        if not productos_bajo_stock and not productos_sin_stock:
            reporte += "✅ ESTADO DEL INVENTARIO: ÓPTIMO\n"
            reporte += "   Todos los productos tienen stock adecuado\n\n"
        
        reporte += "=" * 80 + "\n"
        
        self.text_reportes.delete('1.0', tk.END)
        self.text_reportes.insert('1.0', reporte)
    
    def generar_reporte_financiero(self):
        """Generar reporte financiero completo"""
        reporte = "=" * 80 + "\n"
        reporte += "                         💰 REPORTE FINANCIERO\n"
        reporte += "=" * 80 + "\n\n"
        
        if not self.sistema.ventas:
            reporte += "⚠  NO HAY DATOS DE VENTAS PARA GENERAR REPORTE FINANCIERO\n\n"
        else:
            # Cálculos financieros
            ingresos_totales = sum(venta['total'] for venta in self.sistema.ventas)
            numero_ventas = len(self.sistema.ventas)
            promedio_venta = ingresos_totales / numero_ventas
            
            # Análisis por vendedor
            ventas_vendedor = {}
            for venta in self.sistema.ventas:
                if venta['vendedor'] not in ventas_vendedor:
                    ventas_vendedor[venta['vendedor']] = []
                ventas_vendedor[venta['vendedor']].append(venta['total'])
            
            reporte += "💵 RESUMEN FINANCIERO:\n"
            reporte += "-" * 40 + "\n"
            reporte += f"   Ingresos totales: ${ingresos_totales:.2f}\n"
            reporte += f"   Número de ventas: {numero_ventas}\n"
            reporte += f"   Promedio por venta: ${promedio_venta:.2f}\n"
            reporte += f"   Venta más alta: ${max(venta['total'] for venta in self.sistema.ventas):.2f}\n"
            reporte += f"   Venta más baja: ${min(venta['total'] for venta in self.sistema.ventas):.2f}\n\n"
            
            reporte += "👨‍💼 DESEMPEÑO POR VENDEDOR:\n"
            reporte += "-" * 40 + "\n"
            for vendedor, ventas in ventas_vendedor.items():
                total_vendedor = sum(ventas)
                num_ventas = len(ventas)
                promedio_vendedor = total_vendedor / num_ventas
                participacion = (total_vendedor / ingresos_totales) * 100
                
                reporte += f"   {vendedor.upper()}:\n"
                reporte += f"     • Total vendido: ${total_vendedor:.2f}\n"
                reporte += f"     • Número de ventas: {num_ventas}\n"
                reporte += f"     • Promedio por venta: ${promedio_vendedor:.2f}\n"
                reporte += f"     • Participación: {participacion:.1f}%\n\n"
        
        # Valor del inventario
        valor_inventario = sum(p['precio'] * p['stock'] for p in self.sistema.inventario)
        reporte += "📦 VALOR DEL INVENTARIO:\n"
        reporte += "-" * 40 + "\n"
        reporte += f"   Valor total en inventario: ${valor_inventario:.2f}\n"
        reporte += f"   Productos en stock: {len(self.sistema.inventario)}\n"
        reporte += f"   Unidades totales: {sum(p['stock'] for p in self.sistema.inventario)}\n\n"
        
        # Resumen general
        if self.sistema.ventas:
            reporte += "📊 INDICADORES CLAVE:\n"
            reporte += "-" * 40 + "\n"
            rotacion = ingresos_totales / valor_inventario if valor_inventario > 0 else 0
            reporte += f"   Rotación de inventario: {rotacion:.2f}\n"
            reporte += f"   Ingresos vs Inventario: {(ingresos_totales / valor_inventario * 100):.1f}%\n" if valor_inventario > 0 else ""
        
        reporte += "\n" + "=" * 80 + "\n"
        
        self.text_reportes.delete('1.0', tk.END)
        self.text_reportes.insert('1.0', reporte)