# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Valeria Acuña Castillo
# Fecha: 22 de noviembre, 2026
# Versión: 1.0
# Descripción: Simulación y control diario de abastecimiento de agua y alimento durante una expedición.

# Declaración de constantes
AGUA_INICIAL = 150.0
ALIMENTO_INICIAL = 100.0
MIN_JORNADAS = 1
MAX_JORNADAS = 30

# Inicialización de variables 
agua_disponible = AGUA_INICIAL
alimento_disponible = ALIMENTO_INICIAL

agua_consumida_total = 0.0
alimento_consumido_total = 0.0
dias_completados = 0
expedicion_interrumpida = False

print("=== SISTEMA DE CONTROL DE ABASTECIMIENTO DE EXPEDICIÓN ===")
print(f"Suministros iniciales -> Agua: {agua_disponible} L | Alimento: {alimento_disponible} unid.\n")

# Solicitud y validación de jornadas planeadas
jornadas_planeadas = int(input(f"Ingrese la cantidad de jornadas planeadas ({MIN_JORNADAS}-{MAX_JORNADAS}): "))

while jornadas_planeadas < MIN_JORNADAS or jornadas_planeadas > MAX_JORNADAS:
    print(f"[ERROR] La cantidad de jornadas debe ser un entero entre {MIN_JORNADAS} y {MAX_JORNADAS}.")
    jornadas_planeadas = int(input(f"Ingrese la cantidad de jornadas planeadas ({MIN_JORNADAS}-{MAX_JORNADAS}): "))

# Simulación de jornadas
for dia in range(1, jornadas_planeadas + 1):
    # Comprobar al inicio si existen recursos disponibles
    if agua_disponible <= 0 or alimento_disponible <= 0:
        expedicion_interrumpida = True
        break

    print(f"\n--- JORNADA {dia} DE {jornadas_planeadas} ---")
    print(f"Disponible al iniciar -> Agua: {agua_disponible:.2f} L | Alimento: {alimento_disponible:.2f} unid.")

    # Solicitud y validación de consumo de agua 
    consumo_agua = float(input("Ingrese los litros de agua consumidos hoy: "))
    while consumo_agua <= 0 or consumo_agua > agua_disponible:
        if consumo_agua <= 0:
            print("[ERROR] El consumo de agua debe ser una cantidad positiva mayor a 0.")
        else:
            print(f"[ERROR] El consumo excede el agua disponible ({agua_disponible:.2f} L).")
        consumo_agua = float(input("Ingrese los litros de agua consumidos hoy: "))

    # Solicitud y validación de consumo de alimento 
    consumo_alimento = float(input("Ingrese las unidades de alimento consumidas hoy: "))
    while consumo_alimento <= 0 or consumo_alimento > alimento_disponible:
        if consumo_alimento <= 0:
            print("[ERROR] El consumo de alimento debe ser una cantidad positiva mayor a 0.")
        else:
            print(f"[ERROR] El consumo excede el alimento disponible ({alimento_disponible:.2f} unid.).")
        consumo_alimento = float(input("Ingrese las unidades de alimento consumidas hoy: "))

    # Descuento de existencias y actualización de acumuladores
    agua_disponible = agua_disponible - consumo_agua
    alimento_disponible = alimento_disponible - consumo_alimento

    agua_consumida_total = agua_consumida_total + consumo_agua
    alimento_consumido_total = alimento_consumido_total + consumo_alimento
    dias_completados = dias_completados + 1

    print(f"[REGISTRO] Jornada {dia} completada.")
    print(f"Saldo restante -> Agua: {agua_disponible:.2f} L | Alimento: {alimento_disponible:.2f} unid.")

    # Verificar si algún recurso llegó exactamente a 0 teniendo jornadas pendientes
    if (agua_disponible == 0 or alimento_disponible == 0) and dia < jornadas_planeadas:
        print("\n[ALERTA CRÍTICA] Uno o más suministros se han agotado por completo.")
        print("No es posible continuar al día siguiente. Interrumpiendo expedición...")
        expedicion_interrumpida = True
        break

# Cálculo de promedios diarios sobre los días realmente completados
if dias_completados > 0:
    promedio_agua = agua_consumida_total / dias_completados
    promedio_alimento = alimento_consumido_total / dias_completados
else:
    promedio_agua = 0.0
    promedio_alimento = 0.0

# Determinación del estado final de la expedición
if expedicion_interrumpida:
    estado_expedicion = "INTERRUMPIDA ANTICIPADAMENTE POR AGOTAMIENTO DE SUMINISTROS"
else:
    estado_expedicion = "COMPLETADA EXITOSAMENTE"

# Informe final
print("\n============================================================")
print("             INFORME FINAL DE LA EXPEDICIÓN                 ")
print("============================================================")
print(f"Estado de la expedición   : {estado_expedicion}")
print(f"Días completados          : {dias_completados} de {jornadas_planeadas}")
print(f"Agua total consumida      : {agua_consumida_total:.2f} L")
print(f"Alimento total consumido  : {alimento_consumido_total:.2f} unid.")
print(f"Agua restante             : {agua_disponible:.2f} L")
print(f"Alimento restante         : {alimento_disponible:.2f} unid.")
print(f"Promedio diario agua      : {promedio_agua:.2f} L/día")
print(f"Promedio diario alimento  : {promedio_alimento:.2f} unid./día")
print("============================================================")