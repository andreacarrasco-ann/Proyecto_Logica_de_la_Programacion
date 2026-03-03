# ============================================================
#               TIENDA RHODE - MENÚ DE PRODUCTOS
# ============================================================
# ================= ARREGLOS DE PRECIOS ======================
preciosLip    = [16.00, 18.00, 20.00, 22.00, 30.00]
preciosFace = [24.00, 26.00, 22.00, 28.00, 30.00]
preciosLimited = [72.00, 56.00, 78.00, 29.00, 20.00]
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
 2. Teddy Blush
 3. Freckle Tint
 4. Glow Balm
 5. Soft Sculpt
 0. Menú Principal
→ """)

        if opcionm2 == '1':
            precio = preciosFace[0]
            nombre = "Pocket Blush"
        elif opcionm2 == '2':
            precio = preciosFace[1]
            nombre = "Teddy Blush"
        elif opcionm2 == '3':
            precio = preciosFace[2]
            nombre = "Freckle Tint"
        elif opcionm2 == '4':
            precio = preciosFace[3]
            nombre = "Glow Balm"
        elif opcionm2 == '5':
            precio = preciosFace[4]
            nombre = "Soft Sculpt"
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
 1. Lip Tint
 2. Lip Trio
 3. Winter
 4. Mascara
 5. Blush
 0. Menú Principal
→ """)

        if opcionm2 == '1':
            precios = preciosLimited[0] 
            nombre = "Lip Tint"
        elif opcionm2 == '2':
            precios = preciosLimited[1]  # Trio de tintes
            nombre = "Lip Trio"
        elif opcionm2 == '3':
            precios = preciosLimited[2] 
            nombre = "Winter"
        elif opcionm2 == '4':
            precios = preciosLimited[3] 
            nombre = "Mascara"
        elif opcionm2 == '5':
            precios = preciosLimited[4] 
            nombre = "Blush"
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











