cola = []
atendidos = 0

while True:
    print("\n=== COLA DE ESPERA · TALLER RUEDA LIBRE ===")
    print(f"Clientes en espera: {len(cola)}")
    print("1. Llega un cliente")
    print("2. Llega un cliente urgente")
    print("3. Llega un grupo")
    print("4. Atender al siguiente")
    print("5. Un cliente se retira")
    print("6. Consultar posición")
    print("7. Ver la cola")
    print("0. Cerrar el día")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        nombre = input("Nombre: ").strip().title()
        cola.append(nombre)
        print(f"{nombre} está en la posición {len(cola)}.")

    elif opcion == "2":
        nombre = input("Nombre: ").strip().title()
        cola.insert(0, nombre)
        print(f"{nombre} pasa al primer lugar.")

    elif opcion == "3":
        texto = input("Nombres separados por coma: ")
        grupo = []
        for nombre in texto.split(","):
            nombre = nombre.strip().title()
            if nombre != "":
                grupo.append(nombre)
        cola.extend(grupo)
        print(f"Se agregaron {len(grupo)} clientes al final de la cola.")

    elif opcion == "4":
        if len(cola) == 0:
            print("No hay nadie esperando.")
        else:
            siguiente = cola.pop(0)
            atendidos += 1
            print(f"Pase {siguiente}, por favor.")

    elif opcion == "5":
        nombre = input("¿Quién se retira? ").strip().title()
        if nombre in cola:
            cola.remove(nombre)
            print(f"{nombre} salió de la cola.")
        else:
            print(f"{nombre} no está en la cola.")

    elif opcion == "6":
        nombre = input("Nombre: ").strip().title()
        if nombre in cola:
            posicion = cola.index(nombre) + 1
            print(f"{nombre} está en la posición {posicion}.")
            print(f"Tiene {posicion - 1} persona(s) delante.")
            veces = cola.count(nombre)
            if veces > 1:
                print(f"{nombre} aparece {veces} veces: trajo varias bicicletas.")
        else:
            print(f"{nombre} no está en la cola.")

    elif opcion == "7":
        if len(cola) == 0:
            print("La cola está vacía.")
        else:
            for i in range(len(cola)):
                print(f"{i + 1}. {cola[i]}")
            print("Próximos tres:", ", ".join(cola[:3]))
            print("Lista alfabética:", ", ".join(sorted(cola)))

    elif opcion == "0":
        pendientes = cola.copy()
        cola.clear()
        print(f"Clientes atendidos hoy: {atendidos}")
        if len(pendientes) > 0:
            print("Quedaron sin atender:", ", ".join(pendientes))
        break

    else:
        print("Opción no válida.")