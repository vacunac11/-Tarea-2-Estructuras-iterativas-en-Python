TARIFA_HORA = 12.00      # mano de obra, dólares por hora

bicis_recibidas = 0

while True:
    print("\n=== RECEPCIÓN · TALLER RUEDA LIBRE ===")
    print("1. Recibir bicicleta")
    print("2. Ver horario de atención")
    print("3. Cotizar mano de obra")
    print("0. Cerrar recepción")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        cliente = input("Nombre del cliente: ").strip()
        if cliente == "":
            print("El nombre no puede estar vacío.")
            continue
        bicis_recibidas += 1
        print(f"Bicicleta #{bicis_recibidas} recibida a nombre de {cliente}.")

    elif opcion == "2":
        print("Lunes a viernes de 8:00 a 17:00; sábado de 8:00 a 12:00.")

    elif opcion == "3":
        texto = input("Minutos de trabajo estimados: ").strip()
        if not texto.isdigit():
            print("Por favor ingresa solo números enteros.")
            continue
        minutos = int(texto)
        horas = minutos // 60
        resto = minutos % 60
        costo = minutos / 60 * TARIFA_HORA
        print(f"Trabajo de {horas} h {resto} min. Mano de obra: ${costo:.2f}")

    elif opcion == "0":
        confirmar = input("¿Cerrar la recepción? (s/n): ").strip().lower()
        if confirmar != "s":
            continue
        print(f"Recepción cerrada. Bicicletas recibidas hoy: {bicis_recibidas}.")
        break

    else:
        print("Opción no válida. Elige 0, 1, 2 o 3.")