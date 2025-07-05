import customtkinter as ctk
from PIL import Image, ImageTk
ctk.set_appearance_mode("light")  # Modo claro
ctk.set_default_color_theme("blue")  # Tema azul
#ventana principal
ventana_principal = ctk.CTk()
ventana_principal.title("Llantera Clamatin")
ventana_principal.geometry("1280x720")
ventana_principal.iconbitmap("clamatin.ico")
#ENCABEZADO
marco_encabezado = ctk.CTkFrame(ventana_principal, corner_radius=0,fg_color="#004AAD", height=100,)
marco_encabezado.pack(fill="x")

# Logo CLAMATIN
etiqueta_logo = ctk.CTkLabel(marco_encabezado,text_color="white", text="CLAMATIN", font=("Arial", 25, "bold"))
etiqueta_logo.pack(side="left", padx=20,pady=10)

# Menú de navegación
marco_navegacion = ctk.CTkFrame(marco_encabezado, fg_color="#004AAD")
marco_navegacion.pack(side="left", padx=10,pady=10)
botones_navegacion = ["Inicio", "Catálogo", "Contáctanos", "Promociones"]
for boton in botones_navegacion:
    btn = ctk.CTkButton(marco_navegacion, text=boton, fg_color="#004AAD", 
                        hover_color="#003274", text_color="white", font=("Arial", 14))
    btn.pack(side="left", padx=10)

# Botón del carrito
boton_carrito = ctk.CTkButton(marco_encabezado,fg_color="#EAB309",hover_color="#9B7505", text="Carrito", width=100)
boton_carrito.pack(side="right", padx=20)

# Barra de búsqueda
marco_busqueda = ctk.CTkFrame(marco_encabezado, fg_color="transparent")
marco_busqueda.pack(side="right")
entrada_busqueda = ctk.CTkEntry(marco_busqueda,placeholder_text_color="#89BCFD",border_color="#5BA2FF" , placeholder_text="Buscar...",fg_color="#5BA2FF", width=200)
entrada_busqueda.pack(side="right", padx=5)

#CONTENIDO PRINCIPAL
marco_principal = ctk.CTkFrame(ventana_principal, fg_color="#CFCFCF")
marco_principal.pack( fill="both", expand=True)

#filtros
marco_filtros = ctk.CTkFrame(marco_principal,fg_color="#FFFFFF",border_width=1,border_color="black",corner_radius=20)
marco_filtros.pack(side="left", fill="y", padx=(20, 20),pady=20)

#Título
ctk.CTkLabel(marco_filtros,text_color="black", text="Añadir llanta", font=("Arial", 18, "bold")).pack(pady=(10, 10))

#Filtro de Marca
ctk.CTkLabel(marco_filtros,text_color="black", text="Marca de llanta", font=("Arial", 14)).pack(anchor="w", padx=10)
variable_marca = ctk.StringVar(value="Todas las marcas")
menu_marca = ctk.CTkOptionMenu(
    marco_filtros, 
    variable=variable_marca,
    values=["Todas las marcas", "Michelin", "Bridgestone", "Goodyear", "Pirelli", "Continental"],
    width=220
)
menu_marca.pack(pady=(0, 15), padx=0)

# Filtro de Modelo
ctk.CTkLabel(marco_filtros,text_color="black", text="Modelo", font=("Arial", 14)).pack(anchor="w", padx=10)
entrada_modelo = ctk.CTkEntry(marco_filtros,border_color="#858585",fg_color="#FFFFFF",text_color="black", placeholder_text="Nombre o código de llanta", width=220)
entrada_modelo.pack(pady=(0, 15), padx=10)

# Filtro de Medidas
ctk.CTkLabel(marco_filtros,text_color="black", text="Medidas", font=("Arial", 14)).pack(anchor="w", padx=10)
entrada_medidas = ctk.CTkEntry(marco_filtros,border_color="#858585",fg_color="#FFFFFF", placeholder_text="205/55 R16", width=220)
entrada_medidas.pack(pady=(0, 15), padx=10)

# Filtro de Tipo de vehículo
ctk.CTkLabel(marco_filtros,text_color="black", text="Tipo de vehículo", font=("Arial", 14)).pack(anchor="w", padx=10)
variable_tipo = ctk.StringVar(value="Todos los tipos")
menu_tipo = ctk.CTkOptionMenu(
    marco_filtros, 
    variable=variable_tipo,
    values=["Todos los tipos", "Auto", "SUV", "Camión", "Motocicleta"],
    width=220
)
menu_tipo.pack(pady=(0, 15), padx=10)

