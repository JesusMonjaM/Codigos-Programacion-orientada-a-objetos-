import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="llantera.db"):
        self.db_name = db_name
        self.init_database()
        
    def _get_connection(self):
        """Crea una conexión a la base de datos."""
        return sqlite3.connect(self.db_name)

    def init_database(self):
        """Inicializar la base de datos y crear las tablas."""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Tabla de usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')
        
        # Tabla de inventario
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                medida TEXT NOT NULL,
                precio REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        ''')
        
        # Tabla de clientes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT,
                email TEXT
            )
        ''')
        
        # Tabla de ventas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ventas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                producto TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                total REAL NOT NULL,
                fecha TEXT NOT NULL,
                vendedor TEXT NOT NULL
            )
        ''')
        
        # Insertar usuarios por defecto si no existen
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        if cursor.fetchone()[0] == 0:
            usuarios_default = [
                ("admin", "admin", "admin"),
                ("vendedor", "vendedor", "vendedor"),
                ("almacenista", "almacenista", "almacenista")
            ]
            cursor.executemany("INSERT INTO usuarios (username, password, role) VALUES (?, ?, ?)", usuarios_default)
            
        # Insertar inventario por defecto
        cursor.execute("SELECT COUNT(*) FROM inventario")
        if cursor.fetchone()[0] == 0:
            inventario_default = [
                ("Michelin", "Primacy", "205/55R16", 2500, 10),
                ("Bridgestone", "Turanza", "185/65R15", 2100, 8),
                ("Continental", "ContiPremium", "225/45R17", 2800, 6)
            ]
            cursor.executemany("INSERT INTO inventario (marca, modelo, medida, precio, stock) VALUES (?, ?, ?, ?, ?)", inventario_default)

        # Insertar clientes por defecto
        cursor.execute("SELECT COUNT(*) FROM clientes")
        if cursor.fetchone()[0] == 0:
            clientes_default = [
                ("Juan Pérez", "555-1234", "juan@email.com"),
                ("María García", "555-5678", "maria@email.com")
            ]
            cursor.executemany("INSERT INTO clientes (nombre, telefono, email) VALUES (?, ?, ?)", clientes_default)

        conn.commit()
        conn.close()

    # Métodos para USUARIOS
    def get_usuarios(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username, password, role FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return {row[0]: {"password": row[1], "role": row[2]} for row in rows}

    def get_usuario_by_username(self, username):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username, password, role FROM usuarios WHERE username = ?", (username,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"username": row[0], "password": row[1], "role": row[2]}
        return None

    def agregar_usuario(self, username, password, role):
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (username, password, role) VALUES (?, ?, ?)", (username, password, role))
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            conn.close()
            return False

    def modificar_usuario(self, username, nuevo_password, nuevo_role):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET password = ?, role = ? WHERE username = ?", (nuevo_password, nuevo_role, username))
        conn.commit()
        conn.close()

    def eliminar_usuario(self, username):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))
        conn.commit()
        conn.close()

    # Métodos para INVENTARIO
    def get_inventario(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, marca, modelo, medida, precio, stock FROM inventario")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": r[0], "marca": r[1], "modelo": r[2], "medida": r[3], "precio": r[4], "stock": r[5]} for r in rows]

    def get_llanta_by_id(self, llanta_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, marca, modelo, medida, precio, stock FROM inventario WHERE id = ?", (llanta_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "marca": row[1], "modelo": row[2], "medida": row[3], "precio": row[4], "stock": row[5]}
        return None

    def agregar_llanta(self, marca, modelo, medida, precio, stock):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inventario (marca, modelo, medida, precio, stock) VALUES (?, ?, ?, ?, ?)", (marca, modelo, medida, precio, stock))
        conn.commit()
        conn.close()

    def modificar_llanta(self, llanta_id, marca, modelo, medida, precio, stock):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE inventario SET marca = ?, modelo = ?, medida = ?, precio = ?, stock = ? WHERE id = ?", (marca, modelo, medida, precio, stock, llanta_id))
        conn.commit()
        conn.close()

    def eliminar_llanta(self, llanta_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM inventario WHERE id = ?", (llanta_id,))
        conn.commit()
        conn.close()

    # Métodos para CLIENTES
    def get_clientes(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, telefono, email FROM clientes")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": r[0], "nombre": r[1], "telefono": r[2], "email": r[3]} for r in rows]
    
    def get_cliente_by_id(self, cliente_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, telefono, email FROM clientes WHERE id = ?", (cliente_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "nombre": row[1], "telefono": row[2], "email": row[3]}
        return None

    def agregar_cliente(self, nombre, telefono, email):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nombre, telefono, email) VALUES (?, ?, ?)", (nombre, telefono, email))
        conn.commit()
        conn.close()

    def modificar_cliente(self, cliente_id, nombre, telefono, email):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET nombre = ?, telefono = ?, email = ? WHERE id = ?", (nombre, telefono, email, cliente_id))
        conn.commit()
        conn.close()

    # Métodos para VENTAS
    def get_ventas(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, cliente, producto, cantidad, total, fecha, vendedor FROM ventas")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": r[0], "cliente": r[1], "producto": r[2], "cantidad": r[3], "total": r[4], "fecha": r[5], "vendedor": r[6]} for r in rows]

    def registrar_venta(self, cliente, producto, cantidad, total, vendedor):
        conn = self._get_connection()
        cursor = conn.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO ventas (cliente, producto, cantidad, total, fecha, vendedor) VALUES (?, ?, ?, ?, ?, ?)", (cliente, producto, cantidad, total, fecha, vendedor))
        conn.commit()
        conn.close()