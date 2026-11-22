# Paso 1: datos de la jornada
while True:
    apertura = int(input("Hora de apertura (0 a 23): "))
    if 0 <= apertura <= 23:
        break
    print("La hora de apertura debe estar entre 0 y 23.")

while True:
    cierre = int(input("Hora de cierre (0 a 23): "))
    if 0 <= cierre <= 23 and cierre > apertura:
        break
    print("El cierre debe estar entre 0 y 23 y ser posterior a la apertura.")

while True:
    duracion = int(input("Minutos por turno: "))
    if duracion > 0:
        break
    print("La duración debe ser mayor que 0.")

# Paso 2: trabajar en minutos desde la medianoche
inicio = apertura * 60
ultimo_inicio = cierre * 60 - duracion

total_turnos = 0
for minuto in range(inicio, ultimo_inicio + 1, duracion):
    total_turnos += 1

    # Paso 3: formato del reloj
    hora_ini = minuto // 60
    min_ini = minuto % 60
    fin = minuto + duracion
    hora_fin = fin // 60
    min_fin = fin % 60

    print(f"Turno {total_turnos:2d}: {hora_ini:02d}:{min_ini:02d} a {hora_fin:02d}:{min_fin:02d}")

print(f"Turnos disponibles: {total_turnos}")