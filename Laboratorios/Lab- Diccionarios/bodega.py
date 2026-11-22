STOCK_MINIMO = 2

inventario = {"cadena": 2, "parche": 10, "pastillas": 4, "camara": 3}
precios = {"cadena": 15.00, "parche": 0.50, "pastillas": 6.00, "camara": 7.50}

while True:
    print("\n=== BODEGA · TALLER RUEDA LIBRE ===")
    print("1. Ver inventario")
    print("2. Consultar un repuesto")
    print("3. Registrar uso de repuestos")
    print("4. Recibir pedido del proveedor")
    print("5. Agregar repuesto nuevo")
    print("6. Descontinuar repuesto")
    print("7. Aplicar lista de precios nueva")
    print("8. Valor de la bodega")
    print("0. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        for repuesto, cantidad in inventario.items():
            if cantidad <= STOCK_MINIMO:
                print(f"{repuesto:<10} {cantidad:>4} <- pedir más")
            else:
                print(f"{repuesto:<10} {cantidad:>4}")
        print(f"Repuestos distintos: {len(inventario)}")

    elif opcion == "2":
        nombre = input("Repuesto: ").strip().lower()
        if nombre in inventario:
            print(f"{nombre}: {inventario[nombre]} unidades a ${precios[nombre]:.2f}")
        else:
            print("No existe. Repuestos registrados:", ", ".join(inventario.keys()))

    elif opcion == "3":
        nombre = input("Repuesto usado: ").strip().lower()
        if nombre not in inventario:
            print("Ese repuesto no existe.")
            continue
        texto = input("Unidades usadas: ").strip()
        if not texto.isdigit():
            print("Escriba un número entero.")
            continue
        cantidad = int(texto)
        if cantidad > inventario[nombre]:
            print(f"Solo hay {inventario[nombre]} unidades.")
        else:
            inventario[nombre] -= cantidad
            print(f"Quedan {inventario[nombre]} unidades de {nombre}.")

    elif opcion == "4":
        pedido = {}
        while True:
            nombre = input("Repuesto recibido (FIN para terminar): ").strip().lower()
            if nombre == "fin":
                break
            texto = input("Unidades: ").strip()
            if not texto.isdigit():
                print("Escriba un número entero.")
                continue
            pedido[nombre] = pedido.get(nombre, 0) + int(texto)

        for nombre, cantidad in pedido.items():
            inventario[nombre] = inventario.get(nombre, 0) + cantidad
            precios.setdefault(nombre, 0.0)
        print(f"Pedido registrado: {len(pedido)} repuesto(s) distinto(s).")

    elif opcion == "5":
        nombre = input("Nombre del repuesto nuevo: ").strip().lower()
        if nombre in inventario:
            print("Ese repuesto ya existe; use la opción 4 para sumar unidades.")
            continue
        inventario[nombre] = int(input("Unidades iniciales: "))
        precios[nombre] = float(input("Precio por unidad: "))
        print(f"{nombre} agregado a la bodega.")

    elif opcion == "6":
        nombre = input("Repuesto a descontinuar: ").strip().lower()
        if nombre in inventario:
            unidades = inventario.pop(nombre)
            precios.pop(nombre, None)
            print(f"{nombre} eliminado. Tenía {unidades} unidades.")
        else:
            print("Ese repuesto no existe.")

    elif opcion == "7":
        lista_proveedor = {"cadena": 16.50, "camara": 8.00}
        precios.update(lista_proveedor)
        print("Precios actualizados:", ", ".join(lista_proveedor.keys()))

    elif opcion == "8":
        valor_total = 0.0
        for repuesto in inventario:
            valor_total += inventario[repuesto] * precios[repuesto]
        print(f"Valor de la bodega: ${valor_total:.2f}")

    elif opcion == "0":
        print("Bodega cerrada.")
        break

    else:
        print("Opción no válida.")