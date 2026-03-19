# ============================================================
#               TIENDA RHODE - MENÚ DE PRODUCTOS
#               (Con Clases y Objetos + Carrito simple)
# ============================================================

# ================= DECLARACIÓN DE CLASE ======================
class Producto:
    # Constructor
    def __init__(self, nombre, precio, categoria, codigo):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.codigo = codigo

    # Método para mostrar info del producto
    def describir(self):
        return f"[{self.codigo}] {self.nombre} | Categoría: {self.categoria} | Precio: L.{self.precio:.2f}"


# ================= ARREGLOS DE PRECIOS ======================
preciosLip     = [16.00, 18.00, 20.00, 22.00, 30.00]
preciosFace    = [24.00, 26.00, 22.00, 28.00, 30.00]
preciosLimited = [72.00, 56.00, 78.00, 29.00, 20.00]

# ================= CARRITO GENERAL ======================
carrito = []  # Guardará: [nombre, cantidad, precio]

# ================= FUNCIONES DE MENÚ ======================
def menuPrincipal():
    opcion = input("""
╔══════════════════════════════╗
      BIENVENIDA A RHODE
╚══════════════════════════════╝
1. Lip Products (Labiales)
2. Face Color (Blush y más)
3. Limited Edition (Edición Limitada)
0. Salir
→ """)
    return opcion

def menuLip():
    opcion = input("""
── LIP PRODUCTS ──
1. Pep Lip       L.{:.2f}
2. Lip Tint      L.{:.2f}
3. Blush Lip     L.{:.2f}
4. Barrier Lip   L.{:.2f}
5. Lip Boost     L.{:.2f}
0. Menú Principal
→ """.format(*preciosLip))
    return opcion

def menuFace():
    opcion = input("""
── FACE COLOR ──
1. Pocket Blush  L.{:.2f}
2. Teddy Blush   L.{:.2f}
3. Freckle Tint  L.{:.2f}
4. Glow Balm     L.{:.2f}
5. Soft Sculpt   L.{:.2f}
0. Menú Principal
→ """.format(*preciosFace))
    return opcion

def menuLimited():
    opcion = input("""
── LIMITED EDITION ──
1. Lip Tint      L.{:.2f}
2. Lip Trio      L.{:.2f}
3. Winter        L.{:.2f}
4. Mascara       L.{:.2f}
5. Blush         L.{:.2f}
0. Menú Principal
→ """.format(*preciosLimited))
    return opcion


# ================= AGREGAR AL CARRITO ======================
# Carrito igual al código anterior: nombre, cantidad, precio
def agregarCarrito(producto, cantidad):
    carrito.append([producto.nombre, cantidad, producto.precio])


# ================= FACTURA FINAL ======================
def mostrarFactura():
    print("""
╔══════════════════════════════════╗
           FACTURA RHODE
╚══════════════════════════════════╝
""")
    total = 0
    for item in carrito:
        nombre = item[0]
        cantidad = item[1]
        precio = item[2]
        subtotal = cantidad * precio
        total += subtotal

        print(f"Producto : {nombre}")
        print(f"Cantidad : {cantidad}")
        print(f"Precio   : L.{precio:.2f}")
        print(f"Subtotal : L.{subtotal:.2f}")
        print("-----------------------------")

    print(f"\nTOTAL FINAL: L.{total:.2f}")
    print("""
╔══════════════════════════════════╗
     Gracias por comprar en RHODE
╚══════════════════════════════════╝
""")


# ================= PROGRAMA PRINCIPAL ======================
otroproducto = '1'

while otroproducto == '1':
    opcionm1 = menuPrincipal()

    # ================= LIP PRODUCTS ======================
    if opcionm1 == '1':
        opcionm2 = menuLip()
        if opcionm2 == '1':
            productoElegido = Producto("Pep Lip", preciosLip[0], "Lip Products", 101)
        elif opcionm2 == '2':
            productoElegido = Producto("Lip Tint", preciosLip[1], "Lip Products", 102)
        elif opcionm2 == '3':
            productoElegido = Producto("Blush Lip", preciosLip[2], "Lip Products", 103)
        elif opcionm2 == '4':
            productoElegido = Producto("Barrier Lip", preciosLip[3], "Lip Products", 104)
        elif opcionm2 == '5':
            productoElegido = Producto("Lip Boost", preciosLip[4], "Lip Products", 105)
        elif opcionm2 == '0':
            continue
        else:
            print("Opción inválida")
            continue

    # ================= FACE COLOR ======================
    elif opcionm1 == '2':
        opcionm2 = menuFace()
        if opcionm2 == '1':
            productoElegido = Producto("Pocket Blush", preciosFace[0], "Face Color", 201)
        elif opcionm2 == '2':
            productoElegido = Producto("Teddy Blush", preciosFace[1], "Face Color", 202)
        elif opcionm2 == '3':
            productoElegido = Producto("Freckle Tint", preciosFace[2], "Face Color", 203)
        elif opcionm2 == '4':
            productoElegido = Producto("Glow Balm", preciosFace[3], "Face Color", 204)
        elif opcionm2 == '5':
            productoElegido = Producto("Soft Sculpt", preciosFace[4], "Face Color", 205)
        elif opcionm2 == '0':
            continue
        else:
            print("Opción inválida")
            continue

    # ================= LIMITED EDITION ======================
    elif opcionm1 == '3':
        opcionm2 = menuLimited()
        if opcionm2 == '1':
            productoElegido = Producto("Lip Tint", preciosLimited[0], "Limited Edition", 301)
        elif opcionm2 == '2':
            productoElegido = Producto("Lip Trio", preciosLimited[1], "Limited Edition", 302)
        elif opcionm2 == '3':
            productoElegido = Producto("Winter", preciosLimited[2], "Limited Edition", 303)
        elif opcionm2 == '4':
            productoElegido = Producto("Mascara", preciosLimited[3], "Limited Edition", 304)
        elif opcionm2 == '5':
            productoElegido = Producto("Blush", preciosLimited[4], "Limited Edition", 305)
        elif opcionm2 == '0':
            continue
        else:
            print("Opción inválida")
            continue

    # ================= SALIR ======================
    elif opcionm1 == '0':
        mostrarFactura()
        break
    else:
        print("Opción inválida")
        continue

    # ================= CANTIDAD ======================
    cantidad = int(input(f"¿Cuántos '{productoElegido.nombre}' deseas? → "))

    print("\n" + productoElegido.describir())

    # Agregar al carrito (formato simple)
    agregarCarrito(productoElegido, cantidad)

    subtotal = cantidad * productoElegido.precio
    print(f"Cantidad : {cantidad}")
    print(f"Subtotal : L.{subtotal:.2f}")

    # ================= OTRO PRODUCTO ======================
    otroproducto = input("""
¿Deseas agregar otro producto?
1. Sí
2. No
→ """)
    if otroproducto != '1':
        mostrarFactura()
        break

