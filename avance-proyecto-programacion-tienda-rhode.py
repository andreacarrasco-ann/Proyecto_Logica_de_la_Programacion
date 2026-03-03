# ============================================================
#               TIENDA RHODE - MENÚ DE PRODUCTOS
# ============================================================

preciosLip    = [16.00, 18.00, 20.00, 22.00, 30.00]
otroproducto = '1'  # Variable para saber si el cliente quiere seguir comprando
total = 0.0         # Total acumulado de la compra

while otroproducto == '1':

    # ======================== MENÚ PRINCIPAL ========================
    opcionm1 = input("""
╔══════════════════════════════╗
       BIENVENIDA A RHODE     
╚══════════════════════════════╝
 1. Lip Products (Labiales)
 2. Face Color (Blush y más)
 3. Limited Edition (Edición Limitada) 
 0. Salir
→ """)

    # ======================== 1. LIP PRODUCTS ========================
    if opcionm1 == '1':

        opcionm2 = input("""
── LIP PRODUCTS ──
 1. Pep Lip 
 2. Lip Tint
 3. Blush Lip
 4. Barrier Lip
 5. Lip Boost
 0. Menú Principal
→ """)

        if opcionm2 == '1':
            precio = preciosLip[0]
            nombre = "Pep Lip"
        elif opcionm2 == '2':
            precio = preciosLip[1]
            nombre = "Lip Tint"
        elif opcionm2 == '3':
            precio = preciosLip[2]
            nombre = "Blush Lip"
        elif opcionm2 == '4':
            precio = preciosLip[3]
            nombre = "Barrier Lip"
        elif opcionm2 == '5':
            precio = preciosLip[4]
            nombre = "Lip Boost"
        elif opcionm2 == '0':
            print("\n↩ Regresando al Menú Principal...")
            continue
        else:
            print("\n Opción inválida. Intenta de nuevo.")
            continue

        cantidad = int(input(f"¿Cuántos '{nombre}' deseas? → "))
        subtotal = precio * cantidad
        total += subtotal

        print(f"\n Producto:  {nombre}")
        print(f"   Cantidad:  {cantidad}")
        print(f"   Subtotal:  L.{subtotal:.2f}")
        print(f"   Total acumulado: L.{total:.2f}")




    # ======================== 2. FACE COLOR ========================
    elif opcionm1 == '2':

        opcionm2 = input("""
── FACE COLOR ──
 1. Pocket Blush
 2. Toasted Teddy Blush
 3. Freckle Tint
 4. Glow Balm Highlighter
 5. Soft Sculpt Bronzer
 0. Menú Principal
→ """)

        if opcionm2 == '1':
            precio = 24.00
            nombre = "Pocket Blush"
        elif opcionm2 == '2':
            precio = 26.00
            nombre = "Toasted Teddy Blush"
        elif opcionm2 == '3':
            precio = 22.00
            nombre = "Freckle Tint"
        elif opcionm2 == '4':
            precio = 28.00
            nombre = "Glow Balm Highlighter"
        elif opcionm2 == '5':
            precio = 30.00
            nombre = "Soft Sculpt Bronzer"
        elif opcionm2 == '0':
            print("\n↩ Regresando al Menú Principal...")
            continue
        else:
            print("\n Opción inválida. Intenta de nuevo.")
            continue

        cantidad = int(input(f"¿Cuántos '{nombre}' deseas? → "))
        subtotal = precio * cantidad
        total += subtotal

        print(f"\n Producto:  {nombre}")
        print(f"   Cantidad:  {cantidad}")
        print(f"   Subtotal:  L.{subtotal:.2f}")
        print(f"   Total acumulado: L.{total:.2f}")


    # ======================== 3. LIMITED EDITION ========================
    elif opcionm1 == '3':

        opcionm2 = input("""
── LIMITED EDITION ──
 1. Scented Peptide Lip Tint Set
 2. Peptide Lip Trio Set
 3. Winter Limited Kit
 4. Lemontini Limited Lip Tint
 5. Limited Edition Pocket Blush
 0. Menú Principal
→ """)

        if opcionm2 == '1':
            precio = 72.00  
            nombre = "Scented Peptide Lip Tint Set"
        elif opcionm2 == '2':
            precio = 56.00  # Trio de tintes
            nombre = "Peptide Lip Trio Set"
        elif opcionm2 == '3':
            precio = 78.00  
            nombre = "Winter Limited Kit"
        elif opcionm2 == '4':
            precio = 29.00  
            nombre = "Lemontini Limited Lip Tint"
        elif opcionm2 == '5':
            precio = 20.00   
            nombre = "Limited Edition Pocket Blush"
        elif opcionm2 == '0':
            print("\n↩ Regresando al Menú Principal...")
            continue
        else:
            print("\n Opción inválida. Intenta de nuevo.")
            continue

        cantidad = int(input(f"¿Cuántos '{nombre}' deseas? → "))
        subtotal = precio * cantidad
        total += subtotal

        print(f"\n Producto:  {nombre}")
        print(f"   Cantidad:  {cantidad}")
        print(f"   Subtotal:  L.{subtotal:.2f}")
        print(f"   Total acumulado: L.{total:.2f}")



    # ======================== SALIR ========================
    elif opcionm1 == '0':
        print(f"""
╔══════════════════════════════╗
   Gracias por visitar Rhode 
   Total de tu compra: L.{total:.2f}
   
╚══════════════════════════════╝
""")
        break

    else:
        print("\n Opción inválida. Intenta de nuevo.")
        continue

    # ======================== ¿OTRO PRODUCTO? ========================
    otroproducto = input("""
¿Deseas agregar otro producto?
 1. Sí
 2. No
→ """)

    if otroproducto != '1':
        print(f"""
╔══════════════════════════════╗
   Gracias por visitar Rhode 
   Total de tu compra: L.{total:.2f}
   
╚══════════════════════════════╝
""")
        break



