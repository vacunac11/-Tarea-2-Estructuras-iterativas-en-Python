# Catálogo: código -> (nombre, precio, repuesto que consume)
SERVICIOS = {
    "FR": ("Ajuste de frenos", 8.00, "pastillas"),
    "CA": ("Cambio de cadena", 15.00, "cadena"),
    "PA": ("Parchado de llanta", 5.00, "parche"),
    "MG": ("Mantenimiento general", 35.00, None),
}

inventario = {"pastillas": 4, "cadena": 2, "parche": 10}
ordenes = []
siguiente_numero = 1

while True:
    print("\n=== TALLER RUEDA LIBRE ===")
    print("1. Ver catálogo de servicios")
    print("2. Registrar orden")
    print("3. Ver órdenes pendientes")
    print("4. Entregar orden")
    print("5. Ver inventario")
    print("6. Reporte del día")
    print("0. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        print("\nCódigo  Servicio                 Precio")
        for codigo, datos in SERVICIOS.items():
            nombre, precio, repuesto = datos
            print(f"{codigo:<7} {nombre:<24} ${precio:>6.2f}")

    elif opcion == "2":
        cliente = input("Nombre del cliente: ").strip()
        servicios_orden = []
        total = 0.0

        while True:
            codigo = input("Código de servicio (FIN para terminar): ").strip().upper()
            if codigo == "FIN":
                break
            if codigo not in SERVICIOS:
                print("  Código no existe.")
                continue

            nombre, precio, repuesto = SERVICIOS[codigo]

            if repuesto is not None:
                if inventario[repuesto] == 0:
                    print(f"  Sin {repuesto} en bodega. No se puede agregar.")
                    continue
                inventario[repuesto] -= 1

            servicios_orden.append(codigo)
            total += precio
            print(f"  + {nombre} (${precio:.2f})")

        if len(servicios_orden) == 0:
            print("Orden cancelada: no tiene servicios.")
        else:
            orden = {
                "numero": siguiente_numero,
                "cliente": cliente,
                "servicios": servicios_orden,
                "total": total,
                "estado": "pendiente",
            }
            ordenes.append(orden)
            print(f"Orden #{siguiente_numero} registrada. Total: ${total:.2f}")
            siguiente_numero += 1

    elif opcion == "3":
        hay_pendientes = False
        for orden in ordenes:
            if orden["estado"] == "pendiente":
                hay_pendientes = True
                codigos = ", ".join(orden["servicios"])
                print(f"#{orden['numero']} {orden['cliente']:<12} {codigos:<15} ${orden['total']:.2f}")
        if not hay_pendientes:
            print("No hay órdenes pendientes.")

    elif opcion == "4":
        texto = input("Número de orden: ").strip()
        if not texto.isdigit():
            print("Escriba un número.")
            continue
        numero = int(texto)
        encontrada = False
        for orden in ordenes:
            if orden["numero"] == numero:
                encontrada = True
                if orden["estado"] == "entregada":
                    print("Esa orden ya fue entregada.")
                else:
                    orden["estado"] = "entregada"
                    print(f"Orden #{numero} entregada a {orden['cliente']}.")
                    print(f"Cobrar ${orden['total']:.2f}")
        if not encontrada:
            print("No existe esa orden.")

    elif opcion == "5":
        for repuesto, cantidad in inventario.items():
            if cantidad <= 1:
                print(f"{repuesto:<10} {cantidad:>3} <- reabastecer")
            else:
                print(f"{repuesto:<10} {cantidad:>3}")

    elif opcion == "6":
        ingresos = 0.0
        entregadas = 0
        conteo = {}
        for orden in ordenes:
            if orden["estado"] == "entregada":
                entregadas += 1
                ingresos += orden["total"]
            for codigo in orden["servicios"]:
                conteo[codigo] = conteo.get(codigo, 0) + 1

        print(f"Órdenes registradas: {len(ordenes)}")
        print(f"Órdenes entregadas: {entregadas}")
        print(f"Ingresos cobrados: ${ingresos:.2f}")

        if len(conteo) > 0:
            mas_pedido = ""
            maximo = 0
            for codigo, veces in conteo.items():
                if veces > maximo:
                    maximo = veces
                    mas_pedido = codigo
            nombre_servicio = SERVICIOS[mas_pedido][0]
            print(f"Servicio más pedido: {nombre_servicio} ({maximo} veces)")

    elif opcion == "0":
        print("Hasta luego.")
        break

    else:
        print("Opción no válida.")