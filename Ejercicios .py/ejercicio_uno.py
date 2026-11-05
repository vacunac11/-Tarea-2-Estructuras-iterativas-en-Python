# ==============================================================================
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Valeria Acuña Castillo
# Fecha: 22 de noviembre, 2026
# Versión: 1.0
# Descripción: Simulación del control de temperatura de una cámara experimental.
# ==============================================================================

# Entrada de datos
temperatura_inicial = float(input("Ingrese la temperatura inicial (°C): "))
temperatura_objetivo = float(input("Ingrese la temperatura objetivo (°C): "))
incremento = float(input("Ingrese el incremento constante por ciclo (°C): "))

# Bloque de decisiones
if temperatura_objetivo <= temperatura_inicial:
    print("Error: La temperatura objetivo debe ser mayor que la inicial.")
elif incremento <= 0:
    print("Error: El incremento debe ser mayor que cero.")
else:
    # Previo al ciclo
    temperatura_actual = temperatura_inicial
    ciclos = 0

    print("\n Inicio de la simulación de calentamiento")

    # Ciclo
    while temperatura_actual < temperatura_objetivo:
        temperatura_actual = temperatura_actual + incremento
        ciclos = ciclos + 1
        print("Ciclo", ciclos, "-> Temperatura:", temperatura_actual, "°C")

    # Salida
    print("\n Resultados de la simulación")
    print("Temperatura final alcanzada:", temperatura_actual, "°C")
    print("Total de ciclos ejecutados:", ciclos)