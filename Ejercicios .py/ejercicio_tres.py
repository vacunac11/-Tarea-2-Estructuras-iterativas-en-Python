# ==============================================================================
# Nombre del archivo: ejercicio3_estacionamiento.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: [Tu Nombre Completo]
# Fecha: 22 de noviembre, 2026
# Versión: 1.4
# Descripción: Sistema de administración de estacionamiento privado con menú
#              repetitivo mediante while True y condicionales múltiples.
# ==============================================================================

# Constantes del programa
CAPACIDAD_MAXIMA = 20
TARIFA_POR_HORA = 800

# Inicialización de contadores y acumuladores
vehiculos_presentes = 0
salidas_registradas = 0
recaudacion_total = 0

# Ciclo principal del menú repetitivo
while True:
    print("\n==============================================")
    print("   ADMINISTRACIÓN DE ESTACIONAMIENTO PRIVADO  ")
    print("==============================================")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupación")
    print("4. Consultar recaudación")
    print("5. Salir")
    print("==============================================")
    
    opcion = int(input("Seleccione una opción (1-5): "))
    
    if opcion == 1:
        if vehiculos_presentes < CAPACIDAD_MAXIMA:
            vehiculos_presentes = vehiculos_presentes + 1
            print("\n[ÉXITO] Vehículo ingresado correctamente.")
            print("Vehículos actualmente estacionados:", vehiculos_presentes)
            print("Espacios libres restantes:", CAPACIDAD_MAXIMA - vehiculos_presentes)
        else:
            print("\n[ERROR] Estacionamiento lleno. No hay espacios disponibles (Máximo 20).")
            
    elif opcion == 2:
        if vehiculos_presentes > 0:
            horas_cobrar = int(input("Ingrese la cantidad de horas a cobrar: "))
            
            # Validación con ciclo while para horas estrictamente mayores a 0
            while horas_cobrar <= 0:
                print("[ERROR] Las horas cobradas deben ser estrictamente mayores a 0.")
                horas_cobrar = int(input("Ingrese una cantidad de horas válida: "))
                
            monto_pago = horas_cobrar * TARIFA_POR_HORA
            vehiculos_presentes = vehiculos_presentes - 1
            salidas_registradas = salidas_registradas + 1
            recaudacion_total = recaudacion_total + monto_pago
            
            print("\n[ÉXITO] Salida procesada.")
            print("Monto a cobrar:", monto_pago, "colones")
            print("Vehículos restantes:", vehiculos_presentes)
        else:
            print("\n[ERROR] No hay vehículos dentro del estacionamiento para procesar una salida.")
            
    elif opcion == 3:
        espacios_libres = CAPACIDAD_MAXIMA - vehiculos_presentes
        print("\n--- ESTADO DE OCUPACIÓN ---")
        print("Espacios ocupados:", vehiculos_presentes)
        print("Espacios libres:", espacios_libres)
        
    elif opcion == 4:
        print("\n--- RESUMEN DE RECAUDACIÓN ---")
        print("Monto total recaudado:", recaudacion_total, "colones")
        print("Cantidad de vehículos procesados (salidas):", salidas_registradas)
        
    elif opcion == 5:
        print("\n==============================================")
        print("         RESUMEN FINAL DE LA SESIÓN           ")
        print("==============================================")
        print("Vehículos que permanecen estacionados:", vehiculos_presentes)
        print("Total de salidas procesadas:", salidas_registradas)
        print("Recaudación total lograda:", recaudacion_total, "colones")
        print("==============================================")
        print("Programa finalizado.")
        break
        
    else:
        print("\n[ERROR] Opción no válida. Ingrese un número del 1 al 5.")