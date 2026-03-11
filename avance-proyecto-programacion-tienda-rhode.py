# ============================================================
#               TIENDA RHODE - MENÚ DE PRODUCTOS
# ============================================================
# ================= ARREGLOS DE PRECIOS ======================
# En los arreglos colocamos el precio de los productos
preciosLip    = [16.00, 18.00, 20.00, 22.00, 30.00] #Precio de los labiales 
preciosFace = [24.00, 26.00, 22.00, 28.00, 30.00] #Precio de los blush
preciosLimited = [72.00, 56.00, 78.00, 29.00, 20.00] #Precio de Edición Limitada

# ================= CARRITO GENERAL ======================
carrito = [] #Una lista vacía que irá llenándose con los productos que el usuario elija.

# ================= FUNCIONES ======================
def menuPrincipal():
    # El input() muestra el menú y espera que el usuario escriba. Lo que escribe se guarda en opcion y se retorna al programa principal.
    opcion = input("""
╔══════════════════════════════╗
      BIENVENIDA A RHODE
╚══════════════════════════════╝
1. Lip Products (Labiales)
2. Face Color (Blush y más)
3. Limited Edition (Edición Limitada)
0. Salir
→ """)
    return opcion # devuelve "1", "2", "3" o "0"

def menuLip():
    opcion = input("""
── LIP PRODUCTS ──
1. Pep Lip
2. Lip Tint
3. Blush Lip
4. Barrier Lip
5. Lip Boost
0. Menú Principal
→ """)
    return opcion

def menuFace():
    opcion = input("""
── FACE COLOR ──
1. Pocket Blush
2. Teddy Blush
3. Freckle Tint
4. Glow Balm
5. Soft Sculpt
0. Menú Principal
→ """)
    return opcion

def menuLimited():
    opcion = input("""
── LIMITED EDITION ──
1. Lip Tint
2. Lip Trio
3. Winter
4. Mascara
5. Blush
0. Menú Principal
→ """)
    return opcion

# ================= AGREGAR AL CARRITO ======================
def agregarCarrito(nombre, cantidad, precio): #Recibe 3 parámetros y los mete como una lista dentro del carrito usando `.append()`.
    carrito.append([nombre, cantidad, precio]) #append() agrega un elemento al final de la lista.

# ================= FACTURA FINAL ======================
def mostrarFactura():
    print("""
╔══════════════════════════════════╗
           FACTURA RHODE
╚══════════════════════════════════╝
""")
    total = 0
    for producto in carrito: # El for recorre cada producto del carrito uno por uno y calcula el subtotal de cada uno, acumulándolo en total.
        nombre = producto[0] # extrae posición 0 → nombre
        cantidad = producto[1] # extrae posición 1 → cantidad
        precio = producto[2] # extrae posición 2 → precio
        subtotal = cantidad * precio
        total += subtotal # va acumulando el total
        print(f"Producto : {nombre}")
        print(f"Cantidad : {cantidad}")
        print(f"Precio   : L.{precio:.2f}")
        print(f"Subtotal : L.{subtotal:.2f}")
        print("-----------------------------")
    print(f"\nTOTAL FINAL: L.{total:.2f}") #El :.2f significa mostrar exactamente 2 decimales
    print("""
╔══════════════════════════════════╗
     Gracias por comprar en RHODE
╚══════════════════════════════════╝
""")

# ================= PROGRAMA PRINCIPAL ======================

otroproducto = '1'  # Variable para saber si el cliente quiere seguir comprando
while otroproducto == '1':
    opcionm1 = menuPrincipal() # llama al menú y guarda lo que eligió
    # ================= LIP PRODUCTS ======================
    if opcionm1 == '1': # eligió Lip Products
        opcionm2 = menuLip() # muestra submenú de labiales
        if opcionm2 == '1':
            nombre = "Pep Lip"
            precio = preciosLip[0]  # busca el precio en el arreglo
        elif opcionm2 == '2':
            nombre = "Lip Tint"
            precio = preciosLip[1]
        elif opcionm2 == '3':
            nombre = "Blush Lip"
            precio = preciosLip[2]
        elif opcionm2 == '4':
            nombre = "Barrier Lip"
            precio = preciosLip[3]
        elif opcionm2 == '5':
            nombre = "Lip Boost"
            precio = preciosLip[4]
        elif opcionm2 == '0':
            continue # vuelve al inicio del while sin comprar
        else:
            print("Opción inválida")
            continue

    # ================= FACE COLOR ======================
    elif opcionm1 == '2': # eligió Face Color
        opcionm2 = menuFace() 
        if opcionm2 == '1':
            nombre = "Pocket Blush"
            precio = preciosFace[0]
        elif opcionm2 == '2':
            nombre = "Teddy Blush"
            precio = preciosFace[1]
        elif opcionm2 == '3':
            nombre = "Freckle Tint"
            precio = preciosFace[2]
        elif opcionm2 == '4':
            nombre = "Glow Balm"
            precio = preciosFace[3]
        elif opcionm2 == '5':
            nombre = "Soft Sculpt"
            precio = preciosFace[4]
        elif opcionm2 == '0':
            continue
        else:
            print("Opción inválida")
            continue

    # ================= LIMITED EDITION ======================
    elif opcionm1 == '3': # eligió Limited Edition
        opcionm2 = menuLimited()
        if opcionm2 == '1':
            nombre = "Lip Tint"
            precio = preciosLimited[0]
        elif opcionm2 == '2':
            nombre = "Lip Trio"
            precio = preciosLimited[1]
        elif opcionm2 == '3':
            nombre = "Winter"
            precio = preciosLimited[2]
        elif opcionm2 == '4':
            nombre = "Mascara"
            precio = preciosLimited[3]
        elif opcionm2 == '5':
            nombre = "Blush"
            precio = preciosLimited[4]
        elif opcionm2 == '0':
            continue
        else:
            print("Opción inválida")
            continue

    # ================= SALIR ======================
    elif opcionm1 == '0':
        mostrarFactura() # muestra todo lo comprado
        break # rompe el while y termina el programa
    else:
        print("Opción inválida")
        continue

    # ================= CANTIDAD ======================
    cantidad = int(input(f"¿Cuántos '{nombre}' deseas? → "))
    agregarCarrito(nombre, cantidad, precio)
    subtotal = cantidad * precio
    print(f"\nProducto: {nombre}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: L.{subtotal:.2f}")
    #Solo llega aquí si se eligió un producto válido. Convierte el input a int, agrega al carrito, y muestra un resumen rápido.

    # ================= OTRO PRODUCTO ======================
    otroproducto = input("""
¿Deseas agregar otro producto?
1. Sí
2. No
→ """)
    if otroproducto != '1':
        mostrarFactura()
        break #Si el usuario escribe cualquier cosa que no sea '1', muestra la factura y termina.



