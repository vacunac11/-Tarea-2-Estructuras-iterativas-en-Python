DIAS_ATENCION = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado")
RESENAS_MES = (5, 4, 5, 3, 5, 2, 4, 5, 5, 4, 1, 5)
bicicleta = ("Trek", "Marlin 5", 29, "Rojo")   # marca, modelo, rodado, color

# Paso 1: ficha de ingreso
marca, modelo, rodado, color = bicicleta
print("=== FICHA DE INGRESO ===")
print(f"Bicicleta: {marca} {modelo}")
print(f"Rodado: {rodado} pulgadas")
print(f"Color: {color}")

# Paso 2: días de atención
print("\n=== DÍAS DE ATENCIÓN ===")
print(f"Atendemos {len(DIAS_ATENCION)} días: de {DIAS_ATENCION[0]} a {DIAS_ATENCION[-1]}.")
print("Horario completo:", ", ".join(DIAS_ATENCION[:5]))

dia = input("¿Qué día traerá su bicicleta? ").strip().capitalize()
if dia in DIAS_ATENCION:
    numero = DIAS_ATENCION.index(dia) + 1
    print(f"{dia} es el día {numero} de atención de la semana.")
else:
    print(f"El {dia.lower()} no atendemos.")

# Paso 3: reseñas del mes
print("\n=== RESEÑAS DEL MES ===")
total = len(RESENAS_MES)
for estrellas in range(5, 0, -1):
    cantidad = RESENAS_MES.count(estrellas)
    barra = "#" * cantidad
    print(f"{estrellas} estrellas | {barra:<6} {cantidad}")

promedio = sum(RESENAS_MES) / total
print(f"Reseñas: {total} | Promedio: {promedio:.1f}")
print(f"Peor: {min(RESENAS_MES)} | Mejor: {max(RESENAS_MES)}")
porcentaje = RESENAS_MES.count(5) / total * 100
print(f"Clientes muy satisfechos: {porcentaje:.0f} %")

if 1 in RESENAS_MES:
    posicion = RESENAS_MES.index(1) + 1
    print(f"Revisar la reseña número {posicion}: es la primera de 1 estrella.")