# Filtro de Estación
ctk.CTkLabel(marco_filtros,text_color="black", text="Estación del año", font=("Arial", 14)).pack(anchor="w", padx=10)
variable_estacion = ctk.StringVar(value="Todas las estaciones")
menu_estacion = ctk.CTkOptionMenu(
    marco_filtros, 
    variable=variable_estacion,
    values=["Todas las estaciones", "Verano", "Invierno", "Todo Clima", "Todo Terreno"],
    width=220
)
menu_estacion.pack(pady=(0, 20), padx=10)

# Botón de aplicar filtros
boton_filtros = ctk.CTkButton(marco_filtros,hover_color="#003274",fg_color="#004AAD", text="Aplicar filtros", width=220)
boton_filtros.pack(pady=10)

# Filtro de orden de productos
marco_catalogo = ctk.CTkFrame(marco_principal, fg_color="transparent")
marco_catalogo.pack(side="right", fill="both", expand=True)

# Ordenar por
marco_orden = ctk.CTkFrame(marco_catalogo, fg_color="transparent")
marco_orden.pack(fill="x", pady=(0, 20))
variable_orden = ctk.StringVar(value="Precio: Mayor a Menor")
menu_orden = ctk.CTkOptionMenu(marco_orden, variable=variable_orden,values=["Precio: Mayor a Menor", "Precio: Menor a Mayor", "Popularidad", "Novedades"],width=200)
menu_orden.pack(side="right",pady=20,padx=20)
ctk.CTkLabel(marco_orden,text_color="black", text="Ordenar por:", font=("Arial", 14)).pack(side="right", padx=0)

#incremento o decremento de la cantidad de llantas
Cantidadllanta = 0
global cantidad_label

def actualizar_cantidad():
    cantidad_label.configure(text=f"Cantidad: {Cantidadllanta}")

def incrementar():
    global Cantidadllanta
    Cantidadllanta += 1
    actualizar_cantidad()

def decrementar():
    global Cantidadllanta
    if Cantidadllanta > 0:
        Cantidadllanta -= 1
        actualizar_cantidad()

marco_producto=ctk.CTkFrame(marco_catalogo,height=50,width=20)
marco_producto.place(x=25,y=30)

marco_info=ctk.CTkFrame(marco_producto, fg_color="transparent")
marco_info.pack(side="right",fill="both",expand=True, padx=10)

#imagen de la llanta
try:
    imagen_llanta = Image.open("neumatico.png")
    imagen_llanta = imagen_llanta.resize((120, 120), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(imagen_llanta)
    label_imagen = ctk.CTkLabel(
        marco_info,
        image=img_tk,
        text="" 
    )
    label_imagen.pack(anchor="n")
    label_imagen.image = img_tk 
except Exception as e:
    print("Error al cargar imagen:", e)
    label_error = ctk.CTkLabel(marco_info, text="Imagen no disponible", text_color="red")
    label_error.place(x=50, y=10)

ctk.CTkLabel(marco_info, text="Michelin Energy Saver", font=("Arial", 16, "bold")).pack(anchor="s")
ctk.CTkLabel(marco_info, text="🛞205/55 R16", font=("Arial", 14)).pack(anchor="s")
ctk.CTkLabel(marco_info, text="🚗Auto/Todo Clima", font=("Arial", 14)).pack(anchor="s")
ctk.CTkLabel(marco_info, text="📍Sucursal Apodaca (8 Disponibles)", font=("Arial", 14)).pack(anchor="s")

agregar = ctk.CTkButton(marco_producto,text="+", width=30,height=30,corner_radius=360, command=incrementar)
agregar.place(x=200,y=170)

quitar = ctk.CTkButton(marco_producto,text="-", width=30,height=30,corner_radius=360, command=decrementar)
quitar.place(x=10,y=170)

cantidad_label = ctk.CTkLabel(marco_info,text=f"Cantidad: {Cantidadllanta}",font=("Arial",16))
cantidad_label.pack(anchor="s")

agregar_compra = ctk.CTkButton(marco_info,text="Comprar",width=100,height=50,corner_radius=30)
agregar_compra.pack(padx=10,pady=10,anchor ="s")


ventana_principal.mainloop()