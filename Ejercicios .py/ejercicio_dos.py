# ==============================================================================
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Valeria Acuña Castillo
# Fecha: 22 de noviembre, 2026
# Versión: 1.0
# Descripción: Registro diario de consumo de agua durante 7 días consecutivos.
# ==============================================================================

# Constantes del programa
TOTAL_DIAS = 7
UMBRAL_CONSUMO = 150.0

# Inicialización de acumuladores y contadores
consumo_total = 0.0
dias_superan_umbral = 0
mayor_consumo = 0.0

print("--- Registro Semanal de Consumo de Agua ---")
print("Ingrese el consumo de agua en litros para cada uno de los 7 días.\n")

# Ciclo del 1 al 7
for dia in range(1, TOTAL_DIAS + 1):
    print("Día", dia)
    consumo_dia = float(input("Ingrese el consumo en litros: "))
    
    # Validación con ciclo while: el consumo no puede ser negativo
    while consumo_dia < 0:
        print("Error: El consumo de agua no puede ser menor a 0 litros.")
        consumo_dia = float(input("Ingrese un consumo válido en litros: "))
    
    # Acumular el consumo total semanal
    consumo_total = consumo_total + consumo_dia
    
    # Evaluar el mayor consumo registrado sin funciones built-in
    if dia == 1:
        mayor_consumo = consumo_dia
    elif consumo_dia > mayor_consumo:
        mayor_consumo = consumo_dia
        
    # Contar si el consumo superó el umbral de 150 litros
    if consumo_dia > UMBRAL_CONSUMO:
        dias_superan_umbral = dias_superan_umbral + 1

# Cálculo del promedio diario
promedio_diario = consumo_total / TOTAL_DIAS

# Resumen e informe final
print("\n==============================================")
print("       RESUMEN SEMANAL DE CONSUMO DE AGUA     ")
print("==============================================")
print("Consumo total semanal:", consumo_total, "litros")
print("Promedio diario de consumo:", promedio_diario, "litros/día")
print("Mayor consumo registrado en un solo día:", mayor_consumo, "litros")
print("Cantidad de días que superaron los 150 litros:", dias_superan_umbral, "días